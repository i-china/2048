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
	




### tuple元组
	按特定顺序排序的元素，序列不可变。不可边的列表，保存不可变的内容，用()定义，用，逗号分隔。元组可存储整数、实数、字符串、列表、元组等任何类型的数据
	('xxx',[x,xx,'xxx'],(x,xx,xxx))
	创建元组
		1. 使用 "=" 运算符直接创建元组
			tupe_str = (x,xx,xxx)
		2. 使用tuple()函数创建元组
			tuple(data)
				list_str = [x,'xx',xxx]
				tuple_str = tuple(list_str)
	访问元组元素
		使用元组各元素的索引值获取
			tuple_str[n]
	修改元组元素
		元组不可改变序列，元素不可单独修改。
		修改方法：
			1. 对元组重新赋值：
				tuple_str = (x,xx,'xxx')
				tuple_str = ('x','xx',xxx)
			2. 通过连接多个元组的方式向元组中添加新元素
				tuple_str = (x,'xx',xxx)
				tuple_str + ('y',yy,'yyy')
				元组连接的必须是元组，否则抛出：TypeError 错误
	删除元组
		使用 del 语句删除：
			tuple_str = ('x',xx,'xxx')
			del(tuple_str)
	元组使用场景：
		1. 元组作为很多内置函数和序列类型方法的返回值存在，使用某些函数或方法，如返回元组类型，对元组进行处理。
		2. 元组比列表访问和处理速度更快，如 对指定元素访问，且不修改时，使用元组
		3. 元组在映射(和集合的成员)中可做 健 使用，列表不行。 

元组和列表的区别：
		同属序列类型，按照顺序存放在一组数据，数据类型不受限制
		数据修改：
			列表可修改
			元组不可修改
		字节：元组比列表少16个字节
			列表是动态的，存储指针指向对应的元素 占用8个字节，元素可变，需要额外存储已经分配的长度大小
			元组，长度固定，存储元素不可变，存储空间是固定的。

### 字典
	dict ： 类列表，数据的集合，可变序列类型。无序可变序列，内容以 键值对 形式存放
	特征：
		通过键来读取元素
		任意数据类型的无需集合
		可变的，可任意嵌套
		键必须是唯一
		键必须不可变
	
	创建字典
		1. 花括号 { }
			每个元素包含2部分： 键 : 值， 键和值用冒号分割，相邻元素用逗号分割，大括号{}包含
			eg : dict_str = {'name':'hale','age':23}
				同一字典 键值 必须唯一，键值可以是整数、字符串、元组
		2. 通过 fromkeys() 创建字典
			创建所有键值为空的字典
			eg:	dict_str = dict.formkeys(list, value=None)
				各个键对应的值为空None， 通常用初始化字典，设置value的默认值
		3. 通过 dict() 映射函数创建字典
			eg： dict_str = dict(one=1,tow=2,thre=2)
				 dict_str = [('one',1),('toe',2)]
				 dict_str = [['one',1],['tow',2]]
				 dict_str = (('one'.1),('two',2))
				 dict_str = ['one','two','three']
	访问字典
		通过 键 访问对应的元素值。 但字典元素是无序的
			eg： dict_str['one']
				 dict_str.get(key[,default])	// 通过 get 方法获取指定键的值
					dict_str.get('two')
				使用get() 方法，可为其设置默认值
	删除字典
		使用 del 语句 删除字典
			eg： del(dict_str)

字典基本操作(添加、修改、删除键值对)
	字典无需
	操作字典的方法：
		1. 向现有字典添加键值对
		2. 修改现有字典中的键值对
		3. 删除指定键值对
		4. 判断是否存在指定键值对
	
	字典添加键值对
		dict[key] = value
			dict ： 表示字典名称
			key  ： 要添加元素的键，不可重复
			value： 要添加的值。支持的数据类型
			
	修改键值对
		不是修改某一键值对的键和值，只修改值
		如 新添加的元素的键已存在，替换原键对应的值
	
	删除键值对
		del 
			eg：del dict_str['one']
	
	判断是否存在
		使用 in 或者 not in 运算符
			eg：'one' in dict_str		|		'two' not in dict_str

