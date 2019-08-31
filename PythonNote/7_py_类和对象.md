### 类和对象
	封装、继承、多态

面向对象： 一切皆对象
	面向对象编程(Object-oriented Programming, OOP)，是一种封装代码的方法
		代码封装：隐藏实现功能的具体代码，仅留接口
		分为两部分描述：
			1. 表面特征： 颜色、外观等
			2. 行为：爬、运动
			所有变量都是对象，
		面向对象相关术语：
			类： 即模版，可创建出多个具体实例。称为：类的实例化
			对象： 创造出的实例，称为对象
			属性： 类中所有变量 称为属性
			方法： 类中所有函数 称为方法

定义类
	类：仅充当图纸，根据图纸创造对象。 先定义、在创建类的实物对象，通过实例对象实现特定的功能。类名：每个单词首字母大写，单词与单词不能有分隔符
	创建类使用 class 关键字
		class 类名：
			N个类属性
			N个类方法
	
	__init__()类构造方法
		用于创建对象使用，没创建一个类的实例对象时，会自动调用它。
			def __init__(self,...):
				代码块
			可包含多个参数，但必须包含 self 此参数，必须作为第一个，类的构造方法至少要一个self参数，self 不需要手动传递参数,python自动给 self传值。
			class Person {
				''' commit '''
				def __init__(self):
					print('构造方法')
			}

类对象的创建和使用
	class 语句只创建类，需手动创建类的对象，创建类对象的过程称为类的实例化
		类名(参数)
		class Person {
			def __init__(self,name,age):
				self.name = name
				self.age = age
		}
		p = Person('Hale',23)
	
	类对象的使用
		作用：
			1. 操作对象的实例变量，即访问、修改实例对象的值，以及给对象添加、删除实例变量
			2. 调用对象的方法。
		类对象访问变量或方法
			使用已创建好的对象访问类中的实例变量
				对象名.变量名
			使用类对象调用类中方法
				对象名.方法名(参数)
				对象与变量名及方法名 用 ' . ' 连接
		给类对象动态添加变量
			为已创建好的对象动态增加实例变量，只要为它的新变量赋值
				xxx.yyy = ['xxxx','xxxx']
			删除变量：
				del xxx.yyy
		给类对象动态添加方法
			如果希望动态增加的方法能自动绑定到第一个参数，可借助于types模块下的MethodType 进行包装

	self 用法
		python 类方法中的self 参数相当于 C++中的 this 指针
		同一个类可产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，python自动绑定类方法的第一个参数指向调用该方法的对象，即解释器知道操作哪个对象的方法
		对构造方法，self 参数 代表 该 构造方法 正在初始化的对象
		class Obj {
			def __ini__(self):
				pass
			def __name(self):
				pass
			def __jump(self):
				self.name()
		}
			当self参数作为对象的默认引用时，可访问self参数，也可当成实例方法的返回值
			class ReturnSelf {
				def obj(self):
					if hasattr(self,'age'):
						self.age += 1
					else: 
						self.age = 1
					return self
			}
			rs = ReturnSelf()		// 实例化

类变量和实例变量(类属性和实例属性)
	类中定义的属性和方法，在外部，无法调用。 可把类看做独立的作用域，称为 类命名空间，类属性定义在类命令空间内的变量
		类属性 可分为： 类属性也称类变量，和 实例属性也称实例变量
		类变量： 指定义在类中，但在各个类方法外的变量，类变量的特点是：所有类的实例化和对象都可共享类变量的值，即类变量可在所有实例化对象中作为公用资源
			类变量推荐直接用类名访问，也可用对象名访问
				改变类变量的值会作用于该类所有的实例化对象

实例变量(实例属性)
	指：定义在类的方法中的属性，特点：只作用于调用方法的对象
		实例变量只能通过对象名访问，无法通过类名直接访问
			class Obj {
				name = 'hale'
				age = 23
				def change(self,name,age):
					self.name = name
					self.age = age
			}
			one = Obj()
			one.change('judy',24)
			print(one.name,one.age)			//	Judy 24
			print(Obj.name,Obj.age)			//	Hale 23

实例方法、静态方法和类方法详解
	分为： 类方法、实例方法、静态方法
	
	类实例方法
		实例方法： 至少需要包含一个self参数，用于绑定调用此方法的实例对象，可用类对象、也可用类名调用
			p = Person{}
			p.say('xxx')
			Person.say(person,'xxx')
	
	类方法
		类方法： 至少包含一个参数，名为： cls， 自动将类本身绑定给 cls 参数， cls命名不规定，可随意命名
		类方法需要使用 @classmethod 修饰
			class Obj:
				# @classmethod 修饰的方法是类方法
				@classmethod 
				def name(cls):
					print('Class Method:',cls)
			如没有 @classmethod ，会将 name方法认定为 实例方法，而不是类方法
	
	类静态方法
		静态方法和函数唯一区别： 静态方法定义在类空间，而函数定义在程序所在的空间中
		静态方法没有类似 self cls 特殊的参数，因此不会对包含的参数做任何类或对象的绑定。此方法中无法调用任何类和对象的属性和方法，其和类关系不大
		静态方法使用 @staticmethod 修饰
			class Obj:
				@staticmethod
				def name(p):
					print('static Method', p)
		静态方法的调用：可用类名，也可用类对象
			Obj.name('Class Name')
			o = Obj()
			b.name('Class Object')
	
