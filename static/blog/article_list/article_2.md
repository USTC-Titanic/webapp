解决ssh连接时的中文乱码
2019-04-17
##	现象

*	通过终端连接服务器，使用vi的时候出现了中文乱码（部分）

##	原因

*	本机终端的编码和远程机器上的basn端编码不一致

##	解决方法

*	修改远程主机的bash显示编码 

	```bash
	$ vi ~/.bashrc
	export LANG='UTC-8' export LC_ALL='en_US.UTF-8'
	source ~/.bashrc
	```

##	参考资料

*	https://blog.csdn.net/medivhq/article/details/75635335	