字典方法攻略
	keys() 、values() 、 items()
		keys() ：返回字典中的所有键
			dict_str.keys()
		values() ： 返回字典中所有键对应的值
			dict_str.values()
		items() ： 返回字典中所有的键值对
			dict_str.items()
	返回数据的两个方法：
		list()	： 将返回的数据转换为 列表
			list(dict_str.keys())
		利用多重赋值，李彤循环结构将键或值分别赋给不同的变量
			for k in dict_str.keys():
				print(k,end=' ')
			for v in dict_str.values():
				...v
			for k,v in dict_str.items():
				print('key: ',k,'value: ',v)
	
	copy() 方法
		返回一个具有相同键值对的新字典
			dict_str.copy()			// copy 将字典 的数据 拷贝给 字典other
				拷贝原理，有深、有浅。 copy为深拷贝
	
	update() 方法
		使用一个字典所包含的键值对更新已有的字典
			如果已存在的键值对，原value会被覆盖，如不存在，即添加

	pop() 方法
		获取指定 key 对应的 value，并删除这个键值对
			dict_stc.pop('key')

	popitem()
		随机弹出字典中的一个键值对，弹出字典最后一个键值对，底层存储的最后一个键值对
			dict_str.popitem()

	setdefault() 方法
		根据 key 获取对应 value 的值，如获取的key在字典中不存在，会设置默认的value，然后返回该key对应的value
			dict_str.setdefault('one',23)

	使用字典格式化字符串
		在字符串模板中按 key 指定变量， 然后通过字典为字符串模板中的 key 设置值 
			字符串模板中使用key
				people = 'name: %(name)s , price: %(price)0.2f, sex: %(sex)s'
				object = {'name':'Hale','price':23,'sex':'man'}
				print(people % object)

Set 集合
	保存不重复的元素，集合中的元素是唯一的，set集合是无序的
	集合将所有元素放在一堆大括号中{}，元素用 ',' 分割
		{key,key2,keyN}
		只能存储不可变的数据类型，即 整形、浮点型、字符串、元组。 不可以存储 列表、字典、集合。
	两种集合类型：
		1. set 类型的集合 ： 可做 添加、删除元素的操作
		2. frozenset 集合 ：	不可以
	
	创建set集合
		2种方式：
			1. 使用 {} 创建 ：直接将集合赋值给变量
				set_str = {key,key1,keyn...}
			
			2. set()函数创建
				set_str = set(iteration)
					iteration : 表示字符串、列表、元组、range对象等数据

	访问set集合元素
		访问集合元素使用循环结构
			for key in set_str:
				print(key,end=' ')
	
	删除set集合
		del()
			del(set_str)
	集合常用操作：向集合中添加、删除元素。以及集合之间做交集、并集、差集等运算。

set集合基本操作(添加、删除、交集、并集、差集)
	向set集合中添加元素
		set_str.add(element)
			只能是数字、字符串、元组或布尔类型，不能添加列表、字典、集合等可变数据
	从set集合删除元素
		set_str.remove(element)
			如删除不存在的，抛出 KeyError错误
				如不想提示KetError错误，可使用discard()方法

set集合做交集、并集、差集运算
	交集： &	取两集合公共的元素		set1 & set2	
	并集： |	取两集合全部的元素		set1 | set2
	差集： -	取一个集合中另一集合没有的元素	set1 - set2
	对称差集： ^	取集合A和B中不属于A&B的元素  set1 ^ set2

set集合方法
	dir(set)	
		add、clear、copy、difference、difference_update、discard、intersection、intersection_update、isdisjoint、issubset、i是superset、pop、remove、symmetric_difference、symmetric_difference_update、union、update

frozenset 集合(set 集合不可变版本)
	特点：
		1. 当集合元素不需要改变时，使用frozenset代替set更安全
		2. API不需要改变时，必须用frozenset代替set。如 集合元素不可变，set只能包含frozenset
			s = set()
			f = frozenset('key')
			s.add(f)

深入底层字典和集合
	字典和集合是进行过性能高度优化的数据结构
		字典和集合的工作原理：
			数据机构
				字典和集合的内部结构都是一张哈希表
					对字典：表存储了哈希值(hash)、键和值
					对集合：哈希表内只存储单一的元素
	哈希表插入数据
	哈希表查找数据
	哈希表删除元素


