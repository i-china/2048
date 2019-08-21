## 常用命令： 
	git log 
	git status

### Git仓库
两种场景：
1. 把已有的项目代码纳入Git管理
cd 项目代码所在的文件夹
git init

2. 新建的项目直接用Git管理
cd 某个文件夹
git init your_project    # 会在当前路径下创建和项目名称同名的文件夹
cd your_project

### 往仓库添加文件
工作目录	 git add files | git add -u : -u 添加所有		
暂存区：	 git commit	-m "xxx"	: 填写提交的信息
版本历史	 git log 
		git log --oneline
		git log -n|-n2  --oneline

		git branch -v :		查看分支
		git branch -av:	
		git checkout -b xxx : 创建xxx的分支
		

### 文件重命名
1 . 
	git add xxx.xx
	git rm xxx	

2. git mv xxx.xx xxx   
	result: ''' renamed: xxx.xx -> xxx '''

### 在线查看帮助文档
	git help --web xxx

### git 目录
	HEAD: 显示正在工作的分支
	config: 显示配置文件信息
	refs > heads(分支) |  tags(标签)
### Git: commit  |  tree	|	blob
	git cat-file -p commit_id	# 看commit的详细内容
	git cat-file -p tree commit_id # 看tree树下面的详细信息
	find .git/objects -type f 

### Git 分离头指针
	在没有绑定分支的情况下，git status 会显示 HEAD， 后面需要 git branch xxx head_id

### 独自使用Git的场景

### install 
yum install git
apt install git
brew install git

### 配置user信息: user.name		user.email
git config --global user.name 'your_name'
git config --global user.email 'your_email@domain.com'

#### Config 的三个作用域:
缺省等同于 local
git config --local			对某个仓库有效
git config --global			对当前用户所有仓库有效
git config --system			对系统所有登陆的用户有效

#### 现实config的配置，加 --list
git config --list --local
git config --list --global 
git config --list --system

### 建Git仓库

两种场景：
#### 1. 把已有的项目代码纳入Git管理
cd 项目代码所在的文件夹
git init 

#### 2. 新建的项目直接用Git管理
cd 某个文件夹
git init your_project    # 会在当前路径下创建和项目名称同名的文件夹
cd your_project


### Git 分离头指针
    在没有绑定分支的情况下，git status 会显示 HEAD， 后面需要 git branch xxx head_id
	如果没有保存，会被当作垃圾清理掉

### HEAD  branch
	git checkout -b xxx yyy			// 基于yyy 创建 xxx 分支
	HEAD 可脱离分支，独立存在

git diff	// 比较两个commit 的不同	git diff HEAD HEAD^ | HEAD～n

