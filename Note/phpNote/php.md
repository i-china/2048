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
			

```
 @Author : Hale Lv
 @Created Time : 2019-09-06 10:23:00
 @Description : 
```

### 基本语法
	
> PHP标记
	<?php		?>	: 告诉PHP开始和停止解析二者之间的代码
	短标记： <? ?> 不推荐， 通过激活 php.ini 中的short_open_tag 配置指令或编译PHP时使用配置选项 --enable-short-tags 

>	从HTML 中分离
		1.使用条件的高级分离术
			<?php if (expression == true): ?>
			this is html text
			<?php endif;	?>
		2.开始和结束标记
			<?php echo 'hi' ?>
			<script language='php'
				echo 'hi';
			/script>
			<? echo 'hi' ?>
			<% echo 'hi' %>
> 指令分隔符
		PHP需要在每个语句后用分号结束指令，PHP代码中的结束标记隐含表示了一个分号；，在一个PHP代码中的最后一行可不用分号结束，如还有新行，代码段的结束标记包含了行结束
> 注释
	单行注释： //  ， #
	多行注释： /* */ 

### 类型：
	PHP支持9中原始数据类型
		四种标量类型： 
			boolean 布尔型
			integer 整型
			float 浮点型 也称作 double
			string 字符串
		三种复合类型：
			array 数组
			object 对象
			callback 可调用
		两种特殊类型：
			resource 资源
			null 无类型
		伪类型 ：
			mixed  混合类型
			number 数字类型
			callback 回调类型 又称 callable
			array|object 数组|对象
			void	无类型
		伪变量： 
			$...
		变量的类型，是由PHP根据该变量使用的上下文在运行时决定
		查看某个表达式的值和类型： var_dump() 函数
		只想得到一个易读懂类型的表达式方式用于调试： gettype() 函数
		校验某个类型： is_type() 函数
			<?php	$str = TRUE	
					echo gettype(str);			// boolean
					is_int($str);				// no
			?>
			变量强制转换为某类型：使用强制转换 或 settype 函数

### Boolean 布尔类型
		TRUE 或 FALSE ： 不区分大小写
		转换为布尔值：
			使用： bool() 或  boolean 强制转换
			当为boolean时， 为False的值：
				1. 布尔值False
				2. 数组 0
				3. 浮点数 0.0
				4. 空字符串
				5. 字符串0
				6. 空数组
				7. NULL
				8. 从空标记生成的SimpleXML对象
			所有其他值都被认为是 True ，包括任何资源和NAN

### Integer 整型
		integer 是集合 Z = {...,-2,-1,0,1,2,...} 中的某个数
		整数值可使用二进制、八进制、十进制、十六进制，可加可选的符号 + 、 -
			：要使用八进制，数字前必须加：0 ，使用十六进制，数字前加：0x，0X，使用二进制，数字前需加： 0b
		整数溢出：
			给定一个数超出了integer范围，将被解释为float，如执行的运算结果超出了integer范围，返回float
		PHP中没有整除的运算符，强制转换为 integer，使用round函数可更好地进行四舍五入
		转换为整型
			要明确地将一个值转换为 integer，用int或integer强制转换
			将一个值转换为整型： intval 函数
		从布尔值转换： False 为 0 ， True 为 1
		从浮点数转换： 浮点数转换为整数，将向下取整
		PHP7.0.0 起， NaN和Infinity 转换为integer， 不再是underfined，都会变为 0 

### Float 浮点数
		浮点型，也叫浮点数float，双精度数double或实数 real 
		浮点数的字长和平台相关
		转换为浮点数：先将值转换为整型，然后再转换为浮点
		比较浮点数： 比较两个浮点数是否相等是有问题的，有迂回的方法比较浮点数值
			要测试浮点数是否相等，使用一个仅比该数值大一丁点的最小误差值，称为机器极小值 epsilon 或最小单元取整数，计算所能接受的最小的差别值
			浮点数在小数后五位精度内都是相等的
			$a = 1.2345678, $b = 1.23456789;
			$epsilon = 0.00001;
			if(abs($a - $b) < $epsilon) {	echo 'true'	};
		NaN : 代表着一个在浮点数运算中未定义或不可表述的值，此值于任何值比较初TRUE外，结果都是False ，NaN代表任何不同值，不应拿NaN去和其他值比较，包括自身，应该用 is_nan 来检查

