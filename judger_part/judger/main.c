#include"argtable3.h"
#include"runner.h"

#define INT_PLACE_HOLDER "<n>"
#define STR_PLACE_HOLDER "str"

struct arg_lit *verb,*help,*version;
struct arg_int *max_cpu_time,*max_real_time,*max_process,*max_memory,*max_stack,
				*max_output_size,*uid,*gid;
struct arg_str *exe_path,*input_path,*output_path,*error_path,*args,*env,*log_path,
				*seccomp_ruler_name;
struct arg_end *end;

int main(int argc,char *argv[])
{
	void *arg_table[]={
		help=arg_litn(NULL,"help",0,1,"Display This Help And Exit"),
		version=arg_litn("v","version",0,1,"Display Version Info And Exit"),
		max_cpu_time=arg_intn(NULL,"max_cpu_time",INT_PLACE_HOLDER,0,1,"max cpu time (ms)"),
		max_real_time=arg_intn(NULL,"max_real_time",INT_PLACE_HOLDER,0,1,"max real time (ms)"),
		max_process=arg_intn(NULL,"max_process",INT_PLACE_HOLDER,0,1,"max process"),
		max_memory=arg_intn(NULL,"max_memory",INT_PLACE_HOLDER,0,1,"max memory (byte)"),
		max_stack=arg_intn(NULL,"max_stack",INT_PLACE_HOLDER,0,1,"Max stack (byte default=16M)"),
		max_output_size=arg_intn(NULL,"max_output_size",INT_PLACE_HOLDER,0,1,"max out size (byte)"),

		exe_path=arg_str1(NULL,"exe_path",STR_PLACE_HOLDER,"exe path"),
		input_path=arg_strn(NULL,"input_path",STR_PLACE_HOLDER,0,1,"input path"),
		output_path=arg_strn(NULL,"output_path",STR_PLACE_HOLDER,0,1,"output path"),
		error_path=arg_strn(NULL,"error_path",STR_PLACE_HOLDER,0,1,"error path"),

		args=arg_strn(NULL,"args",STR_PLACE_HOLDER,0,255,"Arg"),
		env=arg_strn(NULL,"env",STR_PLACE_HOLDER,0,255,"Env"),

		log_path=arg_strn(NULL,"log_path",STR_PLACE_HOLDER,0,1,"Log path"),
		seccomp_ruler_name=arg_strn(NULL,"seccomp_ruler_name",STR_PLACE_HOLDER,0,1,"seccomp ruler name"),

		uid=arg_intn(NULL,"uid",INT_PLACE_HOLDER,0,1,"uid(default 65534)"),
		gid=arg_intn(NULL,"gid",INT_PLACE_HOLDER,0,1,"gid(default 65534)"),

		end=arg_end(10),
	};

	int exit_code=0;
	char name[]="libjudger.so";

	int nerrors=arg_parse(argc,argv,arg_table);

	struct config _config;
	struct result _result={0,0,0,0,0,0,0};
	if(arg_nullcheck(arg_table)!=0)
		printf("error:insufficient memory\n");
	if(nerrors==0)
	{
		if(help->count>0)
		{
			printf("Usage: %s",name);
			arg_print_syntax(stdout,arg_table,"\n\n");
			arg_print_glossary(stdout,arg_table,"%-25s %s\n");
		}

		if(version->count>0)
		{
			printf("Version:%d.%d.%d\n",(VERSION>>16)&0xff,(VERSION>>8)&0xff,(VERSION)&0xff);
			goto exit;
		}

		if(max_cpu_time->count>0)
		{
			_config.max_cpu_time=*max_cpu_time->ival;
		}else{
			_config.max_cpu_time=UNLIMITED;
		}

		if(max_real_time->count>0)
		{
			_config.max_real_time=*max_real_time->ival;
		}else{
			_config.max_real_time=UNLIMITED;
		}

		if(max_memory->count>0)
		{
			_config.max_memory=(long)*max_memory->ival;
		}else
		{
			_config.max_memory=UNLIMITED;
		}

		if(max_process->count>0)
		{
			_config.max_process_number=*max_process->ival;
		}else
		{
			_config.max_process_number=UNLIMITED;
		}

		if(max_stack->count>0)
		{
			_config.max_stack=*max_stack->ival;
		}else
		{
			_config.max_stack=16*1024*1024;
		}

		if(max_output_size->count>0)
		{
			_config.max_output_size=(long)*max_output_size->ival;
		}else{
			_config.max_output_size=UNLIMITED;
		}

		_config.exe_path=(char *)*exe_path->sval;

		if(input_path->count>0)
		{
			_config.input_path=(char *)input_path->sval[0];
		}else{
			_config.input_path="/dev/stdin";
		}

		if(output_path->count>0)
		{
			_config.output_path=(char *)output_path->sval[0];
		}else{
			_config.output_path="/dev/stdout";
		}

		if(error_path->count>0)
		{
			_config.error_path=(char *)error_path->sval[0];
		}else{
			_config.error_path="/dev/stderr";
		}


		_config.args[0]=_config.exe_path;
		int i=1;
		if(args->count>0)
		{
			for(;i<args->count+1;++i)
			{
				_config.args[i]=(char *)args->sval[i-1];
			}
		}
		_config.args[0]=NULL;

		i=0;
		if(env->count>0)
		{
			for(;i<env->count;++i)
			{
				_config.env[i]=(char *)env->sval[i];
			}
		}
		_config.env[i]=NULL;

		if(log_path->count>0)
		{
			_config.log_path=(char *)log_path->sval[0];
		}else{
			_config.log_path="judger.log";
		}

		if(seccomp_ruler_name->count>0)
		{
			_config.seccomp_rule_name=(char *)seccomp_ruler_name->sval[0];
		}else{
			_config.seccomp_rule_name=NULL;
		}

		if(uid->count>0)
		{
			_config.uid=(uid_t)*(uid->ival);
		}else{
			_config.uid=65534;
		}

		if(gid->count>0)
		{
			_config.gid=(gid_t)*(gid->ival);
		}else{
			_config.gid=65534;
		}

		run(&_config,&_result);

		printf("{\n"
			"\"cpu_time\":%d,\n"
			"\"real_time\":%d,\n"
			"\"memory\":%ld,\n"
			"\"exit_code\":%d,\n"
			"\"error\":%d,\n"
			"\"result\":%d,\n"
			"\"signal\":%d,\n"
			"}",
			_result.cpu_time,
			_result.real_time,
			_result.memory,
			_result.exit_code,
			_result.error,
			_result.result,
			_result.signal
			);


	}
	else
	{
		arg_print_errors(stdout,end,name);
		printf("Try '%s --help' for more information",name);
		exit_code=1;
		goto exit;
	}


	exit:
	arg_freetable(arg_table,sizeof(arg_table)/sizeof(arg_table[0]));
	return exit_code;
}