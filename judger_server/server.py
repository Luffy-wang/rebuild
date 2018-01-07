import web
import json
import os


from utils import server_info,logger
urls=("/judge","JudgerServer",
		"/ping","JudgerServer",
		"/spj_judge","JudgerServer")

class JudgerServer(object):
	def judge(self):
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
