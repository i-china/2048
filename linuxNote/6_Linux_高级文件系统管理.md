### 高级文件系统管理
	磁盘配额、 LVM(逻辑卷管理)、 RAID(磁盘阵列)
		磁盘配额：限制普通用户在分区中使用的容量和文件个数
		LVM： 在不停机和不损失数据的情况下修改分区带线啊哦
		RAID：有多块硬盘或分区组成，拥有数据冗余功能，在某块硬盘或分区损坏时，硬盘或分区保存的数据不丢失


磁盘配额
	Linux系统中限制特定的普通用户或用户组在指定的分区上占用的磁盘空间或文件个数
	满足磁盘配额的条件：
		1. 内核支持				grep CONFIG_QUOTA /boot/conrrfig-2...el6.i686
		2. 安装Quota工具		rpm -qa | grep quota
		3. 支持磁盘配额的分区必须开启磁盘配额功能
	常见概念
		用户配额和组配额
		磁盘容量限制和文件个数限制
		软限制和硬限制
		宽限时间
	磁盘配额启动的前期准备(设置挂载参数usrquota和grpquota)
		添加方式：
			1. 手动添加挂载参数：
				mount -o remout,usrquota,grpquota /home
				mount | grep home
			2. 修改/etc/fstab文件。将挂载参数写入配置中
				vi /etc/fstab
					LABEL = /home	/home   ext3   defaults.usrquota,grpquota  1  2
				umount /home
				mount -a
				mount | grep home

quotacheck：扫描文件系统并建立Quota记录文件
	quotacheck [-avugfM] 文件系统
		-a：扫描所有在/etc/mtab 中含有quota支持的filesystem，此参数后边的文件系统可不写
		-u：针对使用者扫描文件与目录的使用情况，会创建 aquota.user
		-g：针对群组扫描文件与目录的使用情况，会创建aquota.group
		-v：显示扫描的详细过程
		-f：强制扫描文件系统，并写入新的quota记录文件
		-M：强制以读写的方式扫描文件系统，特殊情况下使用

quotaon：开始磁盘配额限制
	quotaon [-avug]
	quotaon [-vug] 文件系统名称
		-a：根据/etc/mtab 文件中对文件系统的配置，启动相关的Quota服务
		-u：针对用户启动Quota
		-g：针对群组启动Quota
		-v：显示启动服务过程的详细信息

quotaoff：关闭磁盘配额限制
	quotaoff [-avug]
	quotaoff [-vug] 文件系统名称
		-a：根据/etc/mtab 文件，关闭已启动的Quota服务，如不使用-a选项，则后面需要明确协商特定的文件系统名称
		-u：关闭针对用户启动的Quota服务
		-g：关系针对群组启动的Quota服务
		-v：显示服务过程的详细信息
		
edquota：修改用户(群组)的磁盘配额
	edquota [-u用户名] [-g群组名]
	edquota -t 
	edquota -p 源用户名 -u 新用户名
		-u 用户名：进入配额的Vi编辑界面，修改针对用户的配置值
		-g 群组名：修改针对群组的配置值
		-t：	   修改配额参数中的宽限时间
		-p：	   将源用户(或群组)的磁盘配额设置，复制给其他用户(或群组)
	edquota 命令配额限制信息
		文件系统 filesystem：针对哪个文件系统或分区
		磁盘容量 blocks： quota自己算的，单位为Kbytes，不要手动修改
		磁盘容量的软限制 soft： 超过此限制值，登陆时会收到警告信息
		磁盘容量的硬显示 hard： 要求用户使用的磁盘空间不超此限制值，单位为KB
		文件数量 inodes：  当文件数量超过此值，会发出警告
		文件数量的硬限制 hard： 用户拥有的文件数量不超此值
		
setquota：非交互式设置磁盘配额
	setquota -u 用户名 容量软限制 容量硬限制 个数软限制 个数硬限制 分区名
	
quota和repquota查询磁盘配额方法
	quota 查询用户或用户组的配额
		quota 选项 用户名或组名
			-u 用户名： 查询用户配额
			-g 组名 ：	查询组配额
			-v： 显示详细信息
			-s： 以习惯单位显示容量大小 如 M、G
	repquota 查询整个分区的配额情况
		repquota 选项  分区名
			-a： 依据/etc/mtab 文件查询配额，如不加-a，就得加分区名
			-u： 查询用户配额
			-g： 查询组配额
			-v： 显示详细信息
			-s： 以易读单位显示容量大小

### LVM逻辑卷管理机制(硬盘分区管理机制)
		LVM：Logical Volume Manager，逻辑卷管理，Linux下对硬盘分区的一种管理机制
			物理卷(Physical Volume, PV)：真正的物理硬盘或分区
			卷组(Volume Group, VG)：将多个物理卷组成了卷组，把卷组想象为一块逻辑硬盘
			逻辑卷(Logical Volume, LV)：逻辑卷可被格式化和写入数据，可想象为分区
			物理扩展(Physical Extend,PE)：PE保存数据的最小单元，默认是4MB
		建立LVM的步骤：
			1. 把物理硬盘分成分区
			2. 把物理分区建立为物理卷PV
			3. 把物理卷整合为卷组VG
			4. 把卷组划分为逻辑卷LV
		
PV物理卷：创建、查看、删除
	1. 建立所需的物理分区，方式使用fdisk交互命令
	建立物理卷；
		pvcreate 设备文件名
	查看物理卷：
		pvscan
		pvdisplay
	删除物理卷：
		pvremove /dev/sdb7

VG卷组：创建、激活、查看、扩容、减小、删除
	建立卷组：
		vgcreate [-s PE 大小] 卷组名 物理卷名
	激活卷组：
		激活：vgchange -a y 卷组名
		停用：vgchange -a n 卷组名
	查看卷组：
		vgscan ： 查看系统中是否有卷组
		vgdisplay： 查看卷组的详细状态
	增加卷组容量：
		vgextend scvg /dev/sdb7
	减少卷组容量：
		vgreduce  scvg /dev/sdb7
	删除卷组：
		vgremove scvg 

LV逻辑卷：创建、查看、调整大小、删除
	建立逻辑卷：
		lvcreate 选项 -n 逻辑卷名 卷组名
			-L：容量，逻辑大小，单位为MB、GB、TB
			-l：个数，按照PE个数指定逻辑大小
			-n：逻辑卷名
	查看逻辑卷：
		lvscan		： 查看系统中是否拥有逻辑卷
		lvdisplay	： 查看逻辑卷的详细信息
	调整逻辑卷大小：
		lvresie 选项 逻辑卷的设备文件名
			-L: 容量 
			-l: 个数
	删除逻辑卷：
		lvremove 逻辑卷的设备文件名
LVM(逻辑卷管理) 删除
		

RAID(磁盘列阵)

图形界面配置RAID

mdadm配置RAID











