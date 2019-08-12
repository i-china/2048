git config --globale 

git rm -r xxx
git commit -m 'delete file'
git push 


git 出现 fatal: refusing to merge unrelated histories ERROR
1. git pull origin xxx 
   git add .  git commit -m 'xxx'		git push origin xxx
2. git pull origin xxx --allow-unrelated-histories 
	git push xxii master:xxx // xxii 是别名   master 是本地的branch名字， xxx是远端要推送的branch 分支 名字
本地必须要先 add， commit 完才能推上去
git push origin xxx --allow-unrelated-histories

