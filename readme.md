##	简介

*	测试主页 [https://ustc-titanic.xyz](https://ustc-titanic.xyz)

*	后端框架用的是 `Flask`, 机器学习模块使用的是 `numpy, pandas, sklearn`, 前端框架用的是 `Vue.js`

*	工作流程如下：前端输入乘客信息并提交给服务器，服务器将信息转发给训练好的机器学习模块，后者进行预测后将结果返回给服务器，最终返回给前端并展示生存指数

*	[文档记录](https://segmentfault.com/u/frozenmap/articles)

	<br>

##	如何运行

*	开发环境

	```
	Ubuntu 16.04
	Python 3.5+
	Flask 1.0.2
	```

*	首先下载整个工程，然后修改 `./server.py`, 注释掉第 `9` 行, 然后取消第 10 行的注释

*	在 bash 中运行如下命令

	```bash
	python3 server.py
	```

*	打开浏览器, 输入 `127.0.0.1:8000` 即可在本地进行查看和调试

	<br>

##	更新记录

*	20190124, 搭建了基本的 demo, 在 index 页面提交信息后, 随机返回 Survived 或者 Fallen

*	20190219, 改进前端 UI, 改进前后端接口(使用json进行交互), 后端改进 IndexHandler, 使用 [let's encrypt]() 颁发的 HTTPS 证书并开启 HSTS, 增加机器学习模块

	<br>

##	TODO

*	前端

	*	对输入进行过滤, 比如 `年龄`, `兄弟姐妹数量` 等选项只能输入数字, 否则要求用户重新输入

	*	完善 `index` 页面的表单信息, 使与 `Titanic` 输入特征一致

	*	完善界面

	*	增加注册、登录页面

*	后端

	*	增加注册、登录模块

	<br>

##	参考资料

*	http://flask.pocoo.org/docs/1.0/api

*	https://vuejs.org/index.html

*	https://segmentfault.com/u/frozenmap/articles

	<br>

##	附录

*	常用命令

	*	tar

		```bash
		# Compress
		tar -zcvf archive_name.tar.gz folder_to_compress

		# Extract
		tar -zxvf archive_name.tar.gz
		```

	*	how to delete all `.DS_Store` files

		```bash
		find . -name '.DS_Store' -type f -delete
		```

	*	how to terminate a process

		```
		$ pgrep -l python
		22509 python3
		$ kill -9 22509

		# or combine the two commands
		$ kill -9 `pgrep python`
		```

	*	copy and paste

		```
		Ctrl + Insert => copy
		Shift + Insert => paste
		```
