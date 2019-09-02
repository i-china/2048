源码安装： 
--prefix=/usr/local 软件家目录
--bindir=$prefix/bin	命令的目录
--etcdir=$prefix/etc	配置文件的目录
--mandir=$prefix/share/man	文档路径
--locale=$prefix/share/locale	语言编码


编译：
	make (使用gcc编译器编译)

安装：
	make install  

总结： ./configure 
\
Makefile	make	make install 

rpm : rpm -ivh xxx.rpm 
	rpm -q xxx		// 查看软件是否安装
	rpm -e xxx		// 卸载软件

yum 的使用
yum list | grep xxx		// 查找软件包
yum clean all	// 清空yum缓存
yum makecache	// 创建yum缓存


端口设定：
1～255 ： 知名端口号： 21 22 23 25 53 80 110  
256～1023: Unix系统占用提供特定的服务
1024～5000：客户端临时端口
大于5000：预留服务

查看系统默认的注册端口： /etc/services 

1. 独立服务：
	启动方式： /etc/init.d/xxx start or /etc/rc.d/init.d/xxx start   or service xxxx start 
2. 依赖服务：
	xinetd:	扩展的网络守护进程
	eg: Tcp_Wrappers 一种安全策略机制


SSH ： 远程管理工具 Secure Shell 默认端口 22 
	dsa： 对称的公钥加密算法  安全低，速度快
	rsa： 非对称的公钥加密算法 安全 速度慢，默认的加密算法

	基于密码认证	基于密钥认证

SSH   免密登录
	1. Client端的用户生成一对密钥对 秘钥
	useradd username 
	ssh-keygen		// 生成秘钥文件 保存位置为：~/.ssh
	2. 将生成的公钥远程拷贝到Server端
	保存到root家目录指定位置，~/.ssh 指定文件名	authorized_keys 

	1. 在本地，生成 rsa 公私密钥对
		ssh-keygen			// 如有直接使用，不需要重新生成
	2. 将公钥文件 scp 到远程服务器
		scp .ssh/id_rsa.pub root@39.106.208.58:~
	3. 在远程服务器，将公钥文件添加到 ~/.ssh/authorzied_keys内

SSH 别名登录
	在 ～/.ssh/config 文件中加入如下内容
		Host aliasName
			HostName ipaddress|server_host_name
			Port	22
			User root
			IdentityFile	~/.ssh/id_rsa

