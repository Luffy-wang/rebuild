import web
import json
import os


from utils import server_info,logger

urls=("/judge","JudgerServer",
		"/ping","JudgerServer",
		"/spj_judge","JudgerServer")

class InitSubmissionEnv(object):
	def __init__(self,judger_workspace,submission_id):
		self.path=os.path.join(judger_workspace,submission_id)

	def __entry__(self):
		try:
			os.mkdir(self.path)
			os.chmod(self.path,0777)
		except Exception as e:
			logger.exception(e)
			raise JudgerClientError("faild to clean the runtime env")

	def __exit__(self,exc_type,exc_val,exc_tb):
		if not DEBUG:
			try:
				shutil.rmtree(self.tree)
			except Exception as e:
				logger.exception(e)
				raise JudgerClientError("fail to clean the dir")



class JudgerServer(object):
	def judge(self,language_config,src,max_cpu_time,max_memory,test_case_id,
			spj_version=None,spj_config=None,spj_compile_config=None,spj_src=None,
			output=False):

		compile_config=language_config.get("compile")
		run_config=language_config["run"]
		submission_id=str(uuid.uuid4())

		if spj_config and spj_version:
			spj_exe_path=os.path.join(SPJ_EXE_DIR,spj_config["name"].format(spj_version=spj_version))
			if not os.path.isfile(spj_exe_path):
				logger.warning("%s does not exit,spj src will will be compiled")
				self.compile_spj(spj_version=spj_version,src=spj_src,
								spj_compile_config=spj_compile_config)
		with InitSubmissionEnv(JUDGER_WORKSPACE_BASE,submission_id=str(submission_id)) as submission_dir:
				if compile_config:
					src_path=os.path.join(submission_dir,compile_config["src_name"])
					with open(src_path,"w") as f:
						f.write(serc.encode("utf-8"))

				exe_path=Compiler().compile(compile_config=compile_config,
											src_path=src_path,
											output_dir=submission_dir)
				else:
					exe_path=os.path.join(submission_dir,run_config["exe_name"])
					with open(exe_path,"w") as f:
						w.write(src.encode("utf-8"))


	def pong(self):
		data=server_info()
		data["action"]="pong"  #add element
		return data
	def spj_judge(self):

	def POST(self):
		_token=web.ctx.env.get("HTTP_X_JUDGE_SERVER_TOKEN",None)

		try:
			if _token!=token: #token part
				raise TokenVerificationFailed("Invalid token")

			if web.data():
				try:
					data=json.loads(web.data())
				except Exception as e:
					logger.info(web.data())
					return {"return":"error","data":web.data()}
			else:
				data={}

			if web.ctx["path"]="/judge":
				callback=self.judge
			elif web.ctx["path"]="/ping":
				callback=self.pong
			elif web.ctx["path"]="spj_judge":
				callback=self.spj_judge
			else:
				return json.dumps({"error":"Invalid method","data":data})
			return json.dumps({"error":None,"data":callback(**data)})

app.application(urls,globals())

if __name__=="__main__":
	app.run()
