### 删除不需要的分支
git branch -av
git commit -am"add and commit"
git branch -d|-D xxx :		删除分支 xxx 为分支名，可用-D 删除

### 修改最新的commit信息
	git commit --amend		// 修改第一行的内容即可改变commit 信息

### 修改老旧的commit信息
	先用 git log -n  查找到最近n条的commit信息
	git rebase -i xxx  // xxx为要被改变的commit 的父基（下一条）
	git log -n3 --graph			//	查看最近三次的父子关系

### 把多个连续的commit合并为一个
	git rebase -i xxx		// xxx 为被要修改commit的父基，然后把第一个下面的pick改为 s,然后wq! ，在新弹出的编辑界面中，添加新的commit信息。在接着wq！
	git log --graph   查看最新的父子关系
	
### 把间隔的几个commit整理为一个
	git rebase -i xxx		//	被修改的commit的最后的那个commit的分支id
	在弹出的编辑界面添加 pick 最后commit的ID message，然后把要合并的commit ID的pick改为 s，多余的commit 删除，然后wq!，然后在弹出的界面添加新曾的commit信息

### 比较暂存区和HEAD所含文件的差异
	git diff --cached				// 暂存区和HEAD的差异

### 比较工作区和暂存区所含文件的差异
	git diff	//	比较工作区和暂存区所有文件的差异
	git diff -- readme.md	// 只比较readme.md 文件的差异

###	让暂存区恢复成和HEAD的一样
	git reset HEAD 

### 把工作区的文件恢复为和暂存区一样
	git status					// 查看现在的状态
	git diff --cached			//	比较暂存区和HEAD的差异
	git diff -- xxx.xx			// xxx.xx 为要恢复的文件
	git log						//	查看最近的日志

### 取消暂存区部分文件的更改
	git reset HEAD -- xxx/xxx.xx	//	xxx为要取消恢复的文件
	git reset HEAD -- xxx/xx.xx xxx.xx		// 可以取消恢复多个文件，空格分开

###	消除最近的几次提交
	git reset --hard commitID		//	恢复到指定的commit分支， 很危险，会删除掉指定commit最新的提交文件和信息

### 查看不同提交的指定文件的差异
	git diff 分支1 分支2 -- 文件		//	比较不同分支的差异
	git diff 分支指针1 分支指针2 -- 文件	 // 用分支比较文件的差异

### 正确删除文件的方法
	git rm xxx			//	删除xxx 文件

### 开发中临时加塞了紧急任务的处理方法
	git stash			// 把现在做的工作任务存放到不影响接下来要做的工作环境中去
	git stash list		//	查看所有的stash 任务的列表
	git status			
	git stash apply		//	弹出最新的stash， 不保留stash 的任务
	git stash pop		//	弹出最新的stash 工作，存放起来的任务还在

###	指定不需要Git管理的文件
	.gitignore			// 文件中添加不需要被提交的文件类型

### 将Git仓库备份到本地
	git clone --bare	// 不在工作区的仓库
	哑协议： git clone --bare 本地仓库.git	新建仓库name.git 



