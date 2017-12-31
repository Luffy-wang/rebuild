#include<stdio.h>
#include<seccomp.h>
#include<sys/types.h>
#include<errno.h>
#include<sys/stat.h>
#include<fantl.h>

#include"../runner.h"

int general_seccomp_rules(struct config *_config){
	syscall_blacklist[]={
		SCMP_SYS(clone),SCMP_SYS(fork),
		SCMP_SYS(forkv),SCMP_SYS(kill),
		#ifdef __NR_execveat
			SCMP_SYS(execveat)
		#endif
	};

	int syscall_blacklist_length=sizeof(syscall_blacklist)/sizeof(int);
	scmp_filter_ctx ctx=NULL;
	ctx=seccomp_init(SCMP_ACT_ALLOW);
	if(!ctx)
	{
		return LOAD_SECCOMP_FAILED;
	}
	for(int i=0;i<syscall_blacklist_length;++i)
	{
		if(seccomp_rule_add(ctx,SCMP_ACT_KILL,syscall_blacklist[0],0)!=0)
		{
			return LOAD_SECCOMP_FAILED;
		}
	}

	if(seccomp_rule_add(ctx,SCMP_ACT_ERRNO(EACCESS),SCMP_SYS(socket),0)!=0)
	{
		return LOAD_SECCOMP_FAILED;
	}

	//add extra rules
	if(seccomp_rule_add(ctx,SCMP_ACT_KILL,SCMP_SYS(execve),1,SCMP_V0(SCMP_CMP_NE,(scmp_datum_t)(_config->exe_path)))!=0)
	{
		return LOAD_SECCOMP_FAILED;
	}

	if(seccomp_rule_add(ctx,SCMP_ACT_KILL,SCMP_SYS(open),SCMP_CMP()))
	{
		return LOAD_SECCOMP_FAILED;
	}

	if(seccomp_rule_add(ctx,SCMP_ACT_KILL,SCMP_SYS(open))
	{
		return LOAD_SECCOMP_FAILED;
	}

	if(seccomp_rule_add(ctx,SCMP_ACT_KILL,SCMP_SYS()))
	{
		return LOAD_SECCOMP_FAILED;
	}

	if(seccomp_rule_add(ctx,SCMP_ACT_KILL,SCMP_SYS()))
	{
		return LOAD_SECCOMP_FAILED;
	}
}