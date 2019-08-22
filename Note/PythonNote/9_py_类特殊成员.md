### 类特殊成员(属性和方法
	特殊： 方法名、属性名前后添加双下划线。 可重写或调用方法来实现特殊的功能
	如： 构造方法： __init__ ，通过重写类中的此方法实现自己的初始化逻辑
	__repr__()方法 ： 显式属性
	__del__方法：	销毁对象
	__dir__用法 ： 列出对象的所有属性(方法)名
	__dict__属性： 查看对象内部所有属性名和属性值组成的字典
	setattr() , getattr() , hasattr()
	issubclass , isinstance ： 检查类型
	__call__
	__getitem__ , __setitem__ , __delitem__ , __len__, __contains__
	__iter__ , __reversed__ ：实现迭代器
	生成器详解

	__repr__()方法： 显式属性
		class xxx:
			def __init__(self,xx,xxx):
				self.xx = xx
				self.xxx = xxx
		x = xxx('xx','xxx')
	__repr__(): 所有的类都是object类的子类，所以所有的对象都具有 __repr__()方法
		此方法：用于实现： 当程序直接打印该对象时，系统输出该对象的 自我描述 信息，用来告诉外界该对象具有的状态信息
		此方法返回该对象实现类的 "类名+object at + 内存地址"，如
		class obj:
				def __init__(self,xx,xxx):
					self.xx = xxx
					self.xxx = xxx
				def __repr__(self):
					return "self.xx" + self.xx + \
						,"self.xxx" + self.xxx 
		x = obj('xx','xxx')
	重写__repr__() 总是返回该对象的所有令人感兴趣的信息所组成的字符串，如下格式的字符串
		类名 [field1 = 值1， filed1 = 值2 ,...]

	__del__方法： 销毁对象
		与 __init__() 方法对象， __init__() 方法用于初始化对象，  __del__() 方法用于销毁python对象，在任何对象被系统收回之时，会自动调用该对象的 __del__() 方法
	如不需要一个对象时，必须把对象占用的内存空间释放，称为垃圾回收(GC, Garbage Collector)
		Python 采用自动引用计数(ARC) 方式来回收对象所占用的空间
		当对象被垃圾回收时，自动调用该对象的 __del__方法，当对象的引用计数变为0时，对象才会被回收
		class Obj:
			del __init__(self,xx):
				self.xx = xx
			def __del__(self):
				pass
		o = Obj('xx')
		x = o
		del x
	若父类提供 __del__()方法，则系统重写 __del__() 方法时必须显式调用父类的 __del__()方法，保证合理回收父类实例的部分属性

	__dir__用法：列出对象的所有属性(方法)名
		用于列出该对象内部的所有属性包活方法名，该方法将会返回包含所有属性方法名的序列
		当程序对某个对象执行 dir 函数时，将该对象的__dir__() 方法返回值进行排序，然后包装成 列表
		class obj:
			def __init__(self,xxx):
				self.xxx = xxx
			def info():
				pass 
		x = obj
		print(x.__dir__())
			不仅输出对对象定义的xxx 、info属性和方法，还有系统内置的属性和方法，如 __repr__, __del__方法

	__dict__属性： 查看对象内部所有属性名和属性值组成的字典
		即可看对象的所有内部状态，也可通过字典语法来访问或修改指定属性的值
			class obj:
				def __init__(self,xxx):
					self.xxx = xxx
			x = obj
			print(x.__dict__)
			print(x.__dict__(xxx))

setattr(), getattr(), hasattr() 函数用法
	动态检测对象是否包含某些属性或方法相关的函数：
		1. hasattr(obj,name) : 检查obj对象是否包含名为 name 的属性或方法
		2. getattr(object,name[,default]) : 获取object对象中名为 name 的属性的属性值
		3. setattr(obj,name,value,/) : 将obj对象的 name 属性设为 value
			class obj:
				def __init__(self,xx,xxx):
					self.xx = xx
					self.xxx = xxx
				def info():
					pass
			x = obj
			print(hasattr(x,'xxx'))		// True
			print(getattr(x,'xxx'))		// True
			setattr(x,'xx','yy')
			print(x.xx)
	setattr() 可改变 对象的属性值，若对象设置的属性不存在，可添加属性

