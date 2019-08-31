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




