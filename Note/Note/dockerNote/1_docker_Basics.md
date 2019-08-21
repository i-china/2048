### Docker 基础

install 

windwos: Control Panel  -> open: Hyper-V 和  容器
[Docker.exe](https://www.docker.com/products/docker-desktop)
Mac os : 
[Docker.dmg](https://www.docker.com/products/docker-desktop)
Linux  :
	wget -qO- https://get.docker.com/ | sh
	usermod -aG docker your-user
Windows Server :
	Install-Module DockerProvider -Force
	Install-Package Docker -ProviderName DockerProvider -Force

Update Docker 
	apt update
	apt remove docker docker-engine docker-ce docker.io -y
	wget -qO- https://get.docker.com/ | sh
	systemctl enable docker				// 设置开机启动
	systemctl is-enabled docker			//	检测是否开机启动

Docker Storage Driver: 存储驱动
	/etc/docker/daemon.json		:	{"storage-driver":"overlay2"}
	docker system info			//	检查docker当前的存储驱动类型

运维角度看Docker
	docker version
	镜像：docker image ls 
	容器：docker container run -it ubuntu:latest /bin/bash	// -it 交互模式
			ps -ef				//	查看全部进程
			docker container ls		// 系统内全部处于运行状态的容器
			docker container exec		// 将shell连接到一个运行中的容器终端
			docker container exec -it <options> <container-name or container-id> <command/app>
			Ctrl + PQ	// 退出容器
			docker container stop <container-name or container-id>		// 停止容器
			docker container rm <container-name or container-id>		// 删除容器
			docker container ls -a		//	列出所有容器 包括已删除的
			
开发角度看Docker 
	clone web应用代码	cd xxx  ->  ls -l -> cat Dockfile 
			-> docker image build	// 根据Dockerfile中的指令来创建新的镜像
			-> docker image build -t xxx:latet .

Docker 引擎 engine
	[总体逻辑](http://c.biancheng.net/uploads/allimg/190416/4-1Z416140U0537.gif)
	组成： Docker Client、 Docker daemon、 Contained 、runc 
	[引擎架构](http://c.biancheng.net/uploads/allimg/190416/4-1Z41614102M63.gif)
启动一个新的容器
	docker container run --name ctr1 -it alpine:latest sh
	[启动过程](http://c.biancheng.net/uploads/allimg/190416/4-1Z4161413112O.gif)
daemon 作用
	镜像管理、镜像构建、REST API、身份验证、安全、核心网络以及编排

Docker镜像
	docker container run
	docker service create		//	从某个镜像启动一个或多个容器
拉取镜像
	docker image pull xxx:latest		// xxx 为镜像名 latest 为版本
	docker image ls						// 检查docker主机本地仓库是否包含镜像
	镜像仓库服务 Image Registry 
		镜像命名和标签
			拉取镜像：docker image pull <repository>:<tag>	
						docker image pull ubuntu:latest		// 从官方ubuntu库拉取标签为latest的镜像
			拉取某组织的镜像: docker image pull microsoft/powershell:nanoserver
	为镜像打多个标签
		docker image pull -a nigelpoulton/tu-demo
	返回镜像列表内容
		docker image ls --filter dangling=true	//	返回没有标签的镜像(悬虚镜像)，显示为 <none>:<none>
	移除全部的悬虚镜像:	 docker image prune
	过滤器：	dangding: 返回悬虚镜像(true), 非悬虚镜像(false)
				before :	需要镜像名称或者id，返回在之前被创建的全部镜像
				since :		类似before，返回指定镜像之后创建的全部镜像
				label :		根据标注(label)的名称或者值，进行过滤 
		docker image ls --filter=reference="*.latest"
		docker image ls --format "{{.Size}}"	//	通过Go模板对输出内容格式化
		docker image ls --format "{{.Repository}}:{{.Tag}}:{{.Size}}"

搜索Docker Hub 
	docker search xxx			// xxx 为 仓库名称
	docker search xxx --filter "is-official=true"	// 返回官方镜像
	docker search xxx --filter "is-automated=true"	//	显示自动创建的仓库

镜像和分层
	Docker 镜像由一些 松耦合 的只读镜像层组成
	查看镜像分层： docker image inspect xxx:latest
	查看镜像的构建历史记录： docker history 
	[镜像层](http://c.biancheng.net/uploads/allimg/190416/4-1Z416164115364.gif)
	共享镜像层
		docker image pull -a xxx/xxx
	本地产看镜像摘要：	docker image ls --digests xxx
	在docker主机删除镜像：	docker image rm xxx:latest
	多层架构的镜像
		[Multi-architecture Image](http://c.biancheng.net/uploads/allimg/190416/4-1Z416164446156.gif)
	删除本地镜像： docker image rm	container-id
	获取本地全部镜像:  docker image ls -q 
	删除本地全部镜像:  docker image rm $(docker image ls -q) -f 

Docker 镜像常用命令
	docker image pull						//	下载镜像
	docker image pull xxx:xxx				//	下载指定镜像
	docker image ls							//	列出全部镜像
	docker image inspect					//	列出镜像层数数据和元数据
	docker image rm							//	删除镜像
	docker image rm xxx:xxx					//	删除指定镜像

Docker 容器
	docker container run					//	启动容器
	docker container run <image> <app>		// 指定启动所需的镜像及要运行的应用
	docker container run xxx:xxx sleep 10	// shell连接到容器 10s 的时间
	docker container stop					//	手动停止容器运行
	docker container start					//	再次启动该容器
	docker container rm						// 删除容器

容器和虚拟机
	[](http://c.biancheng.net/uploads/allimg/190417/4-1Z41G01336346.gif)

检擦Docker daemon
	docker version
		如果server 部分有错，需要 usermod -aG docker <user> 添加到本地docker 组
	检查docker daemon状态
		service docker status 
		systemctl is-active docker 

启动一个简单容器
	docker container run 
	docker container run <options> <im- age>:<tag> <app>
	docekr 默认非TLS网络端口为 2375 ， TLS端口为 2376

容器进程：	ps -ef 

查看正在运行的容器列表
	docker container ls 

启动容器后，重新连接到Docker
	docker container exec -it <container-name or container-id> bash 

停止容器
	docker container stop <container-id or container-name>

删除容器
	docker container rm <container-id>

容器生命周期
	docker container run --name percy -it xxx:xxx /bin/bash
	Ctrl - PQ 组合键退出当前容器

优雅地停止容器
	docker container stop				// 向容器内的PID 1进程发送 SIGTERM 信号，优雅结束10s时间

	没有预警停止容器
	docker container stop <container> -f
	docker container rm <container> -f			// -f 不会发送 SIGTERM，直接发出 SIGKILL 

利用重启策略进行容器的自我修复
	容器支持的重启策略： always  unless-stopped  on-failed 
		docker container run --name xxx -it --restart always xx sh
				exit	
		docker container ls 
	1. 创建两容器
		docker container run -d --name always --restart always alpine sleep 1d 
		docker container run -d --name unless-stopped --restart unless-stopped alpine sleep 1d 
		docker container ls 
	2. 停止两容器
		docker container stop always unless-stopped
		docker container ls
	3. 重启 Docker 
		systemctl restart docker
	4. 检查两状态
		docker container ls -a 
	结论：always 重启了，unless-stopped 没有重启

	
Web服务器示例
	docker container run -d --name webserver -p 80:8080 nigelpoulton/pluralsight -docker -ci				//	-d	后台模式	-p 80:8080 端口映射 将Docker主机的80端口映射到容器内的8080端口
	docker container stop	docker container pause		docker container start	docker container rm 

查看容器详情
	docker container inspect 
快速清理
	$()
	rm $(docker image ls -q)	|		($docker container ls -aq)
	docker container rm

Docker容器常用命令
	docker container run						//	启动新容器
	docker container ls							//	列出在运行(UP)， -a: 列出停止的(Exited)
	docker container exec						//	连接该容器 -it <container-name or container-id> bash 
	docker container stop						//	停止运行中的容器
	docker container start						//	重启停止(Exited)状态的容器 <container-id or contaienr -name>
	docker container rm							//	删除停止运行的容器
	docker container inspect					//	显示容器配置细节和运行时信息 <container-id or container-name>

Docker应用容器化(将应用程序部署到容器中)
	容器化：将应用整合到容器中并且运行起来的过程，能够简化应用的构建、部署和运行过程
	完整的应用容器化过程分为以下步骤
		1. 编写应用代码
		2. 创建一个Dockfile，包括应用的描述、依赖、及如何运行应用
		3. 对该Dockerfile 执行 docker image build 命令
		4. 等待Docker将应用程序构建到Docker镜像中
	[步骤](http://c.biancheng.net/uploads/allimg/190417/4-1Z41G51T3502.gif)

单体应用容器化
	步骤：
		1， 获取应用代码
		2.  分析 Dockfile
		3.  构建应用镜像
		4.  运行该应用
		5.  测试应用
		6.  容器应用化细节
		7.  生产环境中的多阶段构建
		8.  最佳实践

登录到Docker Hub
	docker login											// 登录到docker
	docker image push										// 推送到docker
	docker image tag web:latest xxx/web:latest				// 为镜像打标签
















### Dockerfile

docker image build			// 读取Dockerfile，并将应用程序容器化
Dockerfile 示例代码：	
	# Linux x64
	FROM xxx

	LABEL maintainer="mr_hale@163.com"
	
	# install Node and NPM 
	RUN apk and --update nodejs nodejs-npm

	# Copy app to /src
	COPY ./src

	WORKDIR /src
	
	# Install dependencies 
	RUN npm install 

	EXPOSE 8080

	ENTRYPOINT ["node","./app.js"]

解释：
	-t ： 为镜像打标签
	-f ： 指定Dockerfile 的路径和名称，指定位于任意路径下的任意名称的Dockerfile
	FROM ：用于指定要构建的镜像的基础镜像，通常是Dockerfile 中的第一条指令
	RUN ： 用于在镜像中执行命令，会创建新的镜像层，每个指令创建一个新的镜像层
	COPY ： 用于将文件作为一个新的层添加到镜像中，使用COPY指令将应用代码赋值到镜像中
	EXPOSE ： 记录应用所使用的网络端口
	ENTRYPOINT ： 指定镜像以容器方式启动后默认运行的程序
	LABEL ：
	ENV ：
	ONBUILD ：
	HEALTHCHECK ：
	CMD ：

### Dockers Compose
	与Docker Stack类似，在Docker节点上，以单引擎模式(Single-Engine Mode)进行多容器应用的部署和管理
	如：一个间的示例应用可能有4个服务组成
		1. Web前端
		2. 订单管理
		3. 品类管理
		4. 后台数据库
	Compose 用来部署和管理繁多的服务
使用：首先编写定义多容器(多服务)应用的YAML文件，然后由 docker-compose 命令处理，基于Docker引擎API完成应用的部署

安装：
	使用curl下载二进制文件，然后 chmod 修改权限
	检验： docker-compose --version
	用 pip 安装 Docker Compose 的 python 包

Docker Compose YML 配置文件及常用指令
	YAML 定义多服务的应用，是JSON的子集，可使用JSON定义
	默认使用文件名 docker-compose.yml, 也可使用-f参数指定具体文件
	示例：包含  web-fe 、 redis 的小型Flask应用
		能够对其访问者进行计数并将其保存到Redis的简单Web服务
		version: "1.0"
		services:
		web-fe:
		build:.
		command: python app.py
		ports:
		- taget: 5000
		published: 5000
		networks:
		- counter-net
		volumes:
		- type: volume
		source: counter-vol
		target: /code
		redis:
		image: "redis:alpine"
		networks:
		counter-net:

		networks:
		counter-net:

		volumes:
		counter-vol:
	
包含4个一级key： version、services、networks、volumes
		version: 指定版本
		services: 定义不同的应用服务，compose 会将每个服务部署到各自的容器中
		networks：指引docker创建新的网络，默认 创建 bridge 网络，也可以使用driver属性指定网络类型,允许独立的容器连接到该网络上
			networks:
			over-net:
			driver: overlay
			attachable: true
	volumes: 指定docker创建新的卷
	
	定义了两个Key：web-fe 、redis，因此Docker Compose部署两容器，一个包含web-fe，一个redis
	web-fe服务定义中，包含以下指令：
	1. build： 指定docker基于当前目录 (.) 下dockerfile来构建新景象，用于启动该服务的容器
	2. command： 指定docker在容器中执行名为 app.py 的Python脚本作主程序
	3. ports： 将容器内(-target)的5000端口映射到主机(published)的5000端口
	4. networks：是的docker将服务连接到指定的网络上
	5. volumes：将counter-vol卷(source:)挂载到容器内的 /code (target:)
	6. image： redis:alpine 是的docker基于redis:alpine 镜像启动一个独立的名为redis的人弄国企，镜像会从docker hub上拉取下来
	7. networks：配置redis容器连接到counter-net网络

Docker-Compose 部署应用
	在项目目录中，检查文件是否存在
	app.py:	应用程序代码 Flask应用
	docker-compose.yml: compose文件，定义了Docker如何部署应用
	Dockerfile:	定义了如何构建web-fe服务所使用的镜像
	requirements.txt: 列出了应用所依赖的python包

启动应用：
	docker-compose up &
	docker-compose -f prod-equus-bass.yml up		//	基于名为 prod... 的compose文件部署应用
	docker-compose up -d			// 没有-d 用 & 将终端窗口返回
	
	FROM python:3.4-alpine <<  基础镜像
	ADD ./code			   <<	将app复制到镜像中
	WORKDIR /code		   <<	设置工作目录
	RUN pip install -r requirements.txt   << 安装依赖
	CMD ["python","app.py"]  << 设置默认启动命令

若 .Services.redis 中指定了image: "redis:alpine"，会从docker hub拉取redis:alpine 镜像
	docker container ls
	docker network ls 
	docker volume ls

使用Docker-Compose 子命令
	docker-compose up -d			//	拉取和构建的镜像保存在系统中
	docker-compose ps				//	列出容器名称、command、状态、网络端口
	docker-compose top				//	列出各个服务(容器)内运行的进程
	docker-compose stop				//	停止应用，但不删除
	docker-compose rm				//	删除应用相关的容器和网络，但不删除卷和镜像
	docker-compose restart			//	重启应用
	docker-compose down				//	停止和关闭应用
	
	./code 
	[Dockerfile and Compose file](http://c.biancheng.net/uploads/allimg/190417/4-1Z41GJ242b5.gif)

	
### Docker Swarm
	集群管理工具，作用：把若干台Docker主句抽象为一个整体，通过一个入口统一管理各种Docker资源。 类似 Kubernetes，包含：企业级的Docker安全集群，微服务应用编排引擎
	默认内置： 分布式集群存储、加密网络、公用TLS、安全集群接入令牌、简化数字证书管理的PKI
	基于Docker引擎之上的独立产品
	一个Swarm由一个或多个Docker节点组成，通过可靠的网络相连。
	节点被配置为管理节点(Manager)和工作节点(Worker)， 管理节点负责集群控制面，进行诸如监控集群状态、分发任务至工作节点等操作。 工作节点接受来自管理节点的任务并执行
	[Swarm](http://c.biancheng.net/uploads/allimg/190418/4-1Z41Q045505Y.gif)
	
集群搭建：
	[Swarm](http://c.biancheng.net/uploads/allimg/190418/4-1Z41Q24Z2332.gif)
	每个节点装 Docker，并能够与Swarm的其他节点通信
	防火墙开放以下端口：
		2377/tcp:	用于客户端与Swarm进行安全通信
		7946/tcp 与 7946/udp: 用于控制面gossip分发	
		4789/udp: 用于基于VXLAN的覆盖网络

大体流程：初始化第一个管理节点 -> 加入额外的管理节点 -> 加入工作节点 -> 完成

初始化一个全新的Swarm：
	[Swarm](http://c.biancheng.net/uploads/allimg/190418/4-1Z41Q25041I0.gif)
	在单引擎模式下的Docker 主机执行 docker swarm init 切换到swarm模式
	接入额外的管理节点，并切换为Swarm模式
	docker swarm init --advertise-addr 10.0.0.1:2377 --listen-addr 10.0.0.1:2377
		docker swarm init	// 初始化并设置为第一个管理节点，开始swarm模式
		--advertise-addr	// 指定其他节点用来连接到当前管理节点的IP和端口，可选
		--listen-addr		// 用于承载Swarm流量的IP和端口
	docker node ls			// 列出Swarm 节点
	docker swarm join-token	// 获取添加新的工作节点和管理节点到Swarm的命令和Token
		docker swarm join-token worker
		docker swarm join-token manager 
	docker swarm join --token SWMTKN-1-0uahebax...ca... 10.0.0.1:2377 --advertise-addr 10.0.0.4:2377 --listen-addr 10.0.0.4:2377

Swarm 管理器高可用性(HA)
	[Swarm HA](http://c.biancheng.net/uploads/allimg/190418/4-1Z41Q25541296.gif)
	[详细文章：](http://c.biancheng.net/view/3178.html)
	
内置的Swarm 安全机制

锁定Swarm
	启用锁：	docker swarm init --autolock
	解锁  ：	docker swarm init --unlock
	
Docker Swarm 服务的部署及操作
	docker service create				// 创建一个新的服务
		docker service create --name web-fe -p 8080:8080 --replicas 5 xxx/xxx 
			与 docker container run 相似，--name：将其命名为 web-fa -p：映射端口	
	查看服务：
		docker service ls 
	查看服务副本列表及个副本的状态：
		docker service ps <service-name or serviceid>
	查看服务详细信息：
		docker service inspect --pretty xxx			// --pretty 易于阅读的格式
	
	副本服务 VS  全局服务：
		副本模式：服务的默认复制模式(Replication Mode) 是副本模式(replicated)
		全局模式：global 
				docker service create --mode global 
	服务的扩缩容：
		大流量情况下： 
			docker service scale web-fa=10			// 对web-fa服务扩容，将服务副本由5个增加到10个
		检查操作是否成功：
			docker service ls 
		显示服务副本在各个节点上是均衡分布：
			dockers service ps 
		减少副本树：
			docker service scale web-fa=5			// 从10个降为5个
	删除服务：
		docker service rm web-fa 
		docker service ls 
	滚动升级：
		docker network create -d overlay uber-net			// 创建网络并将服务接入网络
		[](http://c.biancheng.net/uploads/allimg/190418/4-1Z41Q4221H59.gif)
		docker network ls			// 查看网络是否创建成功

		docker service create --name uber-svc --network uber-net -p 80:80 --replicas 12 xxxx/xxx 
		docker service create --name uber-svc --network uber-net -publish published=80,target=80,mode=host --replicas 12 xxx/xxx
		docker service update					// 更新运行中的服务
		docker service ps	
		docker inspect --pretty

Docker Swarm 服务日志及相关配置
	docker service log					//	查看服务的日志
		节点默认配置服务是 json-file 日志驱动，还有 journald(仅限systemctl的linux主机)、syslog、splunk、gelf
		json-file和journald 可用logs命令
			docker service logs <service-name>
		第三方日志驱动：
			{
				"log-driver":"syslog"
			}
		docker service create --logdrive --log-opts				// 强制某服务使用一个不同的日志驱动，会覆盖 daemon.json的配置
			--follow ：进行跟踪
			--tail :	显示最近的日志
			--details ： 获取额外细节

Docker Swarm 汇总
	docker swarm init:	创建新的Swarm，成为第一管理节点
	docker swarm join-token: 加入管理节点和工作节点到现有Swarm
			docker swarm join-token manager: 获取新增管理节点 
			docker swarm join-token worker:  获取新增工作节点
	docker node ls:	列出Swarm中的所有节点及相关信息
	docker service create: 创建一个新服务
	docker service ls: 列出Swarm中运行的服务，如服务状态、副本等基本信息
	docker service ps <service>: 列出某个服务副本的信息
	docker service inspect: 获取关于服务的详细信息，--pretty 仅显示重要信息
	docker service scale: 对服务副本个数进行增减
	docker service update: 对运行中的服务属性进行变更
	docker service logs: 查看服务的日志
	docker serivce rm: 从Swarm中删除某服务，不做确认会删除服务的所有副本







