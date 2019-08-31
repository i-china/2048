安装Nodejs:   install node
安装Npm:	install npm
安装Cnpm:  npm install -g cnpm --registry=https://registry.npm.taobao.org
安装Hexo:	cnpm install -g hexo-cli
本地初始化项目Blog:  hexo init
在Github新建仓库Github.io:	githubName.github.io
安装hexo—git插件Blog+Git:	cnpm install --save hexo-deployer-git	
本地配置git博客Config:	vim _config.yml 
	# Deployment	// 注意： 每个配置冒号后面都得加空格 
	deploy:		
	type: git	
	repo: https://github.com/i-china/i-china.github.io.git
	branch: master

推送到远程仓库：	hexo -d 
	接着输入Github 账号和密码


修改Hexo主题:    git clone https://github.com/litten/hexo-theme-yilia.git theme/yilia
	克隆主题的时候可以指定下载的位置
	修改__config.yml 使主题生效： theme: yilia

清理缓存：hexo clean
推送远程：hexo deployer


新建文章： hexo new "My new Post"
修改__ _config.yml 
	修改 Schemes 为 Gemini



