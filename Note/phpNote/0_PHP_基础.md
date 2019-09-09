```
 @Author : Hale Lv
 @Created Time : 2019-09-05 12:48:53
 @Description : 
```

### PHP 
	PHP : PHP Hypertext Perprocessor ,超文本预处理器的字符缩写。多用途脚本语言，可嵌入到HTML中
	主要作用于三个领域：
		1. 服务器脚本
		2. 命令行脚本
		3. 编程桌面应用程序
	:
	<?php
		echo 'hello ';
	>
	实用脚本
		<?php
			echo $_SERVER['HTTP_USER_AGENT'];
		<?php
			if(strpos($_SERVER['HTTP_USER_AGENT'],'MSIE') !== FALSE){
				echo 'use INTERNET EXPLORER';
			}
		>
		strpos() ：内置函数，功能：在一个字符串中搜索另外一个字符串
	处理表单：
		<form action='action.php' method='post'>
			<p> name: <input type='text' name='name' /> </p>
			<p> age : <input type='text' name='age' /> </p>
			...
		</form>
		action.php
			<?php
				echo htmlspecialchars($_POST['name']);
				echo (int)$_POST['age'];
			?>
			htmlspecialchars() ：使得HTML中的特殊字符能被正确的编码，不被使用者注入HTML和JavaScript代码
		$_REQUEST() : 超全局变量，包含了GET、POST、COOKIE和FILE的数据
		
### 安装与配置
		PHP领域： 网站和Web应用程序、命令行脚本、桌面GUI应用程序
		需要：PHP自身、Web服务器、Web浏览器
		Unix安装：编译安装所需知识和软件： Unix技能Make、C编译器、Web服务器、 模块组件
			初始的配置和安装： ./configure --help ：查看所有编译选项和简短解释
		FastCGI进程管理器 FPM
			FPM用于替换PHP FastCGI的大部分附加功能，对于高负载网站
			功能：
				1. 支持平滑停止/启动的高级进程管理功能
				2. 工作于不同的UID/GID/chroot环境下，监听不同的端口和使用不同的php.ini 配置文件 取代 safe_mode 的设置
				3. stdout 和 stderr 日志记录
				4. 发生意外的情况能够重新启动并缓存被破坏的opcode：Opcode是PHP脚本编译后的中间语言，类Java的字节码、Python的字节码对象pycodeobject
				5. 文件上传优化支持
				6. 慢日志，记录脚本
				7. fastcgi_finish_request() 特殊功能：用于在请求完成和刷新数据后，继续在后台执行耗时的工作。
				8. 动态/静态子进程产生
				9. 基于SAPI运行状态信息
				10. 基于PHP.ini 的配置文件
		PECL扩展库安装
			PECl通过PEAR打包系统来的PHP扩展库仓库，extname是PECL扩展库的名字，使用共享扩展库，需编译、安装、加载。通过将其包含在php.ini中用 extension PHP指令加载，或用dl()函数
			当编译PHP模块，拥有各种工具： autoconf、automake、libtool等
			查看 PHP.ini所在位置，显示所有PHP设定： 
				```
					<?php	phpinfo(); 
				```
				: php -i
				注意： 如未在phpinfo中显示，应查看日志
						在命令行使用PHP(CLI)，加载出错信息
						DLL文件位置： php.ini 中 extension_dir 设定的值
		用PEAR编译共享PECl扩展库
			PECl建立PHP扩展，用PECl命令：
				pecl install extname
					将下载extname的源代码，编译之，并将 extname.so 安装到 extension_dir中，然后extname.so 就可通过php.ini加载
			PECL安装beta包：
				pecl install extname-beta
			PECL安装一个指定版本：
				pecl install extname-0.1
		用phpize 编译共享PECL扩展库
			phpize 用来准备PHP扩展库的编译环境，扩展库的源程序位于 extname目录中
				: cd extname
					phpize
					./configure
					make && make install 
			成功安装将创建 extname.so 并设置于PHP的扩展目录中，需调整 php.ini，加入 extension=extname.so 后才能使用此扩展
			查看 phpize 的使用帮助：phpize --help
		php-config 
			：是一个简单的命令行脚本用于获取所安装的PHP配置信息
			如安装多个PHP版本，可在配置时使用 --with-php-config 指定哪个版本编译，指定了相对应的php-config脚本的路径
			php-config -h 显示所能使用的选项
			--prefix ：PHP安装的路径前缀 如 /usr/local
			--includes ： 列出用-l包含的所有文件
			--ldflags	： PHP编译时所用的LD标志
			--libs	：编译时所附加的库
			--extension-dir ：头文件的默认路径前缀
			--php-binary	： PHP CLI 或CGI可执行文件的完整路径
			--php-sapis		：列出可用的SAPI模块
			--configure-options ： 重现当前PHP在编译时的配置选项
			--version ：	PHP版本
			--vernum	： PHP版本号，以整数显示
		将PECL扩展库静态编译入PHP
			将扩展库源程序放入 php-src/ext/ 目录中告知PHP编译系统来生成其配置脚本
				： cd /your/phpsrcdir/ext
					pecl download extname 
					gzip -d <  extname.tgz | tar -xvf -
					mv extname-x.x.x extname
			强制PHP重新生成配置脚本，然后正常编译PHP
				cd /your/phpsrcdir
				rm configure
				./buildcon --force
				./configure --help
				./configure --with-extname --enable-someotherext --with-foobar
				make && make install
			是否用 --enable-extname 或 --with-extname 取决于扩展库，通常不需要外部库文件的扩展库使用 --enable ， 要确认的话，在buildconf 后运行：
				./configure --help | grep extname 
		配置文件
			配置文件php.ini 在PHP启动时被读取
		.user.ini 文件
			PHP 支持基于每个目录的.htaccess风格的ini文件，此类文件仅被 CGI/FastCGI SAPI处理，
		配置可被设定范围
			有些指令在PHP脚本中用 ini_set() 设定，有些只能在 php.ini 或 httd.conf 中
				：PHP_INI_USER ： 在用户脚本ini_set以及 .user.ini中设定
				：PHP_INI_PERDIR ： 可在 php.ini , .htaccess 或 httpd.conf中设定
				：PHP_INI_SYSTEM ： 可在 php.ini 或 httpd.conf 中设定
				：PHP_INI_ALL ： 可在任何地方设定
		修改配置设定
			PHP运行于 Apache 模块方式：
				可用Apache 的配置文件 如httpd.conf 和 .htaccess文件中的指令来修改 PHP 的配置设定， 需要有 AllowOverride Options 或  AllowOverride 权限才可以
			


