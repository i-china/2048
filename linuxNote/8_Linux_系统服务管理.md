### 系统服务管理
	服务是后台运行的应用程序，提供本地系统或网络的功能，Service，Daemon：守护神、守护进程
	守护进程：为了实现服务、功能的进程，是服务在后台运行的真实进程
	系统服务及分类
		[服务分类](http://c.biancheng.net/uploads/allimg/181024/2-1Q02413195AP.jpg)
	软件安装方式：1. RPM包		 2. 源码包
	服务分为两种：
		独立的服务：可自动启动，不依赖管理服务，如 Nginx服务、FTP服务等
		基于Xinetd的服务：依靠管理服务来调用，管理服务是xinetd服务，是系统的超级守护进程，作用：管理不能独立启动的服务，当有客户端请求时，先请求xinetd服务，由xinetd服务去唤醒相对应的服务。

查询已安装的服务与区分服务
	RPM包默认安装到系统默认位置，可被服务管理命令(service、chkconfig)识别
	chkconfig --list 服务名		//	管理RPM包默认安装服务的自启动命令，列出所有服务的自启动状态
	
Linux端口及查询方法
	协议：
		面向连接的可靠的TCP协议(Transmission Control Protocol,传输控制协议)
		面向无连接的不可靠的UDP协议(User Datagram Protocol, 用户数据报协议)
	查询系统中已启动的服务：
		netstat 选项
			-a： 列出系统中所有网络连接，包括：网络服务、监听的网络服务、Socket套接字
			-t： 列出TCP 数据
			-u： 列出UDP 数据
			-l： 列出正在监听的网络服务(不包含已连接的网络服务)
			-n： 用端口号来显示而不用服务名
			-p： 列出该服务的进程ID(PID)
	执行结果字段解析：
		Proto： 数据包的协议
		Revc-Q：收到的数据已在本地接受缓冲
		Send-Q：对方没有收到的数据包数量
		Local Address：本地IP：端口，通过端口知道本机开启的服务
		Foreign Address：远程主机：端口，
		State： 连接状态，已建立连接(ESTABLISED)和监听(LISTEN) 
		PID/Program name: 进程ID和进程命令
	Socket套接字的解析：
		Proto：协议，一般是Unix
		RefCnt： 连接到此Socket的进程数量
		Flags：连接标识
		Type： Socket访问类型
		State：状态 Listening：监听	Connected：已建立连接
		l-Node：程序文件的i节点号
		Path：Socket程序的路径、或者相关数据的输出路径

独立服务的启动管理(RPM包的启动与自启动)
	两种方式：
		1. 使用/etc/init.d/ 目录中的启动脚本来启动独立的服务
			/etc/init.d/独立服务名 start|stop|status|restart|...
				start：启动服务
				stop ：停止服务
				status：服务状态
				restart：重启服务
		2. 使用service命令来启动独立的服务
			service 只是一个脚本，调用/etc/init.d/ 中的启动脚本来启动独立服务
			service 独立服务名 start|stop|restart|...
				--status-all :列出所有独立服务的启动状态
独立服务的自启动管理
	三种方式：
		1. 使用chkconfig服务自启动管理命令
			chkconfig --list    // 查询自启动状态
				chkconfig --list | grep nginx	
			chkconfig [--level 运行级别][独立服务名][on|off]
				--level：设定在哪个运行级别中开机自启动(on)，关闭自启动(off)
				chkconfig --level 2345 nginx on		// 修改2345这4个级别为启用
			/etc/init.d/nginx status	//	查看服务状态
		2. 修改 /etc/rc.d/rc.local 文件，设置服务自启动
			修改 rc.local 文件，添加服务的启动命令，注：/etc/rc.d/rc.local 和 /etc/rc.local 文件时软连接，修改哪个都可以，这个文件中的命令会在启动时调用
			vi /etc/rc.d/rc.local
				/etc/rc.d/init.d/nginx start
				# 在文件中加入nginx的启动命令
			好处：
				1. 集中管理
				2. 服务启动唯一性，不管哪种方式都通过 /etc/rc.d/rc.local 文件实现
		3. 使用ntsysv 命令管理自启动
			ntsysv：调用窗口模式管理服务的自启动
			ntsysv [--level 运行级别]
				ntsysv --level 234
				# 设定234级别的服务自启动

Linux基于xinetd服务的管理方法
	基于xinetd服务的启动
		xinetd 服务的配置文件保存在 /etc/xinetd.d/ 目录中
			telnet： /etc/xinetd.d/telnet 
			如果要启动telnet服务，只需把 /etc/xinetd.d/telnet 文件中的disable=yes 改为 disable=no    ，disable:代表取消
	基于xinetd服务的自启动
		1. 使用chkconfig 命令管理自启动
			chkconfig 服务名 on|off
		2. 使用ntsysv命令管理自启动
			
Linux源码包服务管理(启动与自启动)
	源码包服务的启动管理：
		/usr/local/apache2/bin/apachectl start|stop|restart|status|...
	源码包服务的自启动管理：
		vim /etc/rc.d/rc.local			// 修改自启动文件
			touch /var/lock/subsys/local /usr/local/apache2/bin/apachectl start 
			# 加入源码包服务的标准启动命令
	让源码包服务被服务管理命令识别：
		1. 卸载RPM包默认安装的apache服务
			yum -y remove httpd
		2. 安装源码包的apache服务，并启动
			/usr/local/apache2/bin/apachectl start
			netst -tlun | grep 80
		3. 让源码包安装的apache服务能被service命令管理启动
			ln -s /usr/local/apache2/bin/apachectl /etc/init.d/apache 
			# 把源码包的启动脚本连接到 /etc/init.d/目录中，能被service命令管理
		4. 让源码包安装的apache服务能被chkconfig命令管理自启动
			vi /etc/init.d/apache
				# 修改源码包安装的apache服务的启动脚本，此文件是软连接，实际修改的是源码包的启动脚本
				chkconfig: 运行级别 启动顺序 关闭顺序
			chkconfig --add apache
			chkconfig --list | grep apache
		5. 让ntsysv命令可以管理源码包安装的apache服务
				把服务的启动脚本链接到/etc/init.d/目录中，在启动脚本中加入：
				#chkconfig:运行级别 启动顺序 关闭
				#description:说明
				然后使用： chkconfig --add 服务名
					chkconfig 选项服务名
						-add： 把服务加入chkconfig命令的管理中
						-del： 把服务从chkconfig命令的管理中删除
						chkconfig -del|httpd

Linux常见服务类被及功能
	acpid：	电源管理接口
	anacron：	系统的定时任务，是cron的子系统
	alsasound： alsa声卡驱动
	apmd：	电源管理模块
	atd：指定系统在特定时间执行某个任务，只能执行一次
	auditd：审核子系统
	autofs：让服务器可自动挂载网络中其服务器的共享数据，挂载NFS服务
	avahi-daemon：avahi是zeroconf协议的实现
	bluetooth：蓝牙设备支持
	capi：仅对ISND设备用户有用
	chargen-dgram：使用UDP协议的chargen server，类远程打字功能
	chargen-stream： 同上
	cpuspeed：调整CPU频率
	crond：系统定时任务
	cvs：版本控制系统
	... More
	[常见服务](http://c.biancheng.net/view/1059.html)

