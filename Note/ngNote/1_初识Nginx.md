### 配置文件由指令与指令块构成
[Nginx_DOC](http://www.nginx.cn/doc/)
每条指令以 ； 分号结尾，指令与参数间以空格符号分隔
指令块以 {} 大括号将多条指令组织在一起
include 语句允许组合多个配置文件以提升可维护性
使用# 符号添加注释，提高可读性
使用 $ 符号使用变量
部分指令的参数支持正则表达式
配置参数： 时间的单位
s: seconds	m: minutes	h:hours	 d:days  w:weeks   M:months,30 days   y:years,365 days
		   空间的单位
bytes	k/K: kilobytes		m/M: megabytes		g/G: gigabytes
eg:  
```  http {
		include		mime.types;
		upstream xxx {
			server 127.0.0.1:8000;
		}
	}
	server {
		listen 443 http2;
		# Nginx Config syntax
		limit_req_zone $binary_remote_addr zone=one:10m rate=1r/s;
		location ~* \.(gif|jpg|jpeg)$ {
				proxy_cache my_cache;
				expires 3m;proxy_cache_key $host$uri$is_args$args;
				proxy_cache_valid 200 304 302 1d;
				proxy_pass http://xxx.xxx;
		}
	}
```

### 重载，热部署，日志切割
Nginx 命令行：
格式： nginx -s reload
帮助： -？ -h
使用指定的配置文件： -c
指定配置指令： -g
指定运行目录： -p
发送信号： -s	：	立刻停止服务： stop		优雅的停止：quit	重载配置文件： reload   重新开始记录日志文件 reopen
测试配置文件是否有语法错误： -t		-T
打印nginx的版本信息、编译信息等： -v	-V

重载： nginx -s reload 
热部署：nginx 版本升级， 编译安装， kill -USR2 nginxID(ps -ef | grep nginx), kill -WINCH ID(进程号)
日志切割：xxx.lg(日志文件) nginx -s reopen 

### Nginx 配置静态资源Web服务器
http {
	include		mime.types;
	#default_type	application/octet-stream;
	log_format		main		'$remote_addr - $remote_user [$time_local] "$request"  '
								'$status  $body_bytes_sent "$http_referer" '
								'"$http_user_agent" "$http_x_forwarded_for"';
	
	client_max_body_size	60M;

	proxy_cache_path	/tmp/nginxcache	levels=1:2	keys_zone=my_cache:10m	max_size=10g inactive=60m use_temp_path=off;

	
	#access_log		logs/access.log		main;

	sendfile		on;
	#tcp_nopush		on;

	#keepalive_timeout	0;
	keepalive_timeout	65;

	gzip	on;
	gzip_min_lengt		1;
	gzip_comp_level		2;
	gzip_types			text/plain	application/x-javascript	text/css	application/xml		text/javascript		application/x-httpd-php		image/jpeg	image/gif	image/png;
}

server {
	listen 8080;
	server_name hale.dev;

	access_log  logs/hale.dev.log main;

	location / {
		alias dirpath/;
		#autoindex on;						# 开启目录浏览功能
		#set $limit_rate 1k;				# 限制访问速度 每秒传输1kb
		#index  index.html  index.htm;
	}
	#error_page 404			/404.html;
	# redirect server error pages to the static page /50x.html 
	#
	error_page		500	502	503	504		/50x.html;	
}

##### nginx -s reload 

### Nginx 搭建缓存功能的反向代理服务
openresty实现反向代理

include vhost/****.conf;
upstream local {
	server 127.0.0.1:8080;
}

server {
	server_name hale.dev;
	listen 80;

	location / {
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

			#proxy_cache my_cache;	
			
			#proxy_cache_key $host$uri$is_args$args;
			#proxy_cache_valid	200	304	302	1d;
			proxy_pass	http://local;
	}
}

#### 此处的配置详情可以在Nginx官网 ngx__http__proxy_module 中获取

### GoAccess实现可视化并实时监控access日志






























