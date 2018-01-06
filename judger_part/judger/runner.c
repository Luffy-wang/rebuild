#define _GNU_SOURCE
#define _POSIX_SOURCE

#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<sched.h>
#include<wait.h>
#include<errno.h>
#include<unistd.h>

#include<sys/time.h>
#include<sys/resource.h>



#include"killer.h"
#include"runner.h"
#include"child.h"
#include"logger.h"

void init_result(struct result *_result)
{
	_result->result=_result->error=SUCCESS;
	_result->cpu_time=_result->real_time=_result->signal=_result->exit_code=0;
	_result->memory=0;
}

void run(struct config *_config,struct result *_result)
{
	//init log fp
	FILE *log_fp=log_open(_config->log_path);

	//init result
	init_result(_result);

	//check current usr is root
	uid_t uid=getuid();
	if(uid!=0)
	{
		ERROR_EXIT(ROOT_REQUIRED);
	}

	//check args
	if((_config->max_cpu_time<1 &&_config->max_cpu_time!=UNLIMITED)||
		(_config->max_real_time<1 &&_config->max_real_time!=UNLIMITED)||
		(_config->max_stack<1)||
		(_config->max_memory<1 &&_config->max_memory!=UNLIMITED)||
		(_config->max_process_number<1 &&_config->max_process_number!=UNLIMITED)||
		(_config->max_output_size<1 &&_config->max_output_size!=UNLIMITED))
	{
		ERROR_EXIT(INVALID_CONFIG);
	}

	//record current time
	struct timeval start,end;
	gettimeofday(&start,NULL);

	pid_t child_pid =fork();
	//if pid<0 means fork failure
	if(child_pid<0)
	{
		ERROR_EXIT(FORK_FATAL);
	}
	//pid==0 means subprocess
	else if(child_pid==0)
	{
		child_process(log_fp,_config);
	}
	//pid>0 means superprocess
	else if(child_pid>0)
	{
		//create a new thread to monitor process running time
		pthread_t tid=0;
		if(_config->max_real_time !=UNLIMITED)
		{
			struct timeout_killer_args killer_args;
			killer_args.timeout=_config->max_real_time;
			killer_args.pid=child_pid;
			if(pthread_create(&tid,NULL,timeout_killer,(void*)(&killer_args))!=0)
			{
				kill_pid(child_pid);
				ERROR_EXIT(PTHREAD_FAILED);
			}
		}

		int status;
		struct rusage resource_usage;
		//wait the subprocess terminate
		if(wait4(child_pid,&status,WSTOPPED,&resource_usage)==-1)
		{
			kill_pid(child_pid);
			ERROR_EXIT(WAIT_FAILED);
		}
		gettimeofday(&end,NULL);
		_result->real_time=(int)(end.tv_sec*1000+end.tv_usec/1000-start.tv_sec*1000-start.tv_usec/1000);

		//child process exit,we should cancel monitor thread
		if(_config->max_real_time!=UNLIMITED)
		{
			if(pthread_cancel(tid)!=0)
			{
				ERROR_EXIT(THREAD_CANCEL_ERROR);
			}
		}

		if(WIFSIGNALED(status)!=0)
		{
			_result->signal=WTERMSIG(status);
		}
		if(_result->signal==SIGUSR1)
		{
			_result->result=SYSTEM_ERROR;
		}
		else
		{
			_result->exit_code=WEXITSTATUS(status);
			_result->cpu_time=(resource_usage.ru_utime.tv_sec*1000+
									resource_usage.ru_utime.tv_usec/1000);
			_result->memory=resource_usage.ru_maxrss*1024;
			if(_result->exit_code!=0)
			{
				_result->result=RUNTIME_ERROR;
			}
			if(_result->signal==SIGSEGV)
			{
				if(_config->max_memory!=UNLIMITED &&
							_result->memory>_config->max_memory)
				{
					_result->result=MEMORY_LIMIT_EXCEEDED;
				}
				else
				{
					_result->result=RUNTIME_ERROR;
				}
			}
			else
			{
				if(_result->signal!=0)
				{
					_result->result=RUNTIME_ERROR;
				}
				if(_config->max_memory!=UNLIMITED &&_result->memory > _config->max_memory)
				{
					_result->result=MEMORY_LIMIT_EXCEEDED;
				}
				if(_config->max_real_time!=UNLIMITED &&_result->real_time > _config->max_real_time)
				{
					_result->result=REAL_TIME_LIMIT_EXCEEDED;
				}
				if(_config->max_cpu_time!=UNLIMITED &&_result->cpu_time > _config->max_cpu_time)
				{
					_result->result=CPU_TIME_LIMIT_EXCEEDED;
				}

			}
		}
		log_close(log_fp);

	}
}