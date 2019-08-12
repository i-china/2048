###  注册一个Github账号


###	 配置公私钥
	git config --global user.name 'Hale'
	git config --gloable user.email 'aspire_8@163.com'
	ssh-kengen -t rsa -b 4096 -C 'aspire_8@163.com' 
	一路回车
	cat ~/.ssh/id_ras.pub

###  添加公钥到Github SSH and GPG keys 
		

###	 在Github 创建个人仓库
		

###	 把本地仓库同步到Github
	git remote add xxx git@github.com:aspire_8/xxx.git		// 新增远程Github仓库
	git remote remove xxx				//	删除远程Github仓库
	git remote rename oldName newName				// 更改远程Github仓库的名称
	git push xxx -all		// 提交本地所有分支到远端

####  一般出错的情况
	在推送前，需要先 拉取 远程仓库到本地
	git pull		//	拉取远程到本地并且合并，等同于 git fetch + git merge 
	git fetch		// 仅仅把远端的拉到本地
	git merge 远端分支/本地分支(master)		// 合并分支

####  把不相干的两个分支合并
	git merge --allow-unrelater-histories 远端仓库/本地仓库	



