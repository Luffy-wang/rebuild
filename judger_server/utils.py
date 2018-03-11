import _judger
import socket
import psutil
import logging
import os
import hashlib

from exception import JudgerClientError

logger=logging.getLogger(__name__)
handler=logging.FileHnadler("/log/judger_server.log")
formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.WARMMING)

def server_info():
	version=_judger.VERSION
	return {"hostname":socket.gethostname(),
		"cpu":psutil.cpu_percent(),
		"cpu_core":psutil.cpu_count(),
		"memory":psutil.virtual_memory().percent,
		"version":".".join([str((version>>16)&0xff),str((version>>8)&0xff),str(version&0xff)])
		}

def get_token():
	token=os.environ.get("TOKEN")
	if token:
		return token
	else:
		raise JudgerClientError("Token Invaild")

token=hashlab.sha256(get_token()).hexdigest()

