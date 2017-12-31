#define _DEFAULT_SOURCE
#define _POSIX_SOURCE
#define _GNU_SOURCE


#include<stdio.h>
#include<stdargs.h>
#include<signal.h>
#include<unistd.h>  //for system call
#include<string.h>
#include<grp.h>     //for gid type
#include<dlfcn.h>   //for .so
#include<errno.h>
#include<stdlib.h>
#include<sched.h>   //for process?

#include<sys/resource.h>
#include<sys/time.h>
#include<sys/mount.h>
#include<sys/types.h>

#include"runner.h"
#include"child.h"
#include"logger.h"
#include"killer.h"
#include"rules/seccomp_rules.h"
void close_file(FIle *fp,...)
{
	va_list ap;
	va_start(fp,ap);
	if(fp!=NULL)
	{
		fclose(fp);
	}

	va_end(ap);
}

void child_process(FILE *fp,struct config *_config)
{
	FILE *input_file=NULL,*output_file=NULL,*error_file=NULL;
	
	if(_config->max_stack!=UNLIMITED)
	{
		struct rlimit max_stack;
		max_stack.rlim_cur=max_stack.rlim_max=(rlim_t)(_config->max_stack);
		if(setrlimit(RLIMIT_STACK,&max_stack)!=0)
		{
			CHILD_ERROR_EXIT(SETRLIMIT_FAILED);
		}
	}

	if(_config->max_memory!=UNLIMITED)
	{
		struct rlimit max_memory;
		max_memory.rlim_cur=max_memory.rlim_max.rlim_max=(rlim_t)(_config->max_memory)*2;
		if(setlimit(RLIMIT_AS,&max_memory)!=0)
		{
			CHILD_ERROR_EXIT(SETRLIMIT_FAILED);
		}
	}

	if(_config->max_cpu_time!=UNLIMITED)
	{
		struct rlimit max_cpu_time;
		max_cpu_time.rlim_cur=max_cpu_time.rlim_max=(rlim_t)((_config->max_cpu_time+1000)/1000);
		if(setrlimit(RLIMIT_CPU,&max_cpu_time)!=0)
		{
			CHILD_ERROR_EXIT(SETRLIMIT_FAILED);
		}
	}

	if(_config->max_process_number!=UNLIMITED)
	{
		struct rlimit max_process_number;
		max_process_number.rlim_cur=max_process_number.rlim_max=(rlim_t)(_config->max_process_number);
		if(setrlimit(RLIMIT_NPROC,&max_process_number)!=0)
		{
			CHILD_ERROR_EXIT(SETRLIMIT_FAILED);
		}
	}

	if(_config->max_output_size!=UNLIMITED)
	{
		struct rlimit max_outut_szie;
		max_output_size.rlim_cur=max_output_size.rlim_max=(rlim_t)(_config->max_output_size);
		if(setrlimit(RLIMIT_FSIZE,&max_output_size)!=0)
		{
			CHILD_ERROR_EXIT(SETRLIMIT_FAILED);
		}
	}


	if(_config->input_file!=NULL)
	{
		input_file=fopen(_config->input_file,"r");
		if(input_file==NULL)
		{
			CHILD_ERROR_EXIT(DUP2_FAILED);
		}
		if(dup2(fileno(input_file),fileno(stdin))==-1)
		{
			CHILD_ERROR_EXIT(DUP2_FAILED);
		}
	}

	if(_config->output_file!=NULL)
	{
		output_file=fopen(_config->output_file,"w");
		if(output_file==NULL)
		{
			CHILD_ERROR_EXIT(DUP2_FAILED);
		}
		if(dup2(fileno(output_file),fileno(stdout))==-1)
		{
			CHILD_ERROR_EXIT(DUP2_FAILED);
		}
	}

	if(_config->error_file!=NULL)
	{
		if(_config->output_file!=NULL &&strcmp(_config->output_file,_config->error_file)==0)
		{
			error_file=output_file;
		}
		else{
			error_file=fopen(_config->error_file,"w");
			if(error_file==NULL)
			{
				CHILD_ERROR_EXIT(DUP2_FAILED);
			}
		}
		if(dup2(fileno(error_file),fileno(stderr))==-1)
		{
			CHILD_ERROR_EXIT(DUP2_FAILTED);
		}
		
	}

	git_t group_list[]={_config_gid};
	if(_config->gid=-1 &&(setgid(_config->gid)==-1 ||setgroups(sizeof(group_list)/sizeof(gid_t),group_list)==-1))
	{
		CHILD_ERROR_EXIT(SETUID_FAILED);
	}

	//set uid
	if(_config->uid!=-1 &&setuid(_config->uid)==-1)
	{
		CHILD_ERROR_EXIT(SETGID_FAILED);
	}

	//load seccomp
	if(_config->seccomp_ruler_name!=NULL)
	{
		if(strcmp("c_cpp",_config->seccomp_rules_name)==0)
		{
			if(c_cpp_seccomp_rules(_config)!=SUCCESS)
			{
				CHILD_ERROR_EXIT(LOAD_SECCOMP_FAILED);
			}
		}
		else if(strcmp("general",_config->seccomp_rules_name)==0)
		{
			if(general_seccomp_rules_(_config)!=SUCCESS)
			{
				CHILD_ERROR_EXIT(LOAD_SECCOMP_FAILED);
			}
		}
		else
		{
			CHILD_ERROR_EXIT(LOAD_SECCOMP_FAILED);
		}
	}

	execve(_config->exe_path,_config->args,_config->env);
	CHILD_ERROR_EXIT(EXECVE_FAILED);
}