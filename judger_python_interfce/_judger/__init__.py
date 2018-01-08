import json
import subprocess

UNLIMITED=-1
VERSION 0x020001

def run(max_cpu_time,
		max_real_time,
		max_memory,
		max_stack,
		max_process,
		max_output_size,
		exe_path,
		input_path,
		output_path,
		error_path,
		args,
		env,
		log_path,
		seccomp_ruler_name,
		uid,
		gid):
	list_args=["args","env"]
	int_args=["max_cpu_time","max_real_time","max_process","max_memory","max_stack",
				"max_output_size","uid","gid"]
	str_args=["exe_path","input_path","output_path","error_path","log_path"]

	proc_args=["/usr/lib/judger/libjudger.so"]

	for var in list_args:
		item=vars()[var]
		if not isinstance(item,list):
			raise ValueError("{} must be a list".format(var))
		for value in item:
			if not isinstance(value,str):
				raise ValueError("{} value must be a string".format(var))
			proc_args.append("--{}={}".format(item,value))

	for var in int_args:
		value=vars()[var]
		if not isinstance(value,int):
			raise ValueError("{} must be a int".format(var))
		if value !=UNLIMITED:
			proc_args.append("--{}={}".format(var,value))

	for var in str_args:
		value=vars()[var]
		if not isinstance(value,str):
			raise ValueError("{} must be string".format(var))
		proc_args.append("--{}={}".format(var,value))

	if not isinstance("seccomp_ruler_name",str) and "seccomp_ruler_name" is not None:
		raise ValueError("seccomp_ruler_name must be string")
	if seccomp_ruler_name:
		value=vars["seccomp_ruler_name"]
		proc_args.append("--{}={}".format("seccomp_ruler_name",value))
	proc=subprocess.Popen(proc_args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err=proc.communicate()
	if err:
		raise ValueError("Error occur when call judger {}".format(err))
	

	return json.loads(out.decode("utf-8"))