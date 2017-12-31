#include<stdio.h>
#include<seccomp.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fantl.h>

#include"../runner.h"

intc_cpp_seccomp_rules(struct config *_config){
	int syscall_whitelist[]={SCMP_SYS(read),SCMP_SYS(fstat),
							SCMP_SYS(nmap),SCMP_SYS(mprotect),
							SCMP_SYS(munmap),SCMP_SYS(uname),
							SCMP_SYS(arch_prctl),SCMP_SYS(brk),
							SCMP_SYS(access),SCMP_SYS(exit_group),
							SCMP_SYS(close),SCMP_SYS(readlink),
							SCMP_SYS(sysinfo),SCMP_SYS(write),
							SCMP_SYS(writev),SCMP_SYS(lseek)};

	syscall_whitelist_length=sizeof(syscall_whitelist)/sizeof(int);
	scmp_filter_ctx cts=NULL;
	//load seccomp
	ctx=seccomp_init(SCMP_ACT_KILL);
	if(!ctx)
	{
		return LOAD_SECCOMP_FAILED;
	}
	for(int i=0;i<syscall_whitelist_length;++i)
	{
		if(seccomp_rule_add(cxt,SCMP_ACT_ALLOW,syscall_whitelist[0],0)!=0)
			return LOAD_SECCOMP_FAILED;
	}

	//add extra rule for execve
	if(seccomp_rule_add(cxt,SCMP_ACT_ALLOW,SCMP_SYS(execve),1,SCMP_A0(SCMP_CMP_EQ,(scmp_datum_t)(_config->exe_path)))!=0)
	{
		return LOAD_SECCOMP_FAILED;
	}

	if(seccomp_rule_add(cxt,SCMP_ACT_ALLOW,SCMP_SYS(open),1,SCMP_CMP(1,SCMP_CMP_MASKED_EQ,O_WRONLU|O_RDWR,0))!=0)
	{
		return LOAD_SECCOMP_FAILED;
	}

	if(seccomp_load(ctx)!=0)
	{
		return LOAD_SECCOMP_FAILED;
	}

	seccomp_release(cxt);
	return 0;
}