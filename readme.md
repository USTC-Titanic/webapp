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
	Vue.js v2.5.13
	axios v0.17.1
	Bootstrap v4.0.0
	```

*	首先在 bash 中运行如下命令, 以便对用户数据库进行初始化

	```bash
	$ export FLASK_APP=server
	$ python3 -m flask initdb
	```

	然后启动 server

	```bash
	python3 server.py
	```

*	打开浏览器, 输入 `127.0.0.1:8080` 即可在本地进行查看和调试

	<br>

##	更新记录

*	20190124, 搭建了基本的 demo, 在 index 页面提交信息后, 随机返回 Survived 或者 Fallen

*	20190219, 改进前端 UI, 改进前后端接口(使用json进行交互), 后端改进 IndexHandler, 使用 [let's encrypt](https://letsencrypt.org) 颁发的 HTTPS 证书并开启 HSTS, 增加机器学习模块

*	20190319, 增加数据库模块, 增加注册、登录、登出模块。加盐密码, hmac cookie

	<br>

##	TODO

*	前端

	*	对输入进行过滤, 比如 `年龄`, `兄弟姐妹数量` 等选项只能输入数字, 否则要求用户重新输入

	*	修改首页, 参考 [tensorfly](http://tensorfly.cn) 和 [training](http://training.ustc.edu.cn/), 完善界面

	*	完善 `Huygens` 页面的表单信息, 使与 `Titanic` 输入特征一致

*	后端

	*	增加预测模块

*	其他

	*	学习 tensorboard, 记录准确率变化曲线

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

	*	nohup, run a command immune to hangups, with output to a non-tty

		一般来说, 在命令后面加上 `&`, 可以让命令在后台运行, 相当于 `fork` 出了一个子进程, 比如

		```bash
		python3 server.py &
		```

		但是如果 `shell` 被关掉了, 这些子进程就变成了僵尸进程, 我们的 `server` 也将不再对外提供服务

		为了保证 `shell` 被关闭后, `server` 仍然正常运行, 我们需要借助 `nohup`, 用法也很简单, 直接在命令前加上 `nohup` 就可以了

		```bash
		nohup python3 server.py &
		```

		同时, `nohup` 还会帮我们把日志输出到当前文件夹下的 `nohup.out` 文件, 一举两得(因为关掉 `shell` 后, `stdout` 也被关掉了)

	*	[How to run scripts on start up?](https://askubuntu.com/questions/814/how-to-run-scripts-on-start-up)

		```bash
		crontab -e
		@reboot /path/to/script
		```

		结合 `nohup` 一起使用