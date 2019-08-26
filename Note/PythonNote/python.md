
	线程池及其原理和使用
		当启动新线程的时，使用线程池可提升性能 。线程池在系统启动时即创建大量空闲的线程。
		线程池的使用：
			基类是concurrent.futures模块中的Executor。提供两个子类，即 ThreadPoolExecutor 和 ProcessPoolExecutor。 ThreadPollExecutor 用于创建线程池，ProcessPoolExecutor创建进程池
			Executor提供的常用方法：
				submit(fn,args,**kwargs): 将fn函数提交给线程池， *args 代表传给fn函数的参数，*kwargs 代表以关键字参数的形式给fn函数传入参数
				map(func,*iterables,timeout=None,chunksize=1):类全局函数
				map(func,*iterables)，该函数加你个启动多个线程，以异步方式立即对iterables执行map处理
				shotdown(wait=True): 关闭线程池
			submit方法返回Future对象，Future 提供的方法
				cancel()：取消该Future代表的线程任务，如任务正在执行，不可取消，返回False
				cancelled ：返回线程任务是否被成功取消
				running ： 如正在执行，不可取消，返回False
				done ；如任务被成功取消，返回True
				result(timeout=None) : 获取线程返回的结果，如任务还未完成，该方法会阻塞当前线程，timeout指定组赛的秒数
				exception(timeout=None):任务引发的异常，如任务成功完成，没异常，则返回None
				add_done_callback(fn):为该Future 的线程注册一个 回调函数，任务完成，自动出发fn函数。
		使用线程池执行线程任务的步骤：
				1. 调用ThreadPoolExecutor 类的构造器创建一个线程池
				2. 定义一个普通函数作为线程任务
				3. 调用ThreadPoolExecutor对象的submi方法来提交线程任务
				4. 调用ThreadPoolExecutor对象的shutdown方法来关闭线程池
					from concurrent.futures import ThreadPoolExecutor
					import threading
					import time
					
					def action(max):
						sum = 0
						for i in range(max):
							print(threading.current_therad().name() + ' ' + str(i))
							sum += i
						return sum
					pool = ThreadPoolExecutor(max_workers=2)
					future1 = pool.submit(action,50)
					future2 = pool.submit(action,100)
					print(future1.done())
					time.sleep(3)
					print(future2.done())
					print(future1.result())
					pool.shutdown()
		获取执行结果
			1.调用result方法获取线程任务的返回值。
			2.通过Future的add_done_callback()方法添加回调函数
			  线程池实现了上下文管理协议Context Manage Protocol，程序可用with语句来管理线程池，避免手动关闭线程池
			  map方法会为iterables的每个元素启动一个线程，以并发方式执行func函数，相当于启动len(iterables)个线程，并收集每个线程的执行结果。
		threading local函数：返回线程局部变量
				threding 提供local函数，可返回一个线程局部变量，使用线程局部变量可很简捷隔离多线程访问的竞争资源。
				线程局部变量Thread local Variable，为每个使用该变量的线程提供一个变量的副本，
		线程局部变量的作用：
			import threading
			from concurrent.futures import ThreadPoolExecutor
			data = threading.local()
			def action(max):
				for i in range(max):
					try:
						data.x += i
					except:
						data.x = i
					print(" data %d" % (threading.current_thread().name,data.x)) 
			with ThreadPoolExecutor(max_workers=2) as pool:
				pool.submit(action,10)
				pool.submit(action,10)

	Timer 定时器：控制函数在特定时间执行
		Thread类的子类Timer，可用于控制指定函数在特定时间内执行一次，
			from threading import Timer
			def hi():
				print('hi')
			t = Timer(10.0, hi)
			t.start()
		取消Timer的调度 cancel 函数

	schedule 任务调度及用法
		如需执行更复杂的任务调度，使用sched模块，提供了 sched.scheduler类，该类代表一个任务调度器
		sched.scheduler(timefunc=time.monotonic,delayfunc=time.sleep) 构造器支持两个参数：
			1. timefunc : 指定生成时间戳的时间函数，默认使用time.monotonic 生成时间戳
			2. delayfunc; 指定阻塞程序的函数，默认使用 time.sleep 函数阻塞程序
			[More](http://c.biancheng.net/view/2630.html)
		sched.scheduler 调度器常用属性和方法：
			scheduler.enterabs(time,priority,action,argument=(),kwargs={}): 指定time时间点执行action函数，argument 和 kwargs 用于向 action函数传入参数，arg...使用位置的形式传入参数。 kwargs 使用关键字传入参数
		scheduler.enter(delay,priority,action, argument=(),kwargs={}): delay 指定多少秒后执行action任务。作用同上
		scheduler.cancel(event): 取消任务
		scheduler.empty(): 判断调度器队列是否为空
		scheduler.run(blocking=True): 运行所有需要调度的任务
		scheduler.queue： 只读属性返回该调度器的调度队列
			import sched,time
			improt threading
			s = sched.scheduler()
			def print_time(name='default'):
				print(' %$ de time %s' % (name,time.ctime()))
			print('master threading time', time.ctime())
			s.enter(10,1,print_time)
			s.enter(3,2,print_time,argument=('wei zhi hanshu '))
			s.enter(5,2,print_time,kwargs=['name':'guanjianzi hanshu '])
			s.run()
			print('master ', time.ctime())

	os.fork方法：创建新进程
		多进程实现并发编程
		fork 方法作用： 程序会启动两个进程(一个主进程，一个fork出来的子进程)来执行从os.fork() 开始的所有代码
			fork方法不需要函数,有返回值表明哪个进程在执行:
				1. 如果fork返回0， 表明fork出来的子进程在执行
				2. 如fork返回非0， 表明父进程在执行，返回fork出来的子进程的进程ID
					import os
					print('master %s ' % os.getpid())
					pid = os.fork()
					print('worker in %s ' % os.getpid())
					if pid == 0:
						print('origin id  %s  master  id %s' % (os.getpid(),os.getppid()))
					else:
						print('me %s makr son id %s' % (os.getpid(),pid))
					print('thread over %s ' % os.getpid())

	Process 创建进程的2种方法
		1. 指定函数作为target ，创建Process对象即可创建新进程
		2. 继承Process 类，重写run方法来创建进程类，创建process子类的实例作为进程
		Process 类的属性和方法：
			1. run() : 实现进程的执行体
			2. start ： 启动进程
			3. join([timeout]) ： 类线程的join方法
			4. name ： 设置和访问进程的名字
			5. is_alive ：判断进程是否活着
			6. daemon ： 判断是否设置进程的后台状态
			7. pid ： 返回进程的ID
			8. authkey ：返回进程的授权key
			9. terminate ： 中断该进程
		以指定函数作为target 创建新进程
				import multiprocessing
				import os
				def action(max):
					for i in range(max):
						print('%s subprocess paterprocess %s  id %d ' % (os.getpid(),os.getppid(), i))
				if __name__ == '__main__':
					for i in range(100):
						print('parent %s id %d' % (os.getpid(), i))
						if i == 20:
							mp1 = multiprocessing.Process(target=action,args=(100,))
							mp1.start()
							mp2 = multiprocessing.Process(target=action,args=(100,))
							mp2.start()
							mp2.join()
					print('master process is ok')

		继承Process 类 创建子进程
			步骤：
				1. 定义继承Process 的子类，重写run方法准备作为进程执行提
				2. 创建Process 子类的实例
				3. 调用 Process 子类的实例的start方法来启动进程
					import multiprocessing
					import os
					class MyProcess(multiprocessing.Process):
						def __init__(self,max):
							self.max = max
							super().__init__()
						def run(self):
							for i in range(self.max):
								print('%s subprocess %s parent process %d ' % (os.getpid(),os.getppid(),i))
					if __name__ == '__main__':
					   for i in range(100):
						    print('%s master process %d ' % (os.getpid(),i))
							if i == 20:
								mp1 = MyProcess(100)
								mp1.start()
								mp2 = MyProcess(100)
								mp2.start()
								mp2.join()
						print('master process is ok!')
						
	设置进程启动的3种方式
		1. spawn ：父进程启动解释器进程，子进程继承run方法所需的资源。不必要的文件描述和handler都不被继承，效率比fork或forkserver方式要低得多。 Windows 只支持spawn方式
		2. fork： 通过os.fork 启动解释器， 子进程继承父进程所有资源，子进程等效于父进程
		3. forkserver ： 启动一个服务器进程，当再次启动新进程，父进程会连接到该服务器进程。请求由服务器进程来fork新进程
		multiprocessing 模块提供set_start_method 函数，用于设置启动进程的方式，必须将这行设置代码放在所有与多进程相关代码之前。 
		if __name__ == '__main__':
			multiprocessing.set_start_method('spawn')
			q = multiprocessing.Queue()
			mp = multiprocessing.Process(target=foo,args=(q,))
			mp.start()
			print(q.get())
			mp.join()
	
	多进程和多线程优缺点
		都使用并行机制提升系统运行效率，区别在于运行时所占内存分布不同，多线程共用一套内存的代码块区间，而多进程是各用一套独立的内存区间
		多进程有点在于 稳定性好，一个子进程奔溃，不影响主进程和其余进程，此特性多用多进程来实现守护服务器的功能
		多进程创建进程的代价非常大，操作系统会给每个进程分配固定的资源，会对进程的总数有一点的限制。
		多线程效率高 ，用于批处理任务等功能。 不足：一个线程奔溃整个进程奔溃。
		场景： 计算密集型的任务，多线程效率更高。 IO密集型的任务，如文件操作，网络爬虫，采用多线程
		IO密集型操作，消耗时间是等待时间，Python会释放GIL供新的线程使用，实现线程间的切换。	将多进程程序分布运行在不同的计算机上协同工作，每一进程内部，由多个线程并行工作
		最佳线程数量 = ()(线程等待时间+线程CPU时间) / 线程CPU时间) * CPU数量
	
	使用进程池管理进程
		如需启动多个进程，可使用进程池管理进程，程序可通过multiprocess模块的pool函数创建进程池： multiprocessing.pool.Pool类
		进程池常用方法：
			1. apply(func[,args[,kwds]]) : 将func函数提交给进程池处理，args 传给func的位置参数， kwds代表传给func的关键字参数，会被阻塞直到func函数执行完成
			2. apply_async(func[,args[,kwds[,callback[,error_callback]]]]): 异步，不被阻塞。callback指定func函数完成后的回调函数，error_callback 指定fun指定回调函数
			3. map(func,iterable[,chunksize]) : 类python的map全局函数，使用新进程对iterable的每个元素执行func函数
			4. imap(func,iterable[,chunksize]): map方法的延迟版本
			5. imap_unordered(func,iterable[,chunksize]):类imap，不保证元素顺序一致
			6. starmap(func,iterable[,chunksize]): 类map方法，要求iterable的元素是iterable对象，
			7. close ： 关闭进程池，不再接收新任务，把进程池中的所有任务执行完后再关闭自己
			8. terminate ： 立即中止进程池
			9. join ： 等待所有进程完成
			import multiprocessing
			import time
			import os
			def action(name='default'):
				print('%s process param %s ' % (os.getpid(),name))
				time.sleep(3)
			if __name__ == '__main__':
				pool = multiprocessing.Pool(processes=4)
				pool.apply_async(action)
				pool.apply_async(actino,args=('location parame:',))
				pool.apply_async(action,kwds={'name':'kwords params'})
				pool.join()
			线程池同样实现上下文管理协议，可使用with子句来管理进程池，避免程序主动关闭进程池
				import multiprocessing
				import time
				import os
				def action(max):
					sum = 0
					for i in range(max):
						print('%s %d ' % (os.getpid(),i))
						sum += i
					return sum
				if __name__ == '__main__':
					with multiprocessing.Pool(processes=4) as pool:
						results = pool.map(action,(50,100,200))
						print('---')
						for r in results:
							print(r)
				
	进程间通信的2种实现方法 Queue Pipe
		进程通信提供的2种机制：
			1. Queue ： 一个进程向Queue中放入数据，另一个进程从Queue中读取数据
			2. Pipe ： Pipe代表连接两个进程的管道，程序可调用Pipe函数时会产生两个连接段，分别交给两个进程，进程可从连接端读取数据，也可向该连接端写入数据
		使用Queeu实现进程间通信
			multiprocessing 模块下的Queue和queue 模块下的Queue类似，都提供qsize 、empyt、full、put、put_nowwait、get、get_nowait 等方法，区别： multiprecessing 模块下的Queue为进程提供服务， 而queue模块下的Queue为线程提供服务
			import multiprecessing
			def f(q):
				print('%s ' % multiprocessing.current_process().pid)
				q.quit('Python')
			if __name__ == '__main__':
				q = multiprocessing.Queue()
				p = multiprocessing.Process(target=f,args=(q,))
				p.start()
				print('%s ' % multiprocessing.current_process().pid)
				print(q.get())
				p.join
				
	使用Pipe实现进程间通信
		程序调用 multiprocessing.Pipe() 创建一个管道，返回两个PipeConnection对象，代表管道的两个连接端，一个管道有两个连接端，分别用于连接通信的两个进程
		PipeConnection对象包含的常用方法：
			1. send(obj) : 发送一个obj给管道的另一端，另一端使用 recv方法接收， 该obj需是可picklable的python序列化机制，如该对象序列化超过32MB，可引发ValueError异常
			2. recv ：接收另一端通过send方法发送过来的数据
			3. fileno：关于连接所使用的问价描述器
			4. close ： 关闭连接
			5. poll([timeout]):返回连接中是否有数据可读取
			6. send_types(buffer[,offset[,size]]: 发送字节数据，使用recv_bytes 或 recv_bytes_into 方法接收
			7. recv_bytes([maxlength])):通过send_bytes方法发送的数据，maxlength指定最多接收的字节数，返回接收到的字节数据
			8. recv_bytes_into(buffer[,offset]): 类recv_bytes方法，将接收到的数据放在buffer中
				import multiprocessing
				def f(conn):
					print('%s ' % multiprocessing.current_process().pid)
					conn.send('Python')
				if __name__ == '__main__':
					parent_conn,child_conn = multiprocessing.Pipe()
					p = multiprocessing.Process(target=f, args=(child_conn,))
					p.start()
					print('%s get data' % multiprocessing.current_process().pid)
					print(parent_conn.recv())
					p.join()




