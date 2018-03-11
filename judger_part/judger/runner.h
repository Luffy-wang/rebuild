#ifndef JUDGER_RUNNER_H
#define	JUDGER_RUNNER_H

#include<sys/types.h>
#include<stdio.h>

#define VERSION	 0x020001

#define UNLIMITED -1

#define LOG_ERROR(error_code) LOG_FATAL(log_fp,"Error:"#error_code);

#define ERROR_EXIT(error_code)\
	{\
		LOG_ERROR(error_code);\
		_result->error=error_code;\
		log_close(log_fp);\
		return;\
	}

#define ARGS_MAX_NUMBER 256
#define ENV_MAX_NUMBER	256

enum{
	SUCCESS=0,
	INVALID_CONFIG=-1,
	FORK_FATAL=-2,
	PTHREAD_FAILED=-3,
	WAIT_FAILED=-4,
	ROOT_REQUIRED=-5,
	LOAD_SECCOMP_FAILED=-6,
	SETRLIMIT_FAILED = -7,
    DUP2_FAILED = -8,
    SETUID_FAILED = -9,
    EXECVE_FAILED = -10,
    SPJ_ERROR = -11,
    THREAD_CANCEL_ERROR=-12
};

struct config{
	int max_cpu_time;
    int max_real_time;
    long max_memory;
    long max_stack;
    int max_process_number;
    long max_output_size;
    char *exe_path;
    char *input_path;
    char *output_path;
    char *error_path;
    char *args[ARGS_MAX_NUMBER];
    char *env[ENV_MAX_NUMBER];
    char *log_path;
    char *seccomp_rule_name;
    uid_t uid;
    gid_t gid;
};

enum{
	WRONG_ANSWER = -1,
    CPU_TIME_LIMIT_EXCEEDED = 1,
    REAL_TIME_LIMIT_EXCEEDED = 2,
    MEMORY_LIMIT_EXCEEDED = 3,
    RUNTIME_ERROR = 4,
    SYSTEM_ERROR = 5
};

struct result
{
	int cpu_time;
    int real_time;
    long memory;
    int signal;
    int exit_code;
    int error;
    int result;
};

void run(struct config *,struct result *);
#endif