issubclass 和 isinstance 函数 ： 检查类型
	issubclass(cls, clsss_or_tuple) : 检查cls是否为后一个类或元组包含的多个类中任意类的子类
	isinstance(obj, class_or_tuple) : 检查obj是否为后一个类或元组包含的多个类中任意类的对象
	区别：
		issubclass 第一个参数是类名，判断是否为子类
		isinstance 第一个是变量，判断是否为该类或子类的实例						 
		第二参数都可使用 元组
	__base__属性 ： 通过该属性可查看该类的所有直接父类，该属性返回所有直接父类组成的元组
		class x:
			pass
		class xx:
			pass
		class xxx(x,xx):
			pass
		print(x.__base__)
		print(xx.__base__)

	__subclasses__()方法 ： 查看该类的所有直接子类，返回该类的所有组成的列表
		print(x.__subclasses__()

	__call__方法
		hasattr 函数判断指定属性或方法是否存在，  __call__属性： 进一步判断该属性或方法是否可调用
		class x:
			def __init__(self,xx,xxx):
				self.xx = xx
				self.xxx = xxx
			def ValidLogin(self):
				pass
		x = x('xx','xxx')
		print(x.xx,'__call__')
		print(x.xxx,'__call__')
	
	__getitem__ , __setitem__ , __delitem__ , __len__ , __contains__ 
		序列的特征 可包含多个元素，相关的特殊方法：
			__len__(self)	： 返回值决定序列中元素的个数
			__getitem__(self,key) ： 获取指定索引对应的元素，key是整数值或slice对象，会引发 KeyError异常
			__contains__(self,item) ： 判断序列是否包含指定元素
			__setitem__(self,key,value) ： 指定设置索引对应的元素，key 是整数值或slice对象，否则引发 KeyError异常
			__delitem__(self,key) ： 删除指定索引对应的元素
		def xx(key):
			if not isinstace(key,int) : raise TypeError('must int')
			if key < 0 : raise IndexError('is ini')
		class xxx:
			def __init__(self):
				self.__changed = {}
				self.deleted = []
			def __len__(self):
				pass
			def __getitem__(self,key):
				pass
			def __setitem__(self,key,value):
				pass
			def __delitem(self,key):
				pass

	__iter__ 和 __reversed__ ：实现迭代器
		for循环遍历列表、元组和字典等对象都是可迭代的，都属于迭代器
		实现迭代器，需实现两个方法：
			1. __iter__(self) : 该方法返回一个迭代器，必须包含一个 __next__() 方法，返回迭代器的下一个元素
			2. __reversed__(self) : 为内奸的reversed 反转函数提供支持，对指定迭代器执行反转时
		class  x:
			def __init__(self,len):
				self.first = 0
				self.sec = 1
				self.__len = len
			def __next__(self):
				if self.__len == 0:
					raise StopIteration
					self.first, self.sec = self.sec, self.first + self.sec
					self.__len -= 1
					return self.first
			def __iter__(self):
				return self

	生成器
		生成器与迭代器的区别在于： 迭代器通常是先定义一个迭代器类，通过创建实例来创建迭代器。 生成器：先定义一个包含 yield 语句的函数，然后通过调用该函数来创建生成器
		创建生成器
			创建生成器的步骤：
				1. 定义一个包含 yield 语句的函数
				2. 调用第一步创建的函数得到生成器
					def xxx(val,step):
						xx = 0 
						for i in range(val):
							xx += i * step
							yield xx
				yield xx 语句的作用：
					1. 每次返回一个值，类return 语句
					2. 冻结执行，每次执行到yield 语句时会被暂停
		两种方式创建生成器：
			1. 使用 for 循环的生成器推导式
			2. 调用带 yield 语句的生成器函数
		生成器的方法：
			1. 外部程序通过 send 方法发送数据
			2. 生成器函数使用 yield 语句接收收据
		生成器两个常用方法：
			1. close ：用于停止生成器
			2. throw ：用于在生成器内部(yield语句内) 引发一个异常


