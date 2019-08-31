```
 @Author : Hale Lv
 @Created Time : 2019-08-31 19:27:26
 @Description : 
```
## Git 

###	Git 简介
	最先进的分布式版本控制系统
	
	安装 Git
		Linux： 
			Centos: yum install -y git
			Ununtu: apt install -y git
	配置：	
		git config --global user.name 'Hale'
		git config --global user.email 'Aspire_8@163.com'

	创建版本库
		创建仓库文件夹： mkdir Git		cd Git
		初始化仓库：git init	// 初始化仓库，把这个目录变成Git可管理的仓库
		添加文件到仓库： git add xxx.xx
		编写提交信息： git commit -m 'xxxxx'
	
### 版本
		版本回退：
			查看仓库当前的状态：git status 
			比较文件修改的不同：git diff xxx.xx
		查看历史记录： 
			git log
			git log --pretty=oneline  // 简化输出的日子信息
		回退到上一个版本：
			git reset --hard HEAD^|Commit_ID
		Git命令历史：
			git reflog
	
		工作区和暂存区
			工作区：

		管理修改
			如新建一个文件：readme.txt
			git add readme.txt
			vim readme.txt 修改readme.txt 文件
			git commit -m 'add readme.txt'
			git status 
			比较工作和版本库文件的区别：
				git diff HEAD --readme.txt 
		
		撤销修改
			git status 
			把readme.txt在工作去的修改全部撤销
				git checkout -- file
					git checkout -- readme.txt
			
			git add readme.txt
			git status
			把暂存区的修改撤销掉，从新放回工作区：
				git reset HEAD readme.txt
			git status 
			丢弃工作区的修改：
				git checkout -- readme.txt

		删除文件
			git add readme.txt
			git commit -m 'add readme.txt'
			rm readme.txt 
			git status
			git rm readme.txt
			git commit -m 'remove readme.txt'
			
			把误删的文件回复到最新版本:
				git checkout -- readme.txt

### 远程仓库
		ssh-keygen -t rsa -C 'aspire_8@163.com'	
		cat ~/.ssh/id_ras.pub
		复制公钥到github SSH-KEY

		添加远程库
			git remote add origin git@github.com:i-china/2048.git
			git remote add origin git@github.com:i-china/1024.git
		推送本地库所有内容到远程库
			git push -u origin master			// 把当前分支master推送到远程
			git push origin master
			git push 

		从远程库克隆
			git clone git@github.com:i-china/4096.git
		
### 分支管理
		创建与合并分支
			git checkout -b dev					// 创建dev分支，并切换到dev分支
				=	git branch dev	
				=+	git ckekout dev 
			查看当前分支
				git branch 
			git checkout master
		把dev分支的工作成果合并到master分支：
			git merge dev
		删除分支
			git branch -d dev

		Switch
			创建并切换到新的dev分支：
				git switch -c dev
			直接切换到已有master分支：
				git switch master

		解决冲突
			创建新的分支 dev
				git checkout -b new
					编写readme.txt内容
				git add readme.txt
			切换到master分支
				git checkout master
					编写readme.txt内容
				git add readme.txt
			把各自修改合并起来
				git merge dev
				此时会报冲突
				git status 
				查看readme.txt 文件内容
					Git 用 <<<<< ===== >>>>> 标记不同分支的内容，修改保存即可
					git add readme.txt
					git log
				删除dev分支
					git branch -d dev
				查看分支合并图
					git log --graph

		分支管理策略
			git checkout -b dev
			git add readme.txt
			git checkout master
			git merge --no-off -m 'merge with no-off' dev 
			git log

		Bug 分支
			git status
			git stash 
			git checkout master
			git checkout -b issue-dev
			git add readme.txt
			git checkout master
			git merge --no-off -m 'merged bug fix dev' issue-dev
			git checkout dev
			git status 
			git stash list 
			git stash apply | git stash pop
			git stash list
			复制一个特定的提交到当前分支
				git branch
				git cherry-pick commit_id
				
		Feature 分支
			git checkout -b work
			git add readme.txt
			git commit -m 'add readme.txt'
			git checkout dev
			删除work 分支
				git branch -d work 
			强行删除
				git branch -D work
			
		多人协作
			git remote 
			git remote -v 
			git push origin master
			git push origin dev
		
			抓取分支
				git clone git@github.com:i-china/2048.git
			git branch 
			git checkout -b dev origin/dev
			git add readme.txt
			git push origin dev
			git pul 
			git branch --set-upstream-to=origin/dev dev
			git pull 
			git commit -m 'fix dev readme.txt'
			git push origin dev 

		Rebase
			git log --graph --pretty=oneline --abbrev-commit
			git push origin master
			git pull 
			git staus 
			git log --graph --pretty=oneline --abbrev-commit
			git rebase
			git log --graph --pretty=oneline --abbrev-commit
			git push origin master
			git log --graph --pretty=oneline --abbrev-commit

	标签管理
		创建标签：
			git branch 
			git checkout master
			git tar v1.0
			git tag 
			git log --pretty=oneline --abbrev-commit
			git tag v0.9 <commit_id>
			git tag 
			git show v0.9
			git tag -a v1.0 -m 'version 1.0 released' <commit_id>
			git show v1.0
			
		操作标签
			删除标签：
				git tag -d v1.0 
			git push origin v1.0 
			git push origin --tags 
			删除本地标签：
				git tag -d v0.9
			删除一个远程标签
				git push origin :refs/tags/v0.9

### 使用码云
		git remote add origin git@gitee.com:aspire_8/2048.git
		git remote -v
		git remote rm origin
		git remote add github git@github.com:i-china/2048.git
		git remote -v
		git remote rm origin 
		git remote add gitee git@gitee.com:aspire_8/4096.git
		git remote -v
		git push origin master 
		git push gitee master

### 自定义Git
		git config --global color.ui true

		忽略特殊文件
			.gitignore
				*.xx
			git add remade.xx
			git add -f readme.xx
			git check-ignore -v readme.xx
	
		配置别名
			git config --global alias.st status
			git config --global alias.ci commit
			git config --global alias.br branch
			git config --global alias.unstage 'reset HEAD'
			git config --global alias.last 'log-l'
			把配置别名放在一个文件中，方便管理
				cat ~/.git/config
				vim ~/.git/config
					[alias]
						last = log -1
						co = checkout
						ci = commit
						br = branch 
						st = status
					[user] 
						name = Hale
						email = Aspire_8@163.com

	搭建Git服务器
		apt install git
		adduser git
		收集所有需要登录的用户的公钥，就是他们自己的id_rsa.pub文件，把所有公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个。
		git init --bare git.git 
		chown -R git:git git.git
		git clone git@server:/srv/git.git
		
	[Git Cheat Sheet](https://gitee.com/liaoxuefeng/learn-java/raw/master/teach/git-cheatsheet.pdf)



