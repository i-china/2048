### Python 编程基础
	[编译型和解释型](http://c.biancheng.net/uploads/allimg/190211/2-1Z2111G33L03.gif)
	领域：
		Web应用开发：
			通过mod_wsgi模块，apache可运行python的web程序，Python定义WSGI标准应用接口协调HTTP服务器与基于Python的Web程序之间的通信。Web框架：Django、TurboGears、web2py等
		操作系统管理、自动化运维开发：
			例：Ubunut的Ubiquity安装器、RedHat、Fedora的Anaconda安装器等
		游戏开发：
			支持更多的特性和数据类型，例：文明
		编写服务器软件：
			支持各种网络协议，可编写服务器软件及网络爬虫，例：第三方库Twisted
		科学计算：
			NumPy、SciPy、Matplotlip等
	3和2的区别：
		print函数代替print语句
		默认使用UTF-8编码
		除法运算
		异常
		八进制字面量表示
		不等于运算符
		数据类型
	Python 2to3：自动将Python2.x代码转换为Pyhton3.x代码

安装
	Linux 两种方式：
		1. 命令行安装
			apt update
			apt install python3.6 
			unlink /usr/bin/python		//	取消旧python的映射
			ln -s /usr/bin/python3.6 /usr/bin/python		// python3环境的路径和版本要写正确
		2. 源码安装
			下载：	wget python3.6下载路径
			压缩：	tar -zxvf python3.6.tgz
			编译：	./configure --prefix=/usr/local/	make	make install
					
###	第一个python

```
代码编写
	两种方式：
		1. 在提示符 >>> 直接输入： print("hello world")
		2. 文本编辑器编写并执行python程序
			vim hi.python
				print("hello world")
			python hi.python
			
注释：
	单行注释： #  
	多行注释： 1. '''  xxx...xxx '''	2. """ xxx...xxx """

中文编码声明注释：
	1. # -*-coding:utf-8 -*-	2. # coding=utf-8
	
缩进规则：
	冒号(:)和代码缩进

编码规范(PEP8)
	PEP: Python Enhancement Proposal, 8代表Pyton代码的样式指南
		1. 每个import语句只导入一个模块，避免导入多个
		2. 不在行为加分号，不将两条命令放一行
		3. 每行不超80字符，如超，用小括号连接
		4. 用空行增强可读性，顶级定义空两行，方法定义空一行
		5. 使用空格分隔 运算符、函数参数

Python标识符命名规范
	1. 字符、下划线、数字，数字不开头
	2. 不与保留子相同
	3. 不包含空格、@、%、$等特殊字符
	4. 严格区分大小写
	5. 下划线开头有特殊意义
		单下划线： 不能直接访问的类属性，无法通过 from ... import * 的方式导入
		双下划线： 类的私有成员
		双下划线开头和结尾： 专用标识符

关键字(保留子)
	查看方式：
		import keyword
		keyword.kwlist

内置函数
	[内置函数](https://docs.python.org/zh-cn/3/library/functions.html)



```


