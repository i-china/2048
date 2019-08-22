##	列表、元组、字典、集合
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