## 网络编程
	计算机网路的功能：
		1. 资源共享
		2. 信息传输与集中处理
		3. 均衡负荷与分布处理
		4. 总和信息服务
	常见的类型有： 局域网LAN、城域网MAN、广域网WAN。
	通信协议：负责对传输速率、传输代码、代码结构、传输控制步骤、出错控制等指定处理标准。
		通信协议由三部分组成：
			1. 语义： 决定双方对话的类型
			2. 语法： 决定双方对话的格式
			3. 交换： 决定通信双方的应答关系
			OSI ： Open System Interconnection ：将网络简化，以模块化的方式来设计网络
			OSI七层： 物理层、链路层、网络层、传输层、会话层、表示层、应用层。
		通信协议：是网络通信的基础，IP：Internet Protocol 称为 网际协议，支持网间互联的数据报协议，提供来网间连接的完善功能。TCP：Transmission Control Protocol，传输控制协议，规定一种可靠的数据信息传送服务，可单独使用，功能是互补的，两个协议统称为 TCP/IP 协议
	IP地址和端口号
		IP地址用于唯一标识网络中的一个通信实体。 IP地址是数字型，是一额32位整数
		NIC：Internet Network Information Center ： 统一负责全球IP地址的规划和管理，分为 InterNIC、APNIC、RIPE 三个网络信息中心负责IP地址分配。亚太地区通过APNIC，总部设在日本东京大学
		IP地址分为 A、B、C、D、E五类。每个类别的网络标识和主机标识各有规则：
			1. A 类： 10.0.0.0 ～ 10.255.255.255
			2. B 类： 172.16.0.0 ～ 172.31.255.255
			3. C 类： 192.168.0.0 ～ 192.168.255.255
			IP地址是一个通信实体，每个通信实体可有多个通信程序同时提供网络服务，还需提供使用端口
			端口：是一个16位整数，用于将数据交给哪个通信程序处理。端口是应用程序与外界交流的出入口，是一种抽象的软件结构，包括数据结构和 I/O 缓冲区
			端口分为三类：
				1. 公认端口(Well Known Port): 端口号为 0～1023，绑定特定的服务
				2. 注册端口(Registered Port): 端口号为 1024～49151
				3. 动态和/或私有端口(Dynamic and / or Private Port): 端口号为 49152～65535，是应用程序使用的动态端口
	
	网络编程模块
		网络模型大致分为四层，各有对应的网络协议提供支持
			1. 网络接口层： LAN、MAN、WAN
			2. 网络层： ICMP、IGMP、IP、ARP、RARP
			3. 传输层： TCP、UDP
			4. 应用层： SMTP、FTP、DNS、SNMP、NFS、HTTP、TELNET
		网络层协议主要是IP，是互联网协议的基础，ICMP、IGMP、ARP、RARP等协议是IP协议族的子协议，很少直接基于网络层进行应用程序编程
		Python标准库中的网络相关模块
			socket ： 基于传输层TCP、UDP协议进行网络编程的模块
			asyncore ： socket 模块的异步版，支持基于传输层协议的异步通信
			asynchat ： asyncore 的增强版
			cgi ： 基于CGI：Common Gateway Interface，早期动态网站的技术支持
			email ： E-mail 和MIME消息处理模块
			ftplib ： 支持FTP协议的客户端模块
			httplib、http.client ： 支持HTTP协议以及HTTP客户端的模块
			imaplib ： 支持IMAP4协议的客户端模块
			mailbox ： 操作不同格式邮箱的模块
			mailcap ： 支持Mailcap文件
			nntplib ： NTTP协议
			smtplib ： SMTP 协议，发送邮件的客户端模块
			poplib ： 支持POP3协议
			telnetlib ： 支持TELNET 协议
			urllib及其子模块： 支持URL处理的模块
			xmlrpc、xmlrpc.server、xmlrpc.client ：支持XML-RPC协议的服务和客户端模块
	
	urllib.parset 模块：
		URL：Uniform Resource Locator 对象代表统一资源定位器，指向互联网资源的指针。资源可以是文件、目录、或复杂对象的引用。 URL可由协议名、主机、端口和资源路径组成
			protocol://host:port/path
			1. urllib.request:最核心的子模块，包含打开和读取URL的各种函数
			2. urllib.error ： 包含urllib.request 子模块所引发的各种异常
			3. urllib.parset ： 解析URL
			4. urllib.robotparset ： 解析robots.txt 文件
			通过使用urllib模块可打开任意URl所指向的资源，可完整下载远程页面，与re模块结合使用，可提取页面中的各种信息，即网络爬虫的初步原理
				urllib.parse 子模块中用于解析URL地址和查询字符串的函数：
					1. urllib.parse.urlparset(urlstring,scheme=",allow_fragments=True"):解析URL字符串，返回ParseResult 对象，获取解析出的数据
					2. urllib.parse.urlunparse(parts): 是上一函数的反向操作，解析结果反向拼接URL地址
					3. urllib,parse.parse_qs(qs,keep_blank_values=False,strict_parsing=False,encoding='utf-8',errors='replace'):解析查询字符串(application/x-www-forn--=urlencoded 类型的数据)，以dict形式返回解析结果
																											4. urllib.parse.urlencode(query,deseq=False,safe='',encoding=None,errors=None,quote_via=quote_plus): 将字典形式或列表形式的请求参数恢复成请求字符串。相当与parse_qs、parse_qsl 的逆函数
																																																	5. urllin.parse.urljoin(base,url,allow_fragments=True): 将一个base_url和另一个资源URL连接成代表绝对地址的URl
					from urllib.parse import *
					result = urlparse('https://www.baidu.com')
					print(result)
					print('scheme:', result.scheme,result[0])
					print('hostname and port:', result.netloc,result[1])
					...
					print(result.geturl())
			ParseResult 各属性与元组索引的对应关系
					scheme		0		返回URL的scheme				scheme参数
					netloc		1		网络位置部分主机名和端口	空字符串
					path		2		资源路径					空字符串
					params		3		资源路径的附加参数	
					query		4		查询字符串
					fragment	5		Fragment标识符
					username			用户名						None
					password			密码
					hostname			主机名
					port				端口						None
			urlunparse ： 把一个 ParseResult 对象或元组恢复成URL字符串
			result = urlunparse(('http','www.baidu.com:80','index.php','text','name=hale',frag))
			print(result)
				parse_qs() parse_qsl() ： l代表list，用于解析查询字符串，返回值不同，
			urljoin 负责将两个URL拼接在一起，返回代表绝对值的URL，可出现三种情况：
				1. URL只是一个相对路径path
				2. 被拼接的URl是一个根路径path
				3. URL是一个绝对的path
	
	urllib.requset 模块读取资源用法
		urllib.request.urlopen(url,data=None)：用于打开url指定的资源，并从中读取数据，根据url的不同，返回值发生变化，如url是一个HTTP地址，该方法返回一个http.client.HTTPResponse对象
		from urllib.request import *
		// 打开URL对应的资源
		result = urlopen('http://www.baidu.com/index.php')
		// 按字节读取数据
		data = result.read(333)
		// 将字节数据恢复成字符串
		print(data.decode('utf-8'))
		// 用context manager 管理打开的URL资源
		with urlopen('http://www.baidu.com/index.php') as f:
			// 按字节读取数据
			data = f.read(333)
			// 将字节数据恢复成字符串
			print(data.decode('utf-8'))
		
		使用urlopen函数时，可通过data属性向被请求的URL发送数据：
			from urllib.request import * 
			with urlopen(url='https://www.baidu.com/index.php',data='test'.encode('utf-8')) as f:
				print(f.read().decode('utf-8'))
		通过urlopen 函数发送POST请求参数，可通过data 属性来实现：
			import urllib.parse
			params = urllib.parse.urlencode({'name':'hale','password':'password'})
			params = params.encode('utf-8')
			with urlopen('https://www.baidu.com/index.php',data=params) as f:
				print(f.read().decode('utf-8'))
		urllib.request.Request对象的构造函器：
			urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None)
				Request 可通过method指定请求方法，也可通过data指定请求方法，可通过 headers 指定请求头
				from urllib.request import *
				params = 'put request'.encode('utf-8')
				req = Request(url='https://www.baidu.com/index.php',data=params,method='PUT') 
				with urlopen(req) as f:
					print(f.status)
					print(f.read().decode('utf-8'))
		使用Request对象添加请求头
			// 创建Request对象
			req = Request('https://www.baidu.com/index.php')
			// 添加请求头
			req.add_header('Referer','https://www.baidu.com')
			with urlopen(req) as f:
				print(f.status)
				print(f.read().decode('utf-8'))
			通过Request 的add_header 方法添加一个Referer 请求头，
		实现多线程下载的步骤：
			from urllib.request import * 
			import threading
			class DownUtil:
					def __init__(self,path,target_file,thread_num):
						self.path = path
						self.thread_num = thread_rum 
						self.threads = []
					def download(self):
						req = Request(url=self.path,method='GET')
						...


			1. 使用 urlopen 方法打开远程资源
			2. 获取指定的URL对象所指向资源的大小，通过Content-Length响应头获取
			3. 计算每个线程应该下载网络资源的哪个部分，从哪个节点开始，到哪个字节结束
			4. 依次创建并启动多个线程
				from DownUtil import * 
				du = DownUtil('https://www.baidu.com/' + 'from/logo.png','a.png',3)
				du.download()
				def show_process():
					print('ok : %.2f' % du.get_complete_rate())
					global t
					if du.get_complete_rate() < 1:
						t = threading.Timer(0.1,show_process)
				t = threading.Timer(0.1,show_process)
				t.start()

	http.cookiejar模块：管理cookie
		如使用urllib.request 模块来访问被保护页面，维修与服务器之间的sesion，借助于 cookie 管理器
		使用OpenerDirector 对象来发送请求，步骤：
			1. 创建 http.cookiejar.CookieJar 对象或其子类的对象
			2. 以CookieJar对象为参数，创建urllib.rquest.HTTPCookieProcessor对象，该对象负责调用CookieJar来管理cookie
			3. 以HTTPCookieProcessor对象为参数，调用urllib.reques.build_opener()函数创建OpenerDirector对象
			4. 使用OpenerDirector对象来发送请求，通过HTTPCookieProcessor调用CookieJar管理cookie
			[More](http://c.biancheng.net/view/2646.html)

	TCP协议、IP协议的关系
		TCP/IP通信协议是可靠的网络协议，在通信的两端各建立一个socket，形成虚拟的网络链路，建立虚拟的网络链路，两端的程序可通过该链路进行通信。 使用socket对象来代表两端的通信端口并通过socket进行网络通信
		IP是Internet 的关键协议，全称：Internet Protocol，即Internet协议，简称：IP协议。IP协议负责将消息从一个主机传送到另一个主机，信息被分割成一个个小包
		TCP：端对端协议，TCP协议让他们之间建立一个虚拟链路，用于发送和接收数据
		TCP协议负责收集数据包，并按照顺序传送，接收端接收到数据包后再将其正确地还原。TCP协议保证数据包传送无误，采用重发机制，即当一个通信实体发送一个消息给另一个通信实体后，需要接收到的另一个通信实体的确认信息，如没有收到确认信息，则会重发信息
		只有把TCP和IP两个协议结合，才能保证Internet在复杂的环境下正常运行。
	
###	socket 建立TCP连接
	在使用socket之前，须建立socket对象，通过该类的构造器来创建socket实例：
		socket.socket(family=AF_INET,type=SOCK_STREAM, proto=0,fileno=None)
			1.family 参数用于指定网络类型，socket.AF_UNIX：UNIX网络、socket.AF_INET 基于IPv4协议的网络 和socket.AF_INET6 基于IPv6协议的网络 这三个变量
			2. type参数用于指定网络的Sock类型，支持SOCK_STREAM默认值，创建基于TCP协议的socket、SOCK_DGRAM 创建基于UDP协议的socket 和SOCK_RAW 创建原始socket。常用 SOCK_STREAM和SOCK_DGRAM
			3. proto参数用于指定协议号， 默认0，可忽略
			socket 对象提供的常用方法：
				1. socket.accept： 作为服务端使用的socket调用该方法接收来自客户端的连接
				2. socket.bind(address)：将该socket绑定到指定address，address可是一个元组，包含IP地址和端口
				3. socket.close ： 关闭连接，回收资源
				4. socket.connect(address): 连接远程服务器
				5. socket.connect_ex(address): 当程序出错时，不抛出异常，返回错误标识符
				6. socket.listen([backlog]): 服务器使用socket调用该方法进行监听
				7. socket.makefile(mode='r',buffering=None,*,encoding=None,errors=None,newline=None): 创建和该socket关联的文件对象
																					
				8. socket.recv(bufsize[,flags]): 返回值是(bytes,address)元组
				9. socket.recvmsg(bufsize[,ancbufsize[,flags]]): 不仅接收来自socket的数据，还接收来自socket的辅助数据，返回值是一个长度为4的元组(data.ancdata,msg_flags,address).
				10. socket.recvmg_into(butters[,nbytes[,flags]]):类socket.recvmsg ，将接收的数据放入buffers中
				11. socket.recvfrom_into(buffer[,nbytes[,flags]]):将接收到的数据放入buffer中
				12. socket.recv_into([buffer[,nbytes[,flags]]]): 类recv方法，将接收到的数据放入buffer中
				13. socket.send(bytes[,flags]): 向socket发送数据，该socket必须与远程socket建立连接，基于TCP协议的网络中发送数据
				14. socket.sendto(bytes,addresss)：向socket发送数据，没有与远程socket连接，基于UDP协议发送数据
				15. socket.sendfile(file,offset=0,count=None):将整个文件内容发送出去，直到遇到EOF
				16. socket.shutdown(how):关闭连接，how用于设置关闭方法
		TCP通信的服务器端编程的基本步骤：
			1. 服务器端先创建一个socket对象
			2. 服务器端socket将自己绑定到指定IP地址和端口
			3. 服务器端socket调用listen 方法监听网络
			4. 程序采用循环不断调用socket 的accept方法接收来自客户端的连接
				// 创建socket对象
				s = socket.socket()
				// 将socket 绑定到本机IP地址和端口
				s.bind('192.168.0.123',8888)
				// 服务器开始监听客户端的连接
				s.listen()
				while True:
					c,addr = s.accept()
		客户端先创建一个socket对象，将该socket绑定到指定的ip地址和端口号，然后调用connect方法建立与服务器的连接，就可建立一个基于TCP协议的网络连接
			TCP通信的客户端的基本步骤如下：
				1. 客户端先创建一个socket对象
				2. 客户端socket调用connect方法连接到远程服务器
		socket提供大量方法发送和接收数据：
			1. 发送数据：使用send方法，注意：sendto方法用于UDP协议的通信
			2. 接收数据：使用recv_xxx方法
				import socket
				s = socket.socket()
				s.bind(('192.168.1.88',999))
				s.listen()
				while True:
					c, addr = s.accept()
					print(c)
					print('connect addrss', addr)
					c.send('himessge '.encode('utf-8'))
					c.close()
		从socket中获取服务器发送的数据
			import socket
			s = socket.socket()
			s.connect(('192.168.1.88',999))
			print('--%s--'s.recv(1024).decode('utf-8'))
			s.close()



