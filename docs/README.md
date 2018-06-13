# Hello VuePress

项目基于Django2.0开发，python3支持
前端使用vue


后端模块组成：
   account(用户管理模块)
	url:
		URL/account/loginorlogout   
			get：
				参数：NULL
				返回值：NULL
				介绍：用于注销用户
			post：
				参数： user_id(数字)，password(字符串),
				返回值： 
					data：1  登录成功 name：用户名称
					data：0  登录失败 msg：验证失败
					data：2   登录失败 msg：已登录，请不要重复登录
				介绍：用于用户登录

			put：
				参数：user_id(数字)，newwpd(字符串),oldpwd(字符串)
				返回值：
					data：1  修改成功 msg：修改成功
					data：0  修改失败 msg：验证失败
				介绍：
					提供修改用户密码功能，当用户类型为Student时，user_id自动赋值为当前学生id

		URL/account/userregister
			post：
				参数： userinformation(文件流)
				返回值：
					data：1 上传成功 msg：上传成功
					data：2 上传失败 msg：上传失败
				介绍：
					接收excel表格，表格格式为 第一列用户id，第二列用户名，成功上传则创建用户，默认密码123456

		URL/account/show/
			get：
				参数： page(数字)，不提供或错误参数则默认为 1
				返回值：
					'''JSON格式'''
					user_id, user_name, email, user_type, create_time,
				介绍：
					显示10条用户信息

		URL/account/edittype
			get:
				参数：NULL
				返回值：
					data：1 user_type:用户类型
					data：0 user_type:游客
				介绍：
					获取当前用户的用户类型

			post:
				参数： type(字符串(Teacher,Student,Admin))
					user_id(数字)
				返回值：
					data：1 msg：修改成功
					data：2 msg：修改失败
				介绍：
					修改用户权限类型，可选参数:Teacher,Student,Admin


   homework(作业模块)
	url:
		URL/homework/showhomework
			get:
				参数：page(数字)
				返回值：
					class_name,homework_item,homework_item_title
					data:0  msg:无相关权限
							参数错误
							not teacher or admin
				介绍：
					返回当前登录用户所在班级的作业，需要Teacher或者Admin权限
			post:
				参数：homework_item
					homework_item_title
				返回值：
					data：1 msg：创建成功
					data：0 msg：serializer.errors
				介绍：
					根据当前登录用户所在班级，创建作业项

			delete:
				参数： homework_item
				返回值：
					data：1 msg：删除成功
					data：0 msg：删除失败
				介绍：
					删除作业项

		URL/homework/showclassproblem
			get：
				参数：homework_item(字符串)
				返回值：
					data：0 msg：请求作业项不存在
					
					class_name，homework_item,problem_id，problrm_title
				介绍：
					获取所请求的作业项中的题目

			post:
				参数：homework_item(字符串)，problem(数组)
				返回值：
					data：1 msg：创建成功
					data：0 msg：创建失败
				介绍：
					根据提供的homework_item和problem_id,添加题目到相应的题目

			delete：
				参数：homework_item,problem
				返回值：
					data：1，msg：删除成功
					data：0, msg：删除失败
				介绍：
					根据提供参数，删除相应的题目
   myclass(班级模块)
   problem(问题模块)
   submission(提交模块)
   utils(工具类)
   docs(文档)
   spider(简易爬取题目模块)
