### 软件安装相关
	
RPM 包安装、卸载、升级
	/etc/				：配置文件安装目录
	/usr/bin/			：可执行的命令安装目录
	/usr/lib/			：程序所使用的函数库保存位置
	/usr/share/doc/		：基本的软件使用手册保存位置
	/usr/share/man/		：帮助文件保存位置
RPM 包的安装
	rpm -ivh 包名
		-i ：安装(install)
		-v ：显示详细信息(verbose)
		-h ：打印 # 显示安装进度(hash)
	rpm -ivh x.rpm xx.rpm xxx.rpm 
	rpm 选项 包名
		-nodeps ： 不检测依赖性安装
		-replacefiles ：替换文件安装
		-replacepkgs ：替换软件包安装
		-force ：强制安装
		-test ：测试安装
		-prefix ：指定安装路径

#### 软件的启动和管理
		service 服务名 start | stop | restart | status 
			stat: 启动服务
			stop: 停止服务
			restart:	重启服务
			status:		查看服务状态
		检测端口：	
			netstat -tlun | grep 80

RPM 包的升级
	rpm -Uvh 包名	： 如没安装过则直接安装
	rpm -Fvh 包名	： 如没有安装，则不安装

RPM 包的卸载	(e 时 erase)
	rpm -e 包名  

RPM 命令查询软件包 (-q, -qa, -i ,-p, -l, -f ,-R )
	rpm 选项 查询对象
		-q  ：表示查询， query 
		-qa ：查询系统中所有安装的软件包
		-qi ：查询软件包的详细信息 i = information
		-ql ：查询软件包的文件列表
		-qf ：查询系统文件属于哪个RPM包
		-qR ：查询软件包的依赖关系

RPM 包验证和数字证书(数字签名)
	rpm 包校验 
		-Va ：校验系统中已安装的软件包
		-V  ：校验已安装的包名
		-Vf ：校验某个系统文件是否被修改

提取RPM包文件(cpio命令)
	cpio 用于从归档包中存入和读取文件
		cpio 选项 
			-o ： 指 copy-out 模式，把数据备份到文件库中
			-v ： 显示备份过程
			-c ： 使用较新的protable format 存储方式
			-B ： 设定输入/输出块为5120Bytes，而不是模式的512Bytes
			-i ： 指 copy-in ，把数据从文件库中恢复
			-d ： 还原时自动新建目录
			-u ： 自动使用较新的文件覆盖较旧的文件
			-p ： 指复制模式

YUM 源配置
	Yum 源配置文件： /etc/yum.repos.d/ ， 文件扩展名为："*.repo"
		参数：
			[base]: 容器名称
			name：容器说明
			mirrorlist：镜像站点
			baseurl：源服务器的地址
			enable：此容器是否生效， 不写或写enable表示生效，0为不生效
			gpgcheck：为1表示RPM的数字证书生效，0为不生效
			gpgkey：数字证书的公钥文件保存位置
	Yum 查询、安装、升级、卸载
		yum list : 列出已安装的和可安装的软件名
		yum list 包名 : 查询安装情况
		yum search 关键字 : 查找与关键字相关的所有软件包	
		yum info 包名 : 查询执行软件包的详细信息

Yum 安装命令
		yum -y install 包名
			install ： 安装
			-y ： 自动回答yes

Yum 升级命令
		yum -y update ： 升级所有软件包
		yum -y update 包名 ： 升级特定的软件包
	
Yum 卸载命令
		yum remote 包名 ：卸载指定的软件包

Yum 查询软件组包含的软件
		yum groupinfo 软件组名 ： 查询软件组包含的软件

Yum 安装软件组
		yum groupinstall 软件组名 ： 安装指定软件组，组名由grouplist查询出来

Yum 卸载软件组
		yum groupremove 软件组名 ： 卸载指定软件组

Linux 源码包安装和卸载
	首先安装 gcc 和 make 
		rpm -q gcc   |   yum -y install gcc
		rpm -q make  |   yum -y install make
	下载源码包，如:  xxx.tar.gz  
	解压： tar -zxvf xxx.tar.gz 
	进入解压目录
	检测系统环境是否符合安装要求： ./configure 
		定义需要的功能选项：	
			./configure --prefix=安装路径  
		执行 ./configure--help 查询支持的功能
	编译： make
	正式安装软件： make install
	重装：在make前，要执行 make clean ，他会清空 Makefile 文件或编译产生的 .o 头文件

Linux 源码包卸载
	rm -rf /usr/local/xxx  ： 删除软件的安装目录，删除前需停止服务

Linux 源码包快速升级
	使用补丁更新源码包： 省去./configure 生成新的 Makefile文件，还省去了编译
	Linux 补丁文件的生成和使用
		diff 选项 old new
			-a ： 将任何文档当作文本文档处理
			-b ： 忽略空格造成的不同
			-B ： 忽略空白行造成的不同
			-l ： 忽略大小写造成的不同
			-N ： 比较两个目录时，如某个文件只在一个目录，则另一个目录视为空
			-r ： 比较目录时，递归比较子目录
			-u ： 使用同一输出格式
	1. 创建两个文件
		mkdir test  | cd test | vi old.txt  | vim new.txt  
			
	2. 利用diff命令，比较两个文件(old.txt 和 new.txt)的不同，并生成补丁文件 (txt.patch)，执行一下代码：
		diff -Naur /roor/test/old.txt  /root/text/new.txt < txt.patch
		
给软件打入补丁
	1. 下载补丁文件 
	2. 复制补丁文件到源码包解压目录中 cp xxx.diff 软件包名
	3. 给旧软件打入补丁  cd 软件目录	| vi xxx.diff  
	4. 重新编译 软件包源码  make
	3. 安装 软件  make install










