### 异常处理机制
	异常机制主要依赖try、except、else、finally、raise 五个关键字
		1. try 关键字后的代码块简称 try块，放置 引发异常的代码
		2. 在except 后对应的是异常类型和一个代码块，表明该 except 块处理这种类型的daimakaui	
		3. 多个except 后放一个 else 块，程序不出现异常还是执行 else 块
		4. finally 块用于回收在 try 打开的无力资源，异常机制保证 finally 块总被执行
		5. raise 用于引发实际的异常，可单独作为语句使用，引发具体异常对象

	常见异常类型
		语法错误 和 运行时错误
			语法错误：
				解析代码是出现的错误，报出 SyntaxError 语法错误
			运行时错误：
				逻辑错误
		常见异常类型
			AssertionError ： 当assert 关键字后的条件为假时，程序停止并抛出此异常
			AttributeError ： 试图访问的对象属性不存在时，抛出
			IndexError	   ： 索引超出序列范围
			KeyError	   ： 字典中查找一个不存在的关键字时
			NameError	   ： 尝试访问一个未声明的变量时
			TypeError	   ： 不同类型数据之间的无效操作
			ZeroDivisionError ： 除法运算中除数为 0 引发此异常

异常处理机制
	
try except 异常处理
	try:
		可能产生异常的代码块
	except ([Error1,Error2,...]) [as e]:		// ErrorN 表明处理异常的具体类型
		处理异常的代码块1
	except ([Error3,Error4,...]) [as e]:		// as e 表示将异常类型赋值给变量 e
		处理异常的代码块2
	执行流程：
		1. 先执行 try 中的代码块，如出现异常，自动生成异常对象，提交给Python解释器，称为引发异常
		2. 解释器收到异常，寻找处理该异常对象的except块，如找到合适的except块，则把异常对象交给except块，如找不到，则终止。
			try:
				name = input('Enter name')
			except (ValueError, ArithmeticError):
				print('error')
			except :
				print('no error')
	访问异常信息
		通过except块添加 as e 来访问异常对象的相关信息，当解释器决定调用某个except块来处理该异常对象时，会将异常对象赋值给except 块后的异常变量
		异常对象包含的属性和方法：
			args ： 返回异常的错误编号和描述字符串
			errno ： 返回异常的错误编号
			strerror ： 返回异常的描述字符串
			with_traceback() ： 处理异常的传播轨迹信息

	异常类的继承体系
		异常类派生于 BaseException，
		[继承关系](http://c.biancheng.net/uploads/allimg/190215/2-1Z2151H054Q0.gif)
		BaseException 主要子类是 Exception，不管是系统的异常类，还是用户自定义的异常类，都应该从Exception派生
			1. 如发生数值类型错误，则调用ValueError 对应的except块处理该异常
			2. 如发生逻辑错误： 2/0，则调用ArthmeticError 对应的except块处理该异常
			3. 如运行时发生其他异常，异常对象是Exception类或其他子类的实例，则调用Exception对应的except块处理该异常
			注： 先捕获小异常，再捕获大异常。

try except else 异常处理结构
	作用：指定当try块中没有发现异常时要执行的代码，若try中发现异常，则else块中的语句不会执行
		try:
			r = 20 / int(input('enter num'))
		except ValueError:
			pass
		except ArithmeticError:
			pass
		else:
			print('no error')
	
try except finally : 资源回收
	完整异常处理语法结构：
		try:
			xxx
		except SubException as e:
			xxx
		except SubException as e:
			xxx
		else:
			xxx
		finally:
			xxx
		在异常处理语法结构中，只有try块是必须的
			1. 如没有try块，就没有except 和 finally 块
			2. except 和 finally 块可选，可同时出现，也可出现其一
			3. 可有多个except块，但捕获父类异常的except块位于捕获子类异常的后面
			4. 不能只有try块，没有except  finally块
			5. 多个except 位于try块后，finally块位于所有except块之后
		不要在finally块中使用如return 或 raise 等导致方法终止的语句，若在finally中使用return 或 raise 语句，会导致 try 块、except、中的return、raise语句失效

	raise 用法
		如需自行引发异常，则使用raise语句
			raise [exceptionName [(reason)]]
		raise 语句三种用法
			1. raise： 单独一个raise。 引发当前上下文中捕获的异常，如在except中，引发 RuntimeError异常
			2. raise异常类名称： 指定异常类的默认实例
			3. raise异常类名称： 引发指定异常的同时，附带异常的描述信息
	raise 不需要参数
		class Demo:
			def __init__(self,init_price):
				self.init_price = init_price
			def bid(self,bid_price):
				try:
					xxx
				except Exception as e:
					xxx
					raise 

	except 和 raise 同时使用
		实现通过多个方法协作处理同一个异常，可在except中结合raise语句来完成
			try:
				xx
			except Exception as e:
				raise AuctionException('error message by self')
				raise AuctionException(e)
			对异常的处理分为两个部分：
				1. 应用后台需要通过日志来记录异常发生的详细情况
				2. 根据异常向应用使用者传达某种提示
		用户自定义异常对原始异常进行包装
			raise AuctionException(e)
			被称为： 异常包装或异常转译
	自定义异常类
		自定义异常需继承Exception 基类 或Exception的子类，
		class AuctionException(Exception):
			pass
		
sys.exc_info(): 获取异常信息
	捕获异常的2种方式获得更多的异常信息：
		1. 使用 sys 模块中的 exc_info 方法
		2. 使用 traceback 模块中的相关函数
	两个方法返回异常全部信息：exc_info 和 last_traceback 
			exc_info ： 将当前的异常信息以元组的形式返回，该元组包含三个元素， type、value、traceback
					type： 异常类型的名称
					value： 捕获到的异常实例
					traceback： 是一个traceback 对象
						try:
							pass
						except:
							print(sys.exc_info())

	traceback模块： 获取异常信息
		使用traceback 模块查看异常传播轨迹，现将traceback模块引入，提供两个方法：
			1. traceback.print_exec() ： 将异常传播轨迹信息输出到控制台或指定文件中
			2. format_exc()	： 将异常传播轨迹信息转换为 字符串
		print_exception(etype,value,tb[,limit[,file]])
			三个参数用于分别指定异常的信息：
				etype ： 指定异常类型
				value ： 指定异常值
				tb ： 指定异常的traceback 信息
		print_exc([limit[,file]])
			print_exc 自动处理except块所捕获的异常，涉及两个参数
				1. limit ： 限制显式异常传播的层数
				2. file  ： 指定将异常传播轨迹信息输出到指定文件中，如不指定该参数，默认输出到控制台
				import traceback
				def xxx():
					raise SelfException('by self')
				try:
					xxx()
				except:
						traceback.print_exec(file=open('log.txt','a'))

自定义异常类及用法
	自定义一个异常类，通常应继承自 Exception类，直接继承Exception。也可继承自从Exception 继承而来的类，间接继承Exception
	[异常继承图](http://c.biancheng.net/uploads/allimg/190819/2-1ZQ9154321244.gif)

异常机制使用细节
	成功的异常处理4个小目标
		1. 使程序代码混乱最小化
		2. 捕获并保留诊断信息
		3. 通知合适的人员
		4. 采用合适的方式结束异常活动
	不要过度使用异常
		1. 把异常和普通错误混淆
		2. 使用异常处理代替流程控制
		3. 不要使用过于庞大的try块
		4. 不要忽略捕获到的异常

assert 调试程序
	assert 条件表达式 [,描述信息]
		assert 语句作用： 当条件表示式为真时，什么也不做，如果为假，则assert抛出 AssertionError异常
			age = input('enter age')
			name = input('enter name')
			assert 20 < age < 100 , 'age at 20 ~ 100'
	assert 可与  try except 异常处理语句配合使用
		try:
			age = input('enter age')
			assert 20 < age < 100 , 'age at 20 ~ 100'
		except AssertionError as e:
			print('age is error')






