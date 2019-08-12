### 本地模仿两个用户
	首先配置不同仓库的用户信息
		全局的
			git config --global user.name 'hale'
			git config --global user.email 'aspire_8@163.com'
		局部的：
			git config --add --local user.name 'local'
			git config --add --local user.email 'mr_hale@163.com'

###	不同人修改了不同文件的处理方案
	local 用户
		git checkout -b xxx/xxx	 xxxx/xxxx			//	基于xxxx/xxxx  本地新建分支 xxx/xxx 
		git push 
	global 用户
		git branch -av
		git fetch xxx			// 拉取远程分支到本地，分支名为 xxx
		git checkout -b xxx/xxx xxxx/xxxx	//	基于 xxxx/xxxx  创建本地分支 xxx/xxx

###	不同人修改了同文件的不同区域的处理方案
		git push 

###	不同人修改了同文件的同一区域的处理方案
		global: git pull	vim xxx.xx		git push 
		local : git pull	vim xxx.xx		git push 
		会出错，local没办法提交，解决方案
		vim xxx.xx		//	把修改的同一地方，删除其中一个人的修改，删除git的提示信息
		git status		->		git commit -am '解决冲突'  ->  git push

###	同时变更了文件名和文件内容的处理方案
		global 在更改同一文件名和内容之后
		local  在本地修改文件内容， git pull 的时候，git会弹出界面提示修改的信息，同时也会在被更改文件中，添加local修改的内容

###	把同一文件改成不同文件名的处理方案
		global: 修改xxx.xx 为 xxxa.xx，local:  修改  xxx.xx 为 xxb.xx
		global: git push		local: git pull , git rm xxx.xx, git rm xxa.xx, git add xxb.xx, git commit -m 'delete xxx.xx xxa.xx'	git push
		