### String 字符串
		一个字符串string右一系列的字符组成，每个字符等同于一个字节，PHP只能支持256个字符集，不支持Unicode。String最大2GB
		字符串的四种表达方式：
			1. 单引号
			2. 双引号
			3. heredoc 语法结构
			4. newdoc 语法结构
		1. 单引号：
			单引号包起来的字符。 要表达单引号自身，需在它前面加反斜线，反斜线本身要用两个反斜线。
		2. 双引号：
			双引号 包括的字符，可对一些特殊的字符进行解析：
				\n	： 换行 ASCII字符集中的 LF 或 0x0A	10
				\r	： 回车 ASCII字符集中的 CR 或 0x0D 13
				\t	： 水平制表符 ASCII 字符集中的 HT 或 0x09 9
				\v	： 垂直制表符 ASCII 字符集中的 VT 或 0x0B 11
				\e	： Escape ASCII 的 ESC 
				\f	： 换页， ASCII 的 FF 
				\\	： 反斜线 
				\$	： 美元标记
				\"	： 双引号
				\[0-7]{1,3}	： 符合正则表达式序列的八进制方式表达的字符
				\x[0-9A-Fa-f]{1,2} ： 符合正则表达式的十六进制方式来表达的字符
		3. Heredoc 结构，类双引号
			:	<<<Str
				...
				Str;
				: 在该运算符后要提供一个标识符，然后换行， 接着是字符串本身，最后用前面定义的标识符结束
				标识符命名： 只能包含字符、数字、下划线，必须以字符或下划线开头
					$Hi = <<<EOF
						echo 'hi';
						hhha
					EOF;
				Heredoc结构用在函数参数中来传递数据，也可用Heredoc结构来初始化静态变量和类的属性和常量， 还可在Heredoc结构中用双引号来声明标识符
		4. NewDoc 结构，类单引号
			： <<<'Str' 
				...
				Str;
			： 不能用于解析，适合嵌入 PHP代码或其他大段不用解析的文本
		变量解析规则： 
			1. 简单规则 ：用最少的代码在一个String中嵌入一个变量， 一个array值，或一个object 的属性
			2. 复杂规则： 表示用花括号包围的表达式
		简单语法：
			如遇到美元符号，组合为一个合法的变量名，可用花括号来明确变量名的界线
			一个array索引或object属性可被解析，数组索引和对象属性都用方括号来表示结束边际
		复杂(花括号) 语法
			可使用复杂的表达式
			具有string表达的标量变量， 数组单元或对象属性可使用此语法，用花括号括起来，
		存取和修改字符串中的字符
			字符可通过一个从0 开始的下标， 可用类array的方括号包含对应的数字来访问和修改，把string当成字符组成的array
		有用的函数和运算符
			字符串可用 点 运算符连接
		转换成字符串
			在一个值前面加上 string 或 用 strval函数转换为字符串，使用函数echo或print时，可自动转换为string
			一个布尔值的TRUE转换为 string 的 1 ， FALSE被转换为""空字符串，
			[More](https://www.php.net/manual/zh/language.types.string.php)
			数组转换为字符串为 Array 数组，使用 echo $arr['foo'] 显示整个数组内容
			NULL 总是被转换为空字符串
		字符串转换为数值
			如没有包含 'e'或'E'，该字符串将被当成integer取值，其他情况下都被作为 float来取值
			字符串的开始部分决定了他的值， 如字符串以合法的数值开始，则使用该数值，否则其值为 0 ，合法数值由可选的正负号。
			通过将一个字符转换为整数已得到其他的代码，使用函数 ord 和 chr 实现 ASCII码和字符间的转换
		字符串类型详解
			
### Array 数组
		数组实际上是一个有序映射，映射是把一个values 关联到 keys 的类型，做了优化，可当作数组或列表向量，散列表，字典，栈，队列以及更多可能性，由于数组元素也可是另一个数组，树形结构和多维数组是允许的
		定义数组 array 
			用array() 语言结构 新建一个数组，接受任意数量用逗号分隔的 键key => 值value 对
				array(key => value ...) 
					键(key) 可是整数integer 或 字符串 string
					值(value) 可是任意类型的值
				最后一个数组单元后的逗号可省略，通常用单行数组定义，多行通常保留最后一个逗号
					$arr = ['name' => 'hale','age' => 23 ,...];
				key 可是 integer 或 string ， value 可是任意类型
					key 的强制转换：
						1. 合法整型值的字符串会被转换为整型， 如 "8"会被存储为 8， "08"则不会强制转换，因为不是合法的十进制数值
						2. 浮点数会被转换为整型，小数部分会被舍去，如8.7 被存储为 8
						3. 布尔值转换为 整型， true 为 1 ，false 为0 
						4. NULL 转换为 空字符串， null 存储为 ""
						5. 数组和对象不能被用作 键名，如用会导致警告： lllegal offset type
						数组可同时含有integer 和 string 类型的键名，不区分索引数组和关联数组
						如对给出的值没有指定键名，则取当前最大的整数索引值，新的键名将是该值加1，如指定的键名已存在，则该值会被覆盖。 还可只对某些单元指定键名而对其他的空置
				用方括号语法访问数组单元
					数组单元通过array[key] 语法来访问
						方括号和花括号可互换访问数组单元 
						可直接对函数或方法调用进行数组解引用，通过临时变量
						可直接对一个数组原型进行数组解引用
				用方括号语法新建/修改
					通过明示地设定其中的值来修改一个已有数组

### Object 对象
		对象初始化
			创建一个新的对象object ， 使用new 语句实例化一个类：
				<?php
					class Foo{
						...
					}
				?>
				$foo = new Foo();
			转换为对象
				如将一个对象转换为对象，不会有任何变化，如任何类型的值被转换为对象，将会创建一个内置类 stdClass 实例，如该值为 NULL，则新的实例为空， array 转换为 object 将使键名称为 属性名并具有相对应的值
				<?php
					$obj = (object) array('a' => 1);
				>

### Resource 资源类型
			资源resource 是一种特殊变量，保存了到外部资源的一个引用，资源是通过专门的函数来建立和使用的
				转换为资源：
					资源类型变量保存为打开文件、数据库连接、图形画布区域等特殊句柄，因此将其他类型的值转换为资源没有意义
				释放资源：
					引用计数系统是Zend引擎的一部分，可自动检测到一个资源不再被引用，此资源使用的所有外部资源都会被垃圾回收系统释放

### NULL 
		特殊的NULL 值表示一个变量没有值
		变量被视为NULL的情况：
			1. 被赋值为 NULL
			2. 尚未被赋值
			3. 被 unset() 
		NULL 类型只有一个值，不区分大小写的NULL
		is_null 和 unset 
		转换到NULL	：
			使用(unset)$var 讲一个变量转换为 null，不会删除该变量或unset 其值，仅返回 NULL 值

### Callback / Callable 类型
		Callable 类型指定回调类型 callback， 
		call_user_func 或 usort 可接受用户自定义的回调函数作为参数，回调函数不止函数、还可是对象的方法，包括静态类方法
		传递：
			PHP将函数以  string 形式传递，可使用任何内置或用户自定义函数，但除了语言结构，如： array 、echo 、empty、eval、exit、isset、list、print、unset
			一个已实例化的object的方法被作为 array传递，下标0 包含该 object ，下标1包含方法名，在同一个类可访问 protected 和 private 方法
			除了普通的用户自定义函数外，也可传递 匿名函数 给回调函数
			在函数中注册有多个回调内容时，如 call_user_func 与 call_user_func_array ，如掐一个回调未捕获的异常，其后的将不会再被调用

### 伪类型和变量
		伪类型 pseudo-types 是PHP文档用于指示参数可使用的类型和值，不是原生类型， 不能把伪类型用于自定义函数的类型约束
		mixed ： 一个参数可接受多种不同的类型
			如： gettype 可接受所有的PHP类型，str_replace 可接受字符串和数组
		number ： 一个参数可是integer 或 float 
		callback ： 引入callbale 类型之前使用了 callback 伪类型，含义完全相同
		array| object ： 参数可是array，也可是object 
		void ： 返回类型意味着函数的返回值是无用的，void作为参数列表意味着函数不接受任何参数
		在函数原型中，  $... 表示等等，当一个参数可接受任意个参数时使用

### 类型转换的判别
		变量类型是根据使用该变量的上下文决定的， 如把string赋值给变量$var ，就成了一个string，如把一个integer 赋给$var, 它就变成了 integer 
		自动类型转换，如 乘法运算符 '*' ，如任何一个操作是 float，则所有的操作数都被当为float，结果也是float
		类型强制转换
			允许的强制转换有：
				(int),(integer)  转换为 整型 integer
				(bool),(boolean) 转换为 布尔类型 boolean
				(float),(double),(real)  转换为浮点型
				(string)	转换为 字符串
				(array)		转换为数组
				(object)	转换为对象
				(unset)	 转换为NULL


```
 @Author : Hale Lv
 @Created Time : 2019-09-06 15:14:21
 @Description : 
```

### 变量
	用一个美元符号后跟变量表示,变量名区分大小写
	有效变量名: 由字母或下划线开头，后跟任意数量的字母、数字、下划线。按照正则表达式，可表述为： [a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]
	$this 是一个特殊的变量，不能被赋值
		默认是传值赋值，当将一个表达式的值赋予一个变量时，整个原始表达式的值被赋值到目标变量。
		引用赋值： 新的变量的变量简单的引用了原始变量，改动新的变量将影响到新的原始变量
		使用引用赋值，简单将一个 & 符号加到将要赋值的变量前
		不需要初始化变量，为初始化的变量具有其类型的默认值，布尔类型的变量默认值是 FALSE， 整型和浮点型变量默认值是0，字符串默认是空字符串，数组默认空数组

### 预定义变量	
	在任何范围内自动生效， 通常被称为 自动全局变量 autoglobals 或 超全局变量 superglobals
	
### 变量范围
	即定义的额上下文背景，即生效范围。PHP变量只有一个单独的范围，包含了include 和 require 引入的文件。
	global 关键字
		使用 global 声明
	在全局范围内访问的办法： 使用PHP自定义 $GLOBALS 数组
		使用 $GLOBALS 代替 global
		$GLOBALS 是一个关联数组，每个变量为一个元素，键名对应变量名， 值对应变量的内容，
	使用静态变量
		静态变量仅在局部函数域中存在，当程序执行离开此作用域时，其值并不丢失
		静态变量提供处理递归函数的方法
	全局和静态变量的引用
		变量的static 和 global 定义是以引用的方式实现的，

### 可变变量
		变量的变量名可动态设置和使用
		可变变量获取了普通变量的值作为这个可变变量的变量名
		类的解析也可通过可变属性名来访问，可变属性名将在该调用所处的范围内被解析
		可用花括号给属性名清晰定界
	
### PHP之外的变量
		HTML 表单 GET 和 POST 
			当一个表单提交给PHP脚本时，表单中的信息会自动在脚本中可用
				使用GET表单，要用适当的GET预定义变量
				变量名中的点和空格被转换为 下划线 
				magic_quotes_gpc 配置指令影响到 GET 、POST、和COOKIE的值，如打开，值会自动转换，如it's 会转换为 it\'s  
		IMAGE SUBMIT 变量名
			<input type='image' src='xxx.gif' name='sub' />
			当用户点击图像中的某处时，相应的表单会被传送到服务器，并加上两个变量sub_x 和 sub_y ，包含了用户点击图像的坐标，PHP自动将点转换为了下划线
		HTTP Cookies 
			Cookies ： 是一种在远程浏览器端存储数据并能追踪或识别在此访问的用户的机制，可用setcookie 函数设定 cookies。 Cookies 是HTTP信息头中的一部分，SetCookie函数必须向浏览器发送任何输出之前调用，对于header 函数也有同样的限制，Cookie 数据会在相应的cookie数据数组中可用，如： $_COOKIE, $HTTP_COOKIE_VARS, $_REQUEST
			如将多个值赋给一个cookie变量，必须将其赋成数组：
				: setcookie("name['hale']",'first',time()+3600);
				  setcookie("name['judy']",'second',time()+3600);
				将会建立两个单独的cookie，如仅仅一个cookie中设定多个值，考虑先在值上使用 serialize 或 explode 
				浏览器中一个cookie会替换掉上一个同名的cookie，除非路径或域不同：
					eg: 
						<?php
							if(isset($_COOKIE['count'])){
								$count = $_COOKIE['count'] + 1;
							}else {
								$count = 1;
							}
						setcookie('count', $count,$time() + 3600);
						setcookie("Cart[$count]", $time, time()+3600);
						>
		变量中的点
			点 . ：不是PHP变量中的合法字符，PHP会自动将变量名中的点替换为下划线
		确定变量类型
			PHP包括几个函数可判断变量的类型，如： gettype、is_array、is_float、is_int、is_string、is_object

### 常量
		是一个简单值的标识符，在脚本执行期间值不能改变。 区分大小写，默认大写。 
		命名：字母或下划线开头，后面跟着任何字母、数字或下划线。
		常量的范围是全局的， 与 superglobals 一样，
		定义： 使用 define 函数定义常量， 可使用 const 关键字在类定义之外定义，常量一旦被定义，不可改变或取消定义
		常量： 包含 标量数据 boolean、integer、float、 string 
		获取常量的值： constant 、 get_defined_constants 获得所有已定义的常量列表
		检查是否定义了某常量，用defined 函数
		常量和变量的不同： 
			1. 常量前没有美元符号
			2. 常量只能用define 函数定义，不能通过赋值语句
			3. 常量可不用理会变量的作用域而在任何地方定义和访问
			4. 常量一旦定义不可更改和取消
			5. 常量的值只能是标量
		1. 使用 define函数 定义
				<?php
					define('CONSTANT','hi');
					echo CONSTANT;
				>
		2. 使用 const 定义
					const CONSTANT = 'hi';
					echo CONSTANT;
		define 和 const：
			const 关键字定义常量必须处于最顶端的作用域，此方法是在编译时定义的，不能在函数内，循环内以及if语句之内用const 来定义常量

### 魔术常量
		不区分大小写，值随着代码中的位置改变而改变
			__LINE__ :	文件中的当前行号
			__FILE__ :	文件的完整路径和文件名
			__DIR__ :	文件所在目录
			__FUNCTION__ : 函数名称
			__CLASS__ : 类的名称
			__TARIT__ : Trait的名字
			__METHOD__ : 类的方法名， 区分大小写
			__NAMESPACE__ : 当前命名空间的名称， 区分大小写

### 表达式
		是PHP的基石，几乎所写的任何东西都是一个表达式，最基本的表达式形式是 常量和 变量，如 $a = 3； 即将值3 赋值给了$a 


```
 @Author : Hale Lv
 @Created Time : 2019-09-06 16:47:47
 @Description : 
```

### 运算符
	运算符优先级
	算术运算符
	赋值运算符
	位运算符
	比较运算符
	错误控制运算符
	执行运算符
	递增/递减运算符
	逻辑运算符
	字符串运算符
	数组运算符
	类型运算符
	运算符是通过给出一个或多个值来产生另一个值
		一元运算符：只接受一个值，如逻辑取反或递增运算符
		二元运算符：接受两个值，如算术运算符 + 、- 
		三元运算符：接受三个值
		
#### 运算符优先级
		指定了两个表达式绑定的有多 紧密
		如果运算级别相同，运算符的结合方向决定了该如何运算
		没有结合的相同优先级的运算符不能连在一起使用
		括号的使用

#### 算术运算符
		- + - * / % ** 
	
#### 赋值运算符
		= ：把右边表达式的值赋给左边的运算符
		引用赋值
			引用赋值意味这 两个变量指向了同一个数据

#### 位运算符
		允许对整数中指定的位进行求值和操作

#### 比较运算符

#### 错误控制运算符
		错误控制运算符： @ 
		set_error_handler 设定自定义的错误处理函数

#### 执行运算符
		反引号： `` 
	
#### 递增/递减运算符

#### 逻辑运算符

#### 字符串运算符

#### 数组运算符
	把右边的数组元素附加到左边的数组后面， 两个数组中都有的键名，则只用左边数组中的，右边的被忽略


#### 类型运算符
		instanceof ： 确定一个PHP变量是否属于某一类 class 的实例


```
 @Author : Hale Lv
 @Created Time : 2019-09-06 17:26:40
 @Description : 
```

### 流程控制
	if
	else 
	elseif else if
	while 
	do-while
	for
	foreach
	break
	continue
	switch
	declere
	return
	include
	require
	goto