### 字符串常用方法详解
	拼接字符串、截取字符串、格式化字符串

字符串拼接(+拼接数字)
	使用加号 (+) 作为字符串的拼接运算符
	字符串拼接数字
		先将数字转换为 字符串
			数字转换为字符串： str()	repr()
				直接拼接字符串和数字，会报错

截取字符串(字符串切片)
	通过索引来操作字符：
		string[index]				// index 表示索引值，从0开始递增，最后一个为-1
	使用范围获取字符串的中间值：
		string[start: end: step]
			string : 要截取的字符串
			start : 要截取的第一个字符所在的索引，默认为0
			end ：要截取最后一个字符所在的索引。如不指定，默认字符串的长度
			step ：从start字符开始，step 距离获取一个字符，end索引出的字符。step默认值为1
				支持用 in 运算符判断是hi否包含某个子串

split() : 分割字符串
	将一个字符串按照指定的分隔符切分成多个子串，字串被保存在列表中，不包含分隔符
		str.split(sep,maxsplit)
				1. str：要分割的字符串
				2. set：指定分隔符，默认使用空字符分割
				3. maxsplit：可选参数，指定分割的次数，如不指定，次数不限

join() ：合并字符串
	将列表(或元组)中多个字符串采用固定的分隔符连接在一起
		join_str = str.join(iterable)
			1. join_str : 合并后生成的新字符串
			2. str ： 指定合并时的分隔符
			3. iterator： 做合并操作的源字符串数据，允许：列表、元组等

count() ：统计字符串出现的次数
	用于检索指定字符串在另一个字符中出现的次数，如检索的字符串不存在，返回 0，否则返回出现的次数
		str.count(sub[,start[,end]])
			1. str : 原字符串	
			2. sub : 要检索的字符串
			3. start : 起始位置
			4. end : 终止位置

find() ：检测字符串中是否包含某字串
	检索字符串中是否包含目标字符串，如包含：出现第一次该字符串的索引，返回-1
		1. str：原字符串
		2. sub：目标字符串
		3. start： 起始位置，若不指定，默认从头开始索引
		4. end ：结束位置，若不指定，一直检索到结尾
	rfind() ：字符串从右边开始检索

index() ：检测字符串中是否包含某子串
	检索是否包含指定的字符串，若指定的字符串不存在，抛出异常
		str.index(sub[,start[,end]])
			1. str : 原字符串
			2. sub : 子字符串
			3. start : 起始位置，默认从头开始
			4. end : 结束位置，默认到结尾

startswith() 和 endswith
	startswith() ： 检索字符串是否以指定字符串开头，是返回True，反之False
		str.startswith(sub[,start[,end]])
			1. str ： 原字符串
			2. sub ： 要检索的字串
			3. start ：起始位置，默认从头开始
			4. end ： 结束索引
	end.swith(sub[,start[,end]]) : 是否以指定字符结尾，是返回True，反之Flase
		str.endswith(sub[,start[,end]])
			1. str : 原字符串
			2. sub : 检索的字符串
			3. start : 起始位置
			4. end : 结束位置
			
字符串大小写转换的三种函数
	title()	: 将字符串中每个单词的首字符转为大写，其他转为小写
		str.title()
			str 要进行转换的字符串
	lower() : 将字符串所有大写字符转为小写
		str.lower()
	upper() : 将字符串所有小写字母转为大写
		str.upper()

去除字符串中空格(删除指定字符)的3种方法
	去除字符串中的空格和特殊字符
		特殊字符： 制表符 \t、回车符 \r 、换行符 \n
	strip() 	lstrip() 	rstrip() 
	1. strip()	:	删除字符串前后(左右两侧)的空格或特殊字符
		str.strip([chars]) 
			str : 原字符串
			chars ：指定要删除的字符，可同时指定多个，若不指定，默认为空格、制表符、回车符、换行符等特殊字符
	2. lstrip() :	删除字符左边的空格或特殊字符
		str.lstrip([chars])
	3. rstrip() :	删除字符右边的空格或特殊字符
		str.rstrip([chars])

