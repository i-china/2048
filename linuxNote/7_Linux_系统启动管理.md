### 启动管理

```
启动流程：
	Upstart 启动服务 取代了 System V init
	1. 服务器加点，加载BIOS信息，BIOS进行系统检测，依照BIOS设定，找到第一个可以启动的设备(硬盘)
	2. 读取第一个启动设备的MBR(主引导记录)，加载MBR中的Boot Loader(启动引导程序，最常见为GRUB)
	3. 依照Boot Loader的设置加载内核，内核再进行一遍系统检测，系统一般会采用内核检测硬件的信息，而不一定采用BIOS的自检信息。内核再检测硬件的同时，还会通过加载动态模板的形式加载硬件的驱动
	4. 内核启动系统的第一进程，也就是 /sbin/init
	5. 由 /sbin/init 进程调用 /etc/init/rcS.conf 配置文件，通过这个配置调用/etc/rc.d/rc.sysint 配置文件。 而/etc/rc.d/rc.sysinit 配置文件是用来进行系统初始化的，主要用于配置计算机的初始化环境
	6. 通过/etc/init/rcS.conf 配置文件调用 /etc/inittab 配置文件。 通过 /etc/inittab 配置文件来确定系统的默认运行级别
	7. 确定默认运行级别后，调用/etc/init/rc.conf 配置文件
	8. 通过/etc/init/rc.conf 配置文件调用并执行 /etc/rc.d/rc 脚本，并传入运行级别参数
	9. /etc/rc.d/rc 确定传入的运行级别，然后运行相应的运行级别目录 /etc/rc[0-6].d/ 中的脚本
	10. /etc/rc[0-6].d/ 目录中的脚本依据设定好的优先级一次启动和关闭
	11. 最后执行/etc/rc.d/rc.local 中的程序
	12. 如果是字符界面启动，就可以看到登陆界面，如是图形界面启动，则调用相应的X Window 接口
	归纳：BIOS自检 -> 启动GRUB -> 加载内核 -> 执行第一个进程 -> 配置系统初始环境 

BIOS 开机自检
	通电后，进入BIOS： Basic Input/Ouput System 基本输入/输出系统
	BIOS初始化的工作：
		1. 检查硬件和外围设备， CPU、内存、风扇灯。 自建过程称为 POST(Power On Self Test)
		2. 对硬件进行初始化，规定当前启动设备的先后顺序，选择由哪个设备来开机
		3. 选择好开机设备后，会从该设备的MBR(主引导目录)读取Boot Loader(启动引导程序)并执行，启动引导程序用于引导操作系统启动，Linux系统默认使用GRUB
	当MBR被加载到RAM之后，BIOS将控制权交给RAM，进入系统第二阶段
	[MBR](http://c.biancheng.net/uploads/allimg/181022/2-1Q0221G321149.jpg)
	启动引导程序的作用：
		BIOS作用是自检，从MBR读取启动引导程序。
			启动引导程序作用：
				1. 加载操操作系统的内核
				2. 可选择的系统菜单，如双系统
				3. 调用其他的启动引导程序，多系统启动的关键
			[启动引导程序](http://c.biancheng.net/uploads/allimg/181022/2-1Q0221G60U34.jpg)
	
Linux内核(内核模块)的加载过程
	内存存放位置： /boot 的启动目录中
	GRUB加载内核后，内核进行二次系统自检，内核替代BIOS接管Linux启动。
	内核完成后，采用动态方式加载每个硬件的模块，模块为硬件的驱动。
	initramfe虚拟文件系统
		通过initramfs虚拟文件系统再内存中模拟处一个根目录，然后加载SCSI等硬件驱动，可加载真正的跟目录，之后调用Linux的第一个进程/sbin/init
		优点：
			initramfs随着数据的增减自动增减容量
			再initramfas和页面缓存之间没有重复数据
			initramfs重复利用Linux caching的代码，没有增加内核尺寸
			不需要额外的文件系统驱动
			[](http://c.biancheng.net/uploads/allimg/181023/2-1Q023093PD60.jpg)
			
Linux /sbin/init 初始化系统环境
	内核加载完，完成硬件检测与驱动程序加载后，内核主动呼叫第一个进程/sbin/init, 此配置主要功能准备软件执行的环境：主机名、网络设定、语言、文件系统格式及其他服务的启动
	/etc/rc.d/rc.sysinit 配置文件的工作：
		获得网络环境和主机类型
		测试设备：侦测系统上是否有usb设备，如有主动加载usb驱动程序，并挂载usb文件系统
		开机启动画面Plymouth
		判断是否启用SELinux
		显示开机过程的欢迎画面
		初始化硬件
		用户自定义模块的加载
		配置内核的参数
		设置主机名
		同步存储器
		设备映射器及相关的初始化
		初始化软件磁盘阵列(RAID)
		初始化LVM的文件系统功能
		检验磁盘文件系统(fsck)
		设置磁盘配置(quota)
		重新以可读写模式挂载系统磁盘
		更新quota(非必要)
		启动系统虚拟随机数生成器
		配置机器(非必要)
		清除开机过程中的临时文件
		创建ICE目录
		启动交换分区(swap)
		将开机信息写入 /var/log/dmesg 文件中

Linux /etc/inittab：设置(修改)系统默认运行级别
	Linux有7个级别：
		0 ：关机
		1 ：单用户模式，类Windows安全模式，系统修复
		2 ：不完全的命令行模式，不含NFS服务
		3 ：完全的命令行模式，标准字符界面
		4 ：系统保留
		5 ：图形模式
		6 ：重新启动
	runlevel：查看系统的运行级别
	系统默认运行级别：/etc/inittab 配置文件功能：确定系统的默认运行级别，即开机进入哪个运行级别
	
Linux /etc/rc.d/rc.local 配置文件
	在 /etc/rc[06].d/ 目录中的程序启动后，系统启动完成。
	[启动流程](http://c.biancheng.net/uploads/allimg/181023/2-1Q02310563a22.jpg)

Linux 启动引导程序(GRUB)加载内核
	GRUB加载内核的过程	
		加载操作系统的内核
		可选择的操作系统菜单
		调用其他启动引导程序，实现多系统引导
			1. 执行GRUB主引导
				1.5 识别不同的文件系统
			2. 加载GRUB的配置文件

Linux /boot/grub/ 目录分
	1. 第一阶段启动引导的主程序
	2. 第二阶段为主程序加载配置文件，包括环境参数文件

GRUB磁盘分区表示法
	ha：硬盘
	第一个0：系统查找到的第一块硬盘，第二块为1|2？
	第二个0：硬盘的第一个分区
		硬盘		分区		设备文件名		GRUB设备文件名
	第一块SCSI硬盘
	[内容太多](http://c.biancheng.net/view/1030.html)

/boot/grub/grub.conf(GRUB配置文件)内容
	[内容太多](http://c.biancheng.net/view/1032.html)

多系统并存的GRUB配置文件内容分析
	[多系统](http://c.biancheng.net/view/1033.html)

GRUB手动安装方法
	手动安装GRUB的情况
		1. 不使用GRUB作为引导程序，而想要GRUB作为引导程序
		2. MBR中的引导程序被覆盖，如安装linux后安windows，引导被覆盖
	步骤：
		1. 使用grul-install 命令 在启动分区安装GRUB相关文件
		2. 修改GRUB的配置文件
		3. 安装GRUB到/dev/sdb1分区的启动扇区中

Linux GRUB加密方法
	启动选项按 e 进入编辑模式，通过命令grub-md5-crypt
		模式：
			1. 给每个启动菜单加密
			2. 给GRUB菜单整体加密
	
字符界面调整分比率
	[文章](http://c.biancheng.net/view/1037.html)

Linux内核模块管理(查看、添加、删除)
	模块：动态可加载内核模块，有独立功能的程序，可被单独编译，但不能独立运行
	安装模块的方法：
		1. 在编译内核时，手工调整内核模块功能，加入所需的模块
		2. 下载厂商发布的新硬件的驱动模块，或下载驱动程序，在编译
	内核模块保存位置与模块保存文件
		内核模块保存：		
			/lib/modules/内核版本/kernel/目录中
				depmod 选项
					-a：扫描所有模块
					-A: 扫描新模块，有新模块，更新moudles.dep 文件
					-n：扫描结果不写入modules.dep 文件，直接输出到屏幕
		内核模块的查看：
			lsmod 命令指定结果：
				Module：模块名
				Size：模块大小
				Used by：模块是否被其他模块调用
		内核模块的添加与删除：
			modprobe 选项 模块名
				-l：列出所有模块的文件名，依赖modules.dep文件
				-f：强制加载模块
				-r：删除模块

Linux NTFS文件系统安装
	方法有三：
		一. 重新编译内核
		二. 下载编译内核
		三. 第三方插件 NTFS-3G
			二. 
				1.下载内核
				2.解压内核
				3.生成内核编译所需的.config文件
				4.编译模块
				5.模块安装
			三：
				1.下载NTFS-3G插件
				2.安装NTFS-3G插件
				
Linux单用户模块(修改密码、运行级别)方法
	如何进入单用户模式：
		开机、e 进入GRUB
		kernel、e 进入编辑界面，然后输入 空格 single，代表启动单用户模式
	单用户模式常见错误修复：
		root密码:
			单用户模式、	passwd root
		修改系统默认运行级别：
			直接修改配置文件/etc/inittab. 系统的默认运行级别只能使用3或5

光盘修复模式使用方法：
	[光盘修复](http://c.biancheng.net/view/1042.html)

Linux系统安全性分析
	[密码安全](http://c.biancheng.net/uploads/allimg/181024/2-1Q024111633X7.jpg)

```

