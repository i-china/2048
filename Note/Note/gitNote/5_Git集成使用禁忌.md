### 禁止向集成分支执行push -f 操作
	git push -f 

	示例:
		git log --oneline				// 查看历史日志
		git log --pretty=oneline		// 输出信息简化
		git reflog						// 记录每一次命令
		git reset --hard commitID		// 在本地使用reset 恢复到 任意一个commit的历史，如果使用 -f 提交的话，远程仓库所有被提交的commit之前的改动都会被删除掉，很危险！！！

		
###	禁止向集成分支执行变更历史的操作
	


再本地修改后，拉取的情况下， 需要先把本地的修改暂存或者 清除掉 
	git clean -y -fx
		