format() 格式化输出
	str.format(args)
		str : 指定字符串显示样式
		args: 指定要进行格式化转换的项，如多项，逗号分割
			str 格式：
				{ [index][:[fill] align] [sign] [#] [width] [.precision] [type] ]}
					index :  指定 ；后边设置的格式要作用到args中第几个数据，索引值从0开始
					fill : 指定空白处填充的字符
					align : 指定数据的对齐方式
						< :	左对齐
						> : 右对齐
						= : 右对齐，放在填充内容的最左侧，只对数字类型有效
						^ : 居中，和width参数一起使用
					sign：
						+	： 
						-	：
						空格：
						#	：
					width ：指定输出数据时所占的宽度
					.precision : 指定保留的小数位数
					type ：指定输出数据的具体类型
						s	： 字符串
						d	： 十进制整数
						c	： 将十进制整数自动转换为对应的Unicode字符
						e|E	： 转为科学技术后，再格式化输出
						g|G	： 自动再e|f E|F 中切换
						b	： 将十进制自动转换为二进制，再格式化
						o	： 转为八进制，再格式化
						x|X	： 转为十六进制
						f|F	： 转为浮点数
						%	： 显示百分比，默认小数点后6位

encode() 和 decode() 字符串编码转换
	2中常用字符串类型： str 、bytes。 str：Unicode 。 bytes：二进制数据。使用encode 和decode 进行转换
	encode() : 将str类型转换为bytes类型，成为 编码
		str.encode([encoding="utf-8"][,errors="strict"])
			str ：要进行转换的字符串
			encoding="utf-8" : 采用的字符编码，默认位utf-8 中文：gb2312
			errors="strict"	 : 指定错误处理方法：
					strict :	遇到非法字符就抛出异常
					ignore :	忽略非法字符
					replace:	用 "?" 替换非法字符
					xmlcharrefreplace: 使用xml的字符引用

	decode() ： 将bytes类型的二进制数据转换为str类型，过程称为"解码"
		bytes.decode([encoding="utf-8"][,errors="strict"])
			bytes : 要进行转换的二进制数据
			encoding="utf-8": 解码时采用的字符编码
			errors="strict"

dir() 和 help() 帮助函数
	dir() : 列出指定类或模块名包含的全部内容，包括函数、方法、类、变量等
	help() : 查看某个函数或方法的帮助文档


### 流程控制
	两种基本流程控制结构： 分支结构、循环结构
		分支结构： 实现根本条件来选择性地执行某段代码
		循环结构： 实现根据循环条件重复执行某段代码
		if语句：分支
		while、for in 循环
			break 和 continue 控制程序的循环结构
	
	条件语句可分3中形式：
		if、if else、 if elif else
			if 表达式：
				代码块
			if 表达式：
				代码块 1
			else：
				代码块 2
			if 表达式 1：
				代码块 1
			elif 表达式 2：
				代码块 2
			elif 表达式 3：
				代码块 3
				...
			else :
				代码块 n

	if 表达式真假值判断方法：
		if 表达式的值 是 布尔值，要么是真 True，假为False
		假 False： False、None、0、 "" 、()、[]、{}

	if else 语句用法规范
		1. 代码块不要忘记缩进
		2. if 代码块不要随意缩进
		3. if 表达式不要遗忘冒号

	if 语句嵌套
		if condition 1:
			if condition 2:
				code1
			else:
				code2
	
	if condition 1:
		if condition 2:
			code 1
		else: 
			code 2
	else:
		if condition 3:
			code 3
		else:
			code 4

	pass 语句及作用
		占位

	assert 断言函数及用法
		对于对一个bool表达式进行断言，如为True，继续向下执行，否则引发 AssertionError错误
		会让程序奔溃，测试、调试的辅助工具
		eg： age = input('enter age')
			age = int(age)
			assert 30 < age < 100
			print('your age at 30 ~ 100')
			
while 循环语句
	如果条件condition为真，一直重复执行代码块
	while 条件表达式：
		代码块
		执行流程：判断条件表达式的值，如果为True 真，执行代码块语句，执行完毕，重新判断条件表达式的值是否为真，如为真，继续执行代码块，直到表达式的值为假False，才终止循环
	
	使用while循环遍历列表和元组
		列表和元组有索引，通过while循环、列表和元组的索引来遍历列表和元组中的所有元素
			eg： tuple_str = ('name','age','sex')
				i = 0
				while(i < len(tuple_str)):
					print(tuple_str[i])
					i += 1

for循环用法
	循环语句有2种，while 和for 
		用于遍历字符串、列表、元组、字典、集合等序列类型
			for 迭代变量 in 字符串|列表|元组|字典|集合：
				代码块
			迭代变量：用来存放从序列类型变量中读取的元素，一般不再循环中对迭代变量赋值，代码块值具有相同缩进格式的多行代码。也称为循环体

	for 进行数值循环
		如 0 ～100 的累加
		r = 0;
		for i in range(101):
			r += i
		print(r)
	range() : 生成一系列连续的整数，用于for循环中
			range(start,end,step)
				1. start : 计数的初始值，默认从0开始
				2. end : 计数的计数值，不能省略
				3. step : 指定步长，两个数之间的间隔，如省略，默认为1
					for i in range(1,10,2):
						print(i,end=' ')
	
	for循环遍历列表和元组
		列表或元组有几个元素，for循环的循环体就执行几次，迭代变量会依次被赋值为元素的值
	isinstance() 函数用于判断某个变量是否为指定类型的实例

	for 循环遍历字典
		1. items()	： 返回字典中所有key-value对的列表
		2. keys()	： 所有key的列表
		3. values()	： 所有value 的列表
	
循环结构中else用法
	while 和 for循环，可都跟 else 代码块，作用：当循环条件为False，程序最先执行else代码块的代码
	for 循环可使用else代码块，当for把所有元素遍历一次后，会执行else代码块，

for 和while 循环嵌套
	for 和 while 可循环嵌套
		for i in range(1,10):
			j = 0
			while j < 3:
				print("i %d, j %d",(i,j))
				j += 1
	循环可以两层或者更多层嵌套	

列表推导式for表达式
	利用range区间、元组、列表、字典、集合等数据类型，快速生成一个列表
	[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]]
		for 迭代变量 in 可迭代对象
			表达式

元组推导式
	利用range区间、元组、列表、字典、集合等，生成一个列表
	(表达式 for 迭代变量 in 可迭代对象[if 条件表达式])
	使用元组推导式获得新元组或新元组中的元素，有三种方式：
		1. 使用tuple()，直接将生成器对象转换为元组
			a = (x for x in range(1,10))
				print(tuple(a))
		2. 使用for循环遍历生成器对象，获得各个元素
			a = (x for x in range(1,10))
			for i in a:
				print(i,end=' ')
			print(tuple(a))
		3. 使用 __next__() 方法遍历生成器对象，获得各个元素
			a = (x for x in range(3))
			print(a.__next__())
			a = tuple(a)
		无论是for循环遍历生成器对象，还是__next__()遍历，遍历后原生成器对象不复存
	
字典推导式
	使用字典推导式可以借助列表、元组、字典、集合以及range区间，快速生成复合需求的字典
		{表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]}
			[]	扩起来的可省略

集合推导式
	集合推导式可借助 列表、元组、字典、集合以及range区间，快速生成符合需求的集合
		{表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]}
	集合推导式和字典推导式的区别：
		如果表达式以键值对(key:value)的形式，则是字典推导式，反之是集合推导式

zip函数用法
	可把两个列表 压缩 为一个zip对象(可迭代对象)，可使用一个循环并行遍历两个列表
		a = ['a','c','dd']
		b = [1,3,2]
		[x for x in zip(a,b)]
		zip函数压缩得到的可迭代对象所包含的元素是由原列表元素组成的元组
			
reversed 函数及用法
	反向遍历，可接收各种序列(元组、列表、区间等)，返回一个反序排列的法代器
		reversed()可对列表、元组进行反转
			
sorted函数及用法
	与reversed 函数类似，接收一个可迭代对象作为参数，返回一个对元素排序的列表
		不会改变传入的可迭代对象，而是返回新的、排序好的列表
			sorted 可传入一个 reverse 参数，也可传入一个 key 参数

2种强制离开循环体的方法：
	1. continue	： 可跳过执行本次循环体中剩余的代码，转而执行下一次的循环
	2. break ： 完全终止当前循环






