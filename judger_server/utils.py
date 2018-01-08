import _judger
import socket
import psutil
import logging

def server_info():
	version=_judger.VERSION
	return {"hostname":socket.gethostname(),
			"cpu":psutil.cpu_percent(),
			"cpu_core":psutil.cpu_count(),
			"memory":psutil.virtual_memory().percent,
			"version":".".join([str((version>>16)&0xff),str((version>>8)&0xff),str(version&0xff)])
			}

def get_token():