类调用实例方法
	# 定义全局空间的foo函数
	def foo():
		pass
	# 全局空间的bar变量
	bar = 20
	class Obj:
		# 定义Obj空间的bar变量
		def foo():
			pass
		bar = 200
	# 调用Obj空间的函数和变量
	foo()
	Obj.foo()
	
总结： python类可调用实例方法，使用类调用实例方法，不会自动为方法的第一个参数self绑定参数值，程序必须显式为参数self传参，称为：未绑定方法

property 函数：定义属性
	属性名 = property(fget=NOne, fset=None, fdel=None, doc=None)
		fget：制定获取该属性值的类方法， fset：指定设置该属性值的方法， fdel：指定删除该属性值的方法，doc： 提供说明此函数的作用
		类似property 函数合成的属性被称为计算属性，并不存储任何状态，值通过某种算法得到，当程序对该值赋值时，被赋的值也会被存储到其他实例变量中

@parperty 装饰器
	既保护类的封装特性，又可以用 对象.属性 操作类属性，除了 property 函数，还提供 @property 装饰器，可直接通过方法名来访问方法，
	@preperty 
	def 方法名(self)
		代码块
	要想实现修改 xx 属性的值，还为xx属性添加 setter方法，可用 setter装饰器
		@方法名.setter
		def 方法名(self,value):
			代码块
	可用 deleter 装饰器 删除指定属性
		@方法名.deleter
		def 方法名(self):
			代码块

@函数装饰器及用法
	内置的函数装饰器：	@staticmethod	@classmethod	@property
	自定义函数装饰器：
		1. 将被修饰的函数(函数B) 作为参数传给 @ 符号引用的函数(函数A)
		2. 将函数B替换(装饰) 成第一步的返回值

封装机制及实现方法
	目的：
		隐藏类的实现细节
		使用预定义方法访问，可加入控制逻辑，限制对属性的不合理访问
		进行数据检查，保证完整性
		便于修改，提高可维护性
	实现封装的两方面：
		1. 将对象的属性和实现细节隐藏起来，不可直接访问
		2. 暴露方法，对属性安全访问和操作
	定义：
		类的成员命名以双下划线开头，就能隐藏
		class User:
			def __hide(self):
				pass
			def getname(self):
				return self.__name

继承机制及作用
		实现继承的类称为 子类， 被继承的类称为 父类，也叫 基类、超类
		子类继承父来的语法：在定义类时，将多个父类放在子类后的圆括号内
			class 类名(父类1，父类2,...):
				类定义部分
		Python是多继承机制，一个类可继承多个父类
			object 类是所有类的父类，直接父类、间接父类
			子类是对父类的扩展，子类是一种特殊的父类
			从子类的角度看，子类扩展(extend)类父类，从父类的角度看，父类派生出(derive)出子类，
			class Fruit:
				def name(self):
					pass
			class Animal:
				def name(self):
			class Obj(Fruit,Animal):
				pass

父类方法重写
	子类与父类同名的方法为方法重写(Override)，也叫方法覆盖
	使用未绑定方法调用被重写的方法
		
super()函数：调用父类的构造方法
	子类继承父类的构造方法，如子类有多个直接父类，优先选择最前面父类的构造方法
	如果子类重写了父类的构造方法，子类的构造方法必须调用父类的构造方法
		子类调用父类构造方法的2种方式：
			1. 使用未绑定，构造方法是实例方法，可通过此方式来调用
			2. 使用super()函数调用父类的构造方法
				当子类继承多个父类时，super()只调用第一个父类的构造方法，其他父类构造方法只能使用 未绑定 的方式调用

__slots(两侧得都有两下划线)__: 限制类实例动态添加属性和方法
	__slots__ 属性的值是一个元组，该元组的所有元素列出了该类的实例允许动态添加的所有属性名和方法名

type(): 动态创建类
	type 可指定三个参数：
		1. 参数一： 创建的类名
		2. 参数二： 该类继承的父类集合，使用元组指定多个父类
		3. 参数三： 该字典对象为该类绑定的类变量和方法

MetaClass 元类
	创建类的来，即创建类后，再由类来创建实例进行应用，使用元类可在创建类时动态修改类定义
	定义元类： 类名以MetaClass 结尾，元类需要定义并实现 _new_()方法，一定要有返回值
		__new__()方法作用： 使用class定义新类时，如指定了元类，__new__方法会被自动执行

多态
	同一变量完全可在不同的时间应用不同的对象，当同一变量在调用同一方法，可呈现多种行为
		class Bird:
			def move(self,filed):
				print('bird %s' % filed)
		class Dog:
			def move(self,filed):
				print('dog %s' % field)
		b = Bird()
		b.move('sky')
		d = Dog()
		d.move('road')

枚举类定义和使用
	定义方式：
		1. 使用Enum 列出多个枚举值来创建枚举类
		2. 通过继承Enum 基类来派生枚举类
		import enum 
		s = enum.Enum('name',('hale','judy','jally'))
	可通过枚举类变量名或枚举值来访问指定枚举对象
	__members__ 属性，返回一个dict字典，包含了该枚举的所有实例，遍历 __members__属性访问枚举的所有实例

	枚举构造器
		可定义构造器，为枚举定义构造器后，在定义枚举实例时，必须为构造器参数设置值

	





