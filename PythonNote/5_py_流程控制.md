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






