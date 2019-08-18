### Python 编程基础
	[编译型和解释型](http://c.biancheng.net/uploads/allimg/190211/2-1Z2111G33L03.gif)
	领域：
		Web应用开发：
			通过mod_wsgi模块，apache可运行python的web程序，Python定义WSGI标准应用接口协调HTTP服务器与基于Python的Web程序之间的通信。Web框架：Django、TurboGears、web2py等
		操作系统管理、自动化运维开发：
			例：Ubunut的Ubiquity安装器、RedHat、Fedora的Anaconda安装器等
		游戏开发：
			支持更多的特性和数据类型，例：文明
		编写服务器软件：
			支持各种网络协议，可编写服务器软件及网络爬虫，例：第三方库Twisted
		科学计算：
			NumPy、SciPy、Matplotlip等
	3和2的区别：
		print函数代替print语句
		默认使用UTF-8编码
		除法运算
		异常
		八进制字面量表示
		不等于运算符
		数据类型
	Python 2to3：自动将Python2.x代码转换为Pyhton3.x代码

安装
	Linux 两种方式：
		1. 命令行安装
			apt update
			apt install python3.6 
			unlink /usr/bin/python		//	取消旧python的映射
			ln -s /usr/bin/python3.6 /usr/bin/python		// python3环境的路径和版本要写正确
		2. 源码安装
			下载：	wget python3.6下载路径
			压缩：	tar -zxvf python3.6.tgz
			编译：	./configure --prefix=/usr/local/	make	make install
					
###	第一个python

```
代码编写
	两种方式：
		1. 在提示符 >>> 直接输入： print("hello world")
		2. 文本编辑器编写并执行python程序
			vim hi.python
				print("hello world")
			python hi.python
			
注释：
	单行注释： #  
	多行注释： 1. '''  xxx...xxx '''	2. """ xxx...xxx """

中文编码声明注释：
	1. # -*-coding:utf-8 -*-	2. # coding=utf-8
	
缩进规则：
	冒号(:)和代码缩进

编码规范(PEP8)
	PEP: Python Enhancement Proposal, 8代表Pyton代码的样式指南
		1. 每个import语句只导入一个模块，避免导入多个
		2. 不在行为加分号，不将两条命令放一行
		3. 每行不超80字符，如超，用小括号连接
		4. 用空行增强可读性，顶级定义空两行，方法定义空一行
		5. 使用空格分隔 运算符、函数参数

Python标识符命名规范
	1. 字符、下划线、数字，数字不开头
	2. 不与保留子相同
	3. 不包含空格、@、%、$等特殊字符
	4. 严格区分大小写
	5. 下划线开头有特殊意义
		单下划线： 不能直接访问的类属性，无法通过 from ... import * 的方式导入
		双下划线： 类的私有成员
		双下划线开头和结尾： 专用标识符

关键字(保留子)
	查看方式：
		import keyword
		keyword.kwlist

内置函数
	[内置函数](https://docs.python.org/zh-cn/3/library/functions.html)



```


###	变量类型和运算符

数值类型(整形、浮点型、复数)
	整形：
		二进制：1 和 0 组成， 0b|0B
		八进制：0～7 ， 0o|0O
		十进制：普通的整数，不以0开头
		十六进制：0～9 + A～F， 0x|0X
	浮点型：
		十进制形式：eg：3.14
		科学计数：eg：2.3e2
	复数：
		虚部用j|J表示
	
字符串(长字符串、原始字符串)
	长字符串：
		三个引号：单引号、双引号
	原始字符串：
		需要'\'进行转义
	
bytes类型
	由多个字节组成，以字节为单位进行操作，只负责以字节(二进制格式)序列来记录数据
	将字符串转换为 bytes对象的三种方式：
		1. 如内容是ASCII，在字符串之前添加 b 构建字节串值
		2. 调用 bytes() 函数
		3. 调用字符串本身的 encode() 方法

bool布尔类型
	真：True ：1 
	假：False：0 

len() 获取字符串长度或字节数
	len(string)： 字符串的字符|字符串长度|一个字符串占用的字节数， string 进行长度统计的字符串

input() 获取用户输入的字符串
	将用户输入的内容放到字符串中，返回一个字符串中

print() 高级用法
	同时输出多个变量： eg：print(value,...sep='',end='\n',file=sys.stdout,flush=False)

格式化字符串(格式化输出)
	对各种类型的数据进行格式化输出
		print()函数包含三部分：
			1. 格式化字符串，相当于字符串模版
			2. 固定使用" % " 作为分隔符
			3. 对应的变量，多个用'()'括号括起来
	转换说明符：
		%d， %i ：	十进制的整数
		%o		：	八进制的整数
		%x，%X	：	十六进制整数
		%e		：	科学计数的浮点数
		%E		：	科学计数的浮点数
		%f，%F	：	十进制的浮点数
		%g		：	智能选择%f或%e格式
		%G		：	智能选择%F或%E格式
		%c		：	格式化字符及其ASCII码
		%r		：	使用repr()将变量或表达式转换为字符串
		%s		：	使用str()将变量或字符串转换为字符串

转义字符
	\			：	一行未完，转到下一行继续写
	\'			：	单引号
	\"			：	双引号
	\0			：	空
	\n			：	换行符
	\r			：	回车符
	\t			：	水平制表符
	\a			：	响铃
	\b			：	退格
	\\			：	反斜线
	\0dd		：	八进制数，dd代表字符，eg：\012代表换行
	\xhh		：	十六进制数，hh代表字符，eg：\x0a 代表换行

数据类型转换
	int(x)		：	将x转换为整数类型
	lloat(x)	：	转为浮点型
	complex(real,[,imag])	： 创建一个复数
	str(x)		：	转为字符串
	repr(x)		：	转为表达式字符串
	eval(x)		：	计算字符串中有效python表达式，返回一个对象
	chr(x)		：	将整数x转为一个字符
	ord(x)		：	将字符x转为对应的整数值
	hex(x)		：	将整数x转为十六进制字符串
	oct(x)		：	整数x转为八进制字符串

算术运算符
	+	：	加
	-	：	减
	*	：	乘
	/	:	除
	%	:	取余，返回除法的余数
	//	:	整除，返回商的整数部分
	**	:	幂，返回x的y次方	eg：2**4，	16

赋值运算符
	=	： 基本赋值
	扩展后的赋值运算符：
		+=	：	加赋值
		-=	：	减赋值
		*=	：	乘赋值
		/=	：	除赋值
		%=	：	取余赋值
		**=	：	幂赋值
		//=	：	取整数赋值
		|=	：	按位或赋值
		^=	：	按位与赋值
		<<=	：	左移赋值
		>>=	：	右移赋值

位运算符
	&	：	按位与
	|	：	按位或
	^	：	按位异或
	～	：	按位取反
	<<	：	按位左移
	>>	：	按位右移
	[详细说明](http://c.biancheng.net/view/2184.html)

比较运算符
	>		：	大于
	>=		：	大于等于
	<		：	小于
	<=		：	小于等于
	==		：	等于
	!=		：	不等于
	is		：	判断两个变量引用的对象是否相同，不同返回False
	is not	：	判断两个变量引用的对象是否不相同，不同返回True
		比较运算符 == 和 is 的区别：
			== ： 比较两个变量的值是否相等。 
			is ： 对比两个变量引用的是否是同一个对象	

逻辑运算符
	and		：	与	两个都为True，为True，否则为False
	or		：	或	一个为True，为True，两都为False，则为False
	not		：	非	只需一个为True，则为False

三目运算符(三元)
	先对逻辑表达式求值，如果为True，则返回True_statements的值，如为False，则返回False_statements的值
		A = 5	B = 3
		st = "A大于B" if A > B else "A小于B"

运算符优先级
	[优先级](http://c.biancheng.net/view/2190.html)


###	列表、元组、字典、集合
	内置的四种常用数据结构： 列表(list)、 元组(tuple)、 字典(dict)、 集合(set)
	列表和元组不同和相同：
		相同：按顺序保存元素
		不同：元组不可修改，列表可修改
	字典和集合的相同和不同：
		相同：数据是无序的
		不同：字典可用key-value形式保存数据

序列		
	序列：一块可存放多个值的连续内容空间，值按一定顺序排列，可通过值位置的编号(索引)访问他们
		序列包括：字符串、列表、元祖、集合、字典。	字典和集合不支持索引、切片、相加、相乘等操作
			字符串是一种常见的序列，可直接通过索引访问字符串内的字符
			索引值从0开始递增，支持索引值负数，从右向左计数
		序列切片：是访问序列中元素的另一种方法，可访问一定范围内的元素，通过切片，生成新的序列
			snmae[start ：end ：step]
				sname：表示序列的名称
				start：表示切片开始索引位置，默认为0，从开头进行切片
				end：  表示切片的结束位置，若不指定，默认为序列的长度
				step： 表示隔几个存储位置取一次元素
		序列相加：两种相同类型的序列使用 " + " 运算符做相加操作，但不去重
			相同类型：指 + 两侧都是序列类型，都为元组 或 都为字符串
		序列相乘：
			使用数字n乘以一个序列生成新的序列，eg : print('hi' * 3)
		检查元素是否包含在序列中：使用 in 关键字
			value in sequence	： value 要检查的元素，sequence 指定的序列
		序列相关的内置函数：
			len()			：	计算序列的长度，即返回序列中包含多少个元素
			max()			：	最大元素
			min()			：	最小元素
			list()			：	将序列转为列表
			str()			：	将序列转为字符串
			sum()			：	计算元素和
			sorted()		：	对元素排序
			reversted()		：	反向序列中的元素
			enumerate()		：	将序列组合为一个索引序列，用在for循环中

### list列表
	python没有数组，有列表。 列表将所有元素放在一对中括号中[],相邻元素用逗号隔开，eg：[var1,var2,...varn]，个数不限，支持的数据类型即可。可以是：整数、实数、字符串、列表、元组、浮点数等
		type(['xxx',xxx,[xxx,'xxx'],xxx]) ：查看数据类型，数据类型为list，即为：列表
	创建列表
		使用 = 运算符创建列表， 使用赋值运算符 = 直接将列表赋值给变量
					listname = [element1, element2,... elementn]
		使用list()函数创建列表：
			list() 将 元组、区间等对象转换为 列表
				a_tuple = ('name',23)
				a_list = list(a_tuple)	
	访问列表元素
		通过列表的索引获取指定的元素 或 直接使用 print() 函数
			list_str[n]		|		print(list_str)
	删除列表
		使用 del 语句删除
			del list_str	

列表添加元素的三种方法
	1. append()：在列表的末尾追加元素，传递列表或元组，视为一个元素，直接添加到列表中，形成包含列表和元组
		list_str.append(obj)
	2. extend()：不将被追加的列表或元组当作一个整体，只追加列表中的元素
		list_str.extend(obj)
	3. insert()：在列表中间增加元素
		list_str.insert(index，obj)	： index 将元素插入到列表中指定位置处的索引值，将插入的对象视为一个整体
	
列表删除元素的三种方法
	删除元素的三种场景：
		1. 根据元素位置的索引值，用del语句
		2. 元素的位置删除，用 list提供的remove 方法
		3. 删除所有元素，用list提供的clear方法
	删除元素的3中方法：
		1. 根据索引值删除元素,类删除列表，用del语句
			del list_str[n:m]	
		2. 根据元素值删除元素
			remove 删除第一个和指定值相同的元素，如没有，则显示ValueError错误，删除前判断是否存在，长于count()方法组合使用
		3. 删除列表所有元素
			clear()	: 清空列表的所有元素
					list_str.clear() 

list列表修改元素
	列表的元素类变量，可对列表的元素赋值，即可修改列表的元素
		通过索引到列表元素赋值，可用正数索引，也可用负数索引
			list_str = list(rang(1,5))
			list_str[1:3] = ['a','b']
				可用步长

list常用方法(count、index、pop、reverse、sort)
	交互模式：查看列表包含的所有方法： dir(list)
	count()	：统计列表中某个元素出现的次数
		listname.count(obj)
	index() ：定位某个元素在列表中出现的位置，即索引
		listname.index(obj,start,end)	: start、end：指定范围内搜索元素
	pop()	：移除列表中指定索引处的元素，若不指定，默认移除列表中最后一个元素
		listname.pop(index)
	reverse() ：反转列表中的元素
		listname.reverse()
	sort() ：对列表元素进行排序
		listname.sort(key=None,reserse=False)
			key ： 指定每个元素提取用于比较的健，key=str.lower：不区分大小写
			reserse ：是否需要反转排序，默认False表示从小到大。True为从大到小排序
	
### tuple元组
	




