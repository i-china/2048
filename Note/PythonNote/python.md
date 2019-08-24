
	fileinput模块：逐行读取多个文件
		把多个输入流合并在一起
			fileinput.input (files = "filename1,filenamex,...",inplace=False,backup=",bufsize=0,mode='r',openhook=None")
				files ：多个文件的路径列表
				inplace ： 指定是否将标准输出的结果写回到文件，默认值为 False
				backup ： 指定备份文件的扩展名
				bufsize ： 指定缓存区的大小，默认0
				mode ： 打开文件的格式，默认 r
				openhook ： 控制文件的打开方式，如编码格式
		fileinput 模块常用函数
			fileinput.filename() ：返回读取文件的文件名
			fileinput.fileno() ：返回文件描述
			fileinput.lineno() ：返回读取的行号
			fileinput.filelineno() ：返回读取的行在文件中的行号
			fileinput.isfirstline() ： 读取的行在文件中是否为第一行
			fileinput.isstdin() ： 是否从sys.stdin 读取
			fileinput.nextfile() ： 关闭当前文件，开始读取下一个文件
			fileinput.close() ： 关闭fileinput对象

	linecache模块：随机读取文件指定行
		从源文件随机读取指定行，并在内部使用缓存优化存储，会使用utf-8字符集
			常用函数：
				linecache.getline(filename,lineno,module_globals=None)：读取指定模块中指定文件的指定行，filename指定文件名，lineno指定行号
				linecache,clearcache() ：清空缓存
				linecache.checkcache(filename=None) ：检查缓存是否有效，如没有指定文件名filename参数，默认检查所有缓存的数据

	pathlib模块
		提供了一组面向对象的类，代表各种操作系统上的路径
		PuraPath 的两个子类： PurePosixPath:Unix风格的路径  PureWindowsPath：Windows风格的路径
	PurePath ：使用此函数或他的子类来创建PurePath对象，创建时，可闯入单个路径字符串，也可传入多个路径字符串
	PurePath类的属性和方法：
		操作路径字符串，[](http://c.biancheng.net/view/2541.html)	
	Path类功能和用法：
		Path 是PurePath的子类，可访问底层的文件系统，判断Path对应的路径是否存在，可对文件进行读写

	os.path 模块函数
		操作目录的方法，可操作系统的目录本身，如 exists():判断目录是否存在, getctime()：创建时间 getmtime()：修改时间  getatime()：访问时间  getsize()：文件大小
	
	fnmatch模块：文件名的匹配
		匹配支持的通配符：
			* ： 匹配任意个任意字符
			? ： 匹配一个任意字符
			[字符序列] ：匹配中括号里字符序列中的任意字符，
			[!字符序列] ： 匹配不在中括号里字符序列中的任意字符
		fnmatch.fnmatch(filename,pattern)：判断指定文件名是否匹配指定pattern
		fnmatch.fnmatchcase(filename,pattern)：匹配时不区分大小写
		fnmatch.filter(names,pattern) ：对names列表进行过滤，返回names列表中匹配pattern的文件名组成的子集合。 
		fnmatch.translate(patteran)：将Unix shell风格的pattern转换为正则表达式pattern

	os模块：
		os模块与目录相关的函数：
			os.getcwd()：获取当前目录
			os.chdir(path) ： 改变当前目录
			os.fchdir(fd) ：通过文件描述改变当前目录
			os.chroot(path)：改变当前进程的根目录
			os.listdir(path)：返回paht对应目录下的所有文件和子目录
			os.mkdir(path[,mode])：创建path对应的目录，mode指定目录的权限
			os.makedirs(path[,mode])：类似mkdir ，可递归创建目录，
			os.rmdir(path)：删除path对应的空目录，如非空抛出 OSError异常，可先用os.remove()删除文件
			os.removedirs(path) ：递归删除目录，类似rmdir
			os.rename(src,dst)：重命名文件或目录，将src命名为dst
			os.renames(old,new) ：对文件或目录进行递归重命名，类rename，

	os模块与权限相关的函数
		os.access(path,mode)：检查path对应的文件或目录是否具有指定权限，第二参数的四个状态
			os.F_OK ： 判断是否存在
			os.R_OK ： 是否可读
			os.W_OK ： 是否可写
			os.X_OK ： 是否可执行
		os.chrnod(path,mode) :更改权限，
			stat.S_IXOTH ：其他用户有执行权限
			[更多](http://c.biancheng.net/view/2558.html)			
		os.chown(path,uid,gid) ：更改文件的所有值，uid代表用户id，gid代表组id
		os.fchmod(fd,mode) ：改变一个文件的访问权限，fd代表文件
		os.fchown(fd,uid,gid) ：改变文件的所有者''

	os模块与文件访问函数
		os.open(file,flags[,mode]) ：打开一个文件，设置打开选项，flags表示打开文件的旗标
	，支持多个选项
			os.O_RDONLY ： 只读方式打开
			os.O_WRONLY ： 只写方式
			os.O_RDWR ： 读写方式
			os.O_NONBLOCK ： 打开时不阻塞
			os.O_APPEND ： 追加方式打开
			os.O_CREAT ；创建并打开一个新文件
			[更多](http://c.biancheng.net/view/2558.html)
		os.read(fd,n) ：从文件描述符fd中读取最多n个字符，返回读到的字符串
		os.wirte(fd,str) ：将字符串写入文件描述符fd，返回写入的字符串长度
		os.close(fd) : 关闭文件描述符fd
		os.lseek(fd,pos,how) ： 用于移动文件指针，how指定从哪里开始移动，
		os.fdopen(fd[,mode[,bufsize]]) ：通过fd打开，返回文件对象
		os.closerange(fd_low,fd_high) : 关闭从fd_low 包含 到 fd_high 不包含范围的所有文件描述符
		os.dup(fd) ： 复制文件描述符
		os.dup2(fd,fd2) ： 讲一个fd 复制到另一个文件描述符 fd2中
		os.ftruncate(fd,length) ： 将fd对应的文件截断到length长度，length参数不超文件大小
		os.remove(path) ：删除path对应的文件
		os.link(src,dst) ： 创建从src 到dst的硬连接
		os.symlink(src,dst) ：创建从src到dst的符号链接

	tempfile模块：生成临时文件和临时目录
		常用函数：
			tempfile.TemporaryFile(mode='w+b',buffering=None,encoding=None,newline=None,suffix=None,prefix=None,dir=None) ：创建临时文件，返回类文件对象，支持I/O
		[More](http://c.biancheng.net/view/2560.html)
			tempfile.gettempdir() : 获取系统临时目录
		创建临时文件的两种方式：
			1. 手动创建临时文件，读写临时文件后需主动关闭，程序关闭时文件自动删除
			2. 使用with语句创建临时文件，with语句自动关闭临时文件



## 数据库编程

### 数据库API(DB API)
	全局变量
		3个全局变量：
			1. apilevel ： 显示数据库模块的API版本号
			2. threadsafety ： 指定数据库模块的线程安全等级，等级值为 0～3，3代表模块完全是线程安全的，1:部分安全 ，0：  完全不能共享该模块
			3. paramstyle ： 指定SQL语句需要参数时，使用风格的参数，返回如下变量值：
				format ： 格式化字符串代表参数，使用 %s
				pyformat ： 使用扩展的格式代码代表参数
				qmark ： 使用 ？ 问号代表参数
				numeric ： 使用数字占位符 :N 代表参数，1 代表一个参数，2 也代表参数
				named ： 使用命名占位符 :name 代表参数

	数据库API的核心类
		连接对象的方法和属性
			cursor() ：			打开游标
			commit() ：			提交事物
			rollback()：		回滚事物
			close() ：			关闭数据库连接
			isolation_level:	返回或指定数据库连接中事物的隔离级别
			in_transaction:		判断当前是否处于事物中
	cursor ： 返回游标对象，游标对象是 Python DB API的核心对象，用于执行各种SQL语句，包括DDL、DML、select 查询语句等，使用游标执行不同的SQL语句返回不同的数据。
		游标对象的属性和方法：
			execute(sql[,parameters]) ： 执行SQL语句，parameters 参数用于为SQL语句中的参数指定值
			executemany(sql,seq_of_parameters) ：重复执行SQL语句，通过第二个参数指定值，序列有多少个元素，SQL语句被执行多少次
			executescript(sql_script) ：直接执行包含多条SQL语句的SQL脚本
			fetchone() : 获取查询结果集的下一行，如没有，则返回None
			fetchmany(size=cursor.arraysize) ：返回查询结果集的下N行组成的列表，如没有，返回空
			fetchall() : 返回查询结果集的全部行组成的列表
			close() : 关闭游标
			rowcount ： 只读属性返回受SQL语句影响的行数，修改的记录条数也可通过该属性获取
			lastrowid ：获取最后修改行的rowid
			arraysize ： 设置或获取fetchmany 默认获取的记录条数，默认为 1
			desciption ： 获取最后一次查询返回所有列的信息，只读
			connection ： 返回创建游标的数据库连接对象，属性只读

		操作数据库的基本流程
			1. 调用 connect 方法打开数据库连接，返回数据库连接对象
			2. 通过数据库连接对象打开游标
			3. 使用游标执行SQL语句 包括 DDL、DML、select查询语句，如执行的是查询语句，则处理查询数据
			4. 关闭游标
			5. 关闭数据库连接
			[图示](http://c.biancheng.net/uploads/allimg/190301/2-1Z301153400E3.gif)

	SQLite 创建数据库表
		是一种嵌入式数据库，数据库是一个文件，SQLite将整个数据库包括定义表、索引以及数据本身，作为一个单独的、可跨平台使用的文件存储在主机中。不需要安装。直接导入
		连接数据库：
			connect() 函数
				conn = sqlite3.connect('xx.db')		// xx.db 是一个数据库,如不存在，在当前目录下创建对应的文件
		创建数据库：
			import sqlite3
			conn = sqlite3.connect('xx.db ')
			c = conn.cursor()
			c.execute(''' create table user_tb(
				id interger primary key autoincrement,
				name text,
				pass text,
			gender text)'''
					)
			c.execute(''' create table post_tb
					id integer primary key autoincrement,
					post_name text,
					post_author text,
					post_number real,
					user_id integer,
					foreign key(user_id) references user_tb(id)''')
			c.close()
			conn.close()
		SQLite 支持 NULL、INTEGER、REAL浮点数、TEXT文本、BLOD大二进制对象
		
	SQLite execute 和 executemany 
		游标的execute 方法可执行DML 操纵语言 的 insert 、update、delete 语句，对数据库执行插入、修改和删除数据操作
		调用execute 方法执行insert 可向数据库插入数据
		向数据库插入一条数据：
			// 导入访问SQLite的模块
			import sqlite3
			// 打开或创建数据库， 可用 :memory: 代表创建内存中的数据库
			conn = sqlite3.connect('xx.db')			// xx.db 指创建时指定的数据库文件
			// 获取游标
			c = conn.cursor()
			//	调用执行 insert 语句插入数据
			c.execute('insert into user_tb values (null,?,?,?)', ('xxx','xxx','xxx'))
			c.execute('insert into xxx_tb values (null,?,?,?)' ('xx','xx','xx'))
			//	提交事物
			conn.commit()
			// 关闭游标
			c.close()
			// 关闭连接
			conn.close()
	 executemany ： 多次执行同一条SQl语句
			import sqlite3
			conn = sqlite3.connect('xx.db')
			c = conn.cursor()
			c.executemany('inert into xxx_tb values (null,?,?,?)',
				(	('xx','xxx','xxxx'),
					('aa','aaa','aaaa'),
					('bb','bbb','bbbb'),
					('zz','zzz','zzzz')
				))
			conn.commit()
			c.close()
			conn.close()
	update | delete
		import sqlite3
		conn = sqlite3.connect('xx.db')
		c = conn.cursor()
		c.execute(' update user_tb set xxx=? where xx=? ',
					(('aa',1),
					('bb',2)
				))
		print('change numbers : ', c.rowcount)
		conn.commit()
		c.close()
		conn.close()
	
	SQLite : fetchone() , fetchmany() and fetchall:
		select 语句执行查询结果， 通过游标的 fetchone 、fetchmany、fecthall获取查询结果，fetchone 获取一条，fetchmany 获取多条， fetchall 获取全部
		import sqlite3
		conn = sqlite3.connect('xx.db')
		c = conn.cursor()
		c.execute('select * from user_tb where xx > ?',(2,))
		print('result : ', c.rowcount)
		for col in (c.description):
			print([col[0],end'\t'])
		print('\n------')
		where True:
			row = c.fetchone()
			if not row:
				break
			print(row)
			print(row[1] + ' -> ' + row[2])
		c.close()
		conn.close()
	可修改部分代码：
		while True:
			// 指定抓起的条数记录，返回由条数组成的列表
			rows = c.fetchmany(3)
			//	判断rows是否为None
			if not row:
				break
			// 再次使用循环遍历获取的列表
			for r in rows:
				print(r)
		避免使用fetchall获取查询的全部记录，如数据量过大，会导致内存开销过大，导致系统崩溃！
		
	SQLite： executescript 
		可执行一段SQL脚本
			import sqlite3
			conn = sqlite3.connect('xx.db')
			c = conn.cursor()
			c.executescript('''
				insert into user_tb values (null,'aaa','aaa','aaaa'),
				insert into user_tb values (null,'bbb','bbb','bbbb'),
				create table item_tb (id integer primary key autoincrement, name, price)
			''')
			conn.commit()
			c.close()
			conn.close()
		简化： SQLite 提供了3个方法为数据库连接对象
			1.  execute(sql[,parameters]) : 执行一条SQL语句
			2. executemany(sql[, parameters]) : 根据序列重复执行SQL语句
			3. executescipt(sql_script) ： 执行SQL脚本
			只是游标对象的3个方法的快捷方式								 
	SQLite： create_function 方法： 注册自定义函数
		create_function 方法包含的三个参数：
			1. name ： 指定注册的自定义函数的名字
			2. num_params ： 指定自定义函数所需参数的个数
			3. func ： 指定自定义函数对应的函数
			为SQL语句注册一个自定义函数，可在SQL语句中使用该自定义函数
				import sqlite3
				def reverse_ext(st):
					return '[' + st[::-1] + ']'
				conn = sqlite3.connect('xx.db')			// xx.db 代表数据库文件
				conn.create_function('enc',reverse_ext)
				c = conn.cursor()
				c.execute('insert into user_tb values(null,?,enc(>),?)' ,
							('xx','xx','xxx'))
				conn.commit()
				c.close()
				conn.close()
	
	SQLite create_aggregate() : 自定以聚集函数
		SQL提供的5个聚集函数：
			1. sum() : 统计总和
			2. avg()  ：统计平均值
			3. count() ： 统计记录条数
			4. max() ： 统计最大数
			5. min() ： 统计最小数
	可使用数据库连接对象提供的 create_aggregate(name,num_params,aggregate_class)方法，用于注册一个自定义的聚集函数
			create_aggregate 方法包含3个方法：
					1. name ： 指定自定义聚集函数的名字
					2. num_params ： 指定聚集函数所需的参数
					3. aggregate_class ： 指定聚集函数的实现类，该类必须实现 step(self,pargams,..) 和 finalize(self) 方法，step方法返回每条记录各执行一次，finalize 方法只在最后执行一次，返回值作为聚集函数最后的返回值

	SQLite： create_collation ： 创建自定义比较函数
		create_collation(name, callable) 注册一个自定义的比较函数
			2个参数：
				1. name ： 指定自定义比较函数的名字
				2. callable ： 指定自定义比较函数对应的函数，包含两参数，对两个参数进行比较，如返回正整数，第一个参数更大，如是负整数，第二个参数更大，如返回0，则相等
				import sqlite3
				def my_collate(str1,str2):
					if st1[1:-1] == str2[1:-1]:
						return 0;
					elif ...
				conn = sqlite3.connect('xx.db')
				conn.creat_collation('sub_cmp',my_callate)
				c = conn.cursor()
				c.execute('seleft * from xxx_tb where field = ?', (1))
				for row in c:
					print(row)
				conn.commit()
				c.close
				conn.close()
				
	MySQL 数据库
		查看已安装的模块： pip list
						   pip show packagename
						   pip show mysql-connector-python
		卸载已安装的模块： pip uninstall packagename
		安装模块： pip install packagename
					pip install mysql-connector-python
					pip install packagename == 1.0	// 可指定版本
	
		MySQL 数据库执行DDL 语句
			import mysql.connector
			conn = mysql.connector.connect(user='root',password='root', host='127.0.0.1|localhost',post='3306', database='python',use_unicode=True)
			c = conn.cursor()
			c.execute('''	create table user_tb (
					user_id int primary key auto_increment,
					name varchar(100),
					pass varchar(200),
					gender varchar(100)
				)''')
			c.execute(''' create table order_tb (
				order_id int primary key auto_increment,
				item_name varchar(100),
				item_price double,
				item_number double,
				user_id  int,
				foreign key(user_id) reference user_tb(user_id)
			)''')
			c.close()
			conn.close()

	MySQL 数据库执行DML 语句
		可使用游标的execute 方法执行DML的 insert 、upadte、delete
			import mysql-connector
			conn = mysql-connector.connect(user='root',password='hale',host='localhost',port='3306',database='python',use_unicode=True)
			c = conn.cursor()
			c.execute('insert into user_tb values(null, %s,%s,$s)',('aa','aaa','aaaa'))
			c.executemany('insert into order_tb values (null,%s ,%s,%s,%s)', 
					(('a','aa','aaa'),('b','bb','bbb'),('c','cc','ccc')))
			conn.commit()
			c.close()
			conn.close()
		使用 %s 作为占位符
		update 
			c.executemany('update user_tb set name=%s where user_id = %s ', (('e','ee','eee'),('w','ww','www')))
			print('change : ', c.rowcount)
			conn.comm
		mysql数据库模块连接对象有一个 autocommit ，如属性设置为True ，则关闭连接的事物支持，每次执行DML语句后会自动提交，无需调用 commit 方法提交事物
			import mysql.connector 
			conn = mysql.connector.connect(user='root',password='hale',host='localhost',port='3306',database='python',use_unicode=True)
			conn.autocommit = True

	MySQL 数据库执行查询语句
		import mysql.connector
		conn = mysql.connector.connect(user='root',password='hale',host='localhost',port='3306',database='python',use_unicode=True)
		c = conn.cursor()
		c.execute('selecet * from user_tb where user_id > %s', (1,))	
		for col in (c.description):
			print(col[0],end='\t')
		print('\n -------')
		for row in c:
			print(row)
			print(row[1] + ' -> ' + row[2])
		c.close()
		conn.close()
		
		游标对象支持 fetchone() fetchmany() fetchall() 
		c.execute('select * from ueer_tb where user_id > %s',(1,))
		where True:
			rows = c.fetchmany(3)
			if not rows:
				break
			for r in rows:
				print(r)

	MySQl callproc : 调用数据库存储过程
		callproc(self,procname,args=0)
			procname : 代表存储过程的名字， args 参数用于存储过程传入参数
			result_args = c.callproc('add_pro',2,1,0)

	PyMySQl模块下载和安装
		类Connector/Python、PyMySQL ，称为接口程序，通过此对象，可对另外一个对象操作
		安装PyMySQL模块：
			pip install PyMySQL
				import pymysql
		
		import pymysql
		conn = pymysql.connect(host='localhost',root='root',password='pass',db='python',charset='utf8mb4')
		c = conn.cursor()
		c.execute('select  Version()')
		while True:
			rows = c.fetchmany(3):
				if not rows:
					break
				
				for i in rows:
					print(i)
		c.close()
		conn.close()
	创建数据库：	
		import pymysql
		conn = pymysql.connect('localhost','root','root','python')
		cursor = conn.cursor()
		cursor.execute('Drop table if exists tb_name')
		sql = ''' create table user_tb (
			user_id int primary key auto_increment,
			name varchar(100),
			email varchar(10),
			pass varchar(100)
		)'''
		cursor.execute(sql)
		cursor.close()
		conn.close()
	
	数据库插入操作
		import pymysql
		conn = pymysql.connect('localhost','root','root','py_db')
		cursor  = conn.cursor()
		sql = ''' insert into user_tb (name,pass) values ('%s','%s') % ('aa','aa')'''
		try: 
			cursor.execute(sql)
			conn.commit()
		except:
			conn.rollback()
		conn.close()



## 并发编程(多进程、多线程)

### 进程和线程 区别
	进程： 操作系统资源分配的基本单位，通常是一个程序
	线程： 任务调度和执行的基本单位，是进程的组成部分
		可运行多个进程(程序)，同一进程可多个线程同时执行(通过CPU调度，每个时间片中只有一个线程执行
	内存方面：进程分配不同的内存控件，线程不分配
	开销方面： 进程有独立的代码和数据空间程序上下文，进程切换开销大，线程是轻量级的进程，同一类线程共享代码和数据空间，有独立的运行栈和计数器，线程切换开销小
	
	单线程： 当一个进程中只有一个线程时
	多线程： 当一个进程中有多个线程时 

###	创建线程的两种方式：
	相关模块：
		1. _thread ： 提供低级别的原始的线程支持，及简单的锁，功能有限，不建议使用
		2. threading ： 提供丰富的多线程支持，推荐使用
	创建方式：
		1. 使用 threading 中的 Thread 类的构造器创建线程，直接对类 threding.Thread 进程实例化，并调用对象的 start 方法创建线程
		2. 继承 threading 模块中的 Thread 类创建线程类，用 threading.Theread 派生出一个新的子类， 将新建类实例化，并调用 start 方法创建线程
		
	 调用Thread 类的构造器创建线程：
		直接调用 threading.Thread 类构造器创建线程：
			__init__(self,gourp=None,target=None,name=None,args=(),kwargs=None,*,daemon=None)
				group: 指定该线程所属的线程组，
				target： 指定该线程要调度的目标方法
				args ： 指定一个元组，以位置参数形式为target 指定的函数传入参数，元组的第一个参数传给target函数的第一个参数，第二个传给target第二个参数，以此类推
				kwargs ：指定一个字典，以关键字参数的形式为target指定的函数传参
				daemon ： 指定所构建的线程是否为后代线程
		通过Thread 类的构造器创建并启动多线程的步骤：
			1. 调用Thread类的构造器创建线程对象，创建时，target参数指定的函数将作为线程执行体
			2. 调用线程对象的start() 方法启动该线程
				import threading
				// 定义普通的action函数，作为线程执行体
				def action(max):
					for i in range(max):
						print(threading.current_thred().getName() + " " + str(i))
				// 主程序、祝线程的执行体
				for i range(100):
					print(threading.current_thread().getName() + " " + str(i))
					if i == 20:
						t1 = threading.Thread(target=action,args=(100,))
						t1.start()
						t2 = threading.Thread(target=action,args=(100,))
						t2.start()
				print('master thread is run over !')
				1. 创建一个Thread对象，线程的target 为 action， 将action函数作为线程主体执行，接下来的程序调用start 来启动t1线程
				2. 再次创建线程，创建和启动与第一个线程完全相同
				显式创建并启动了两个线程，但实际上有三个，当程序运行后，至少创建一个主线程，主线程的线程执行代码就是程序中的主程序，没放在任何函数中的代码
					用到的函数和方法：
						threading.current_thread(): 是threading 模块的函数，总是返回当前正在执行的线程对象
						getName ：Thread类的实例方法，返回调用他的线程名字
					在Threading模块中，经常用到的函数：
						threading.enumerate() : 正运行线程的list
						threading.activeCount ： 返回正在运行的线程数量，与 len(threading.enumerate())

	继承Thread类创建线程类
		步骤：
			1. 定义Thread 类的子类，并重写run方法，run方法方法体代表线程需要完成的任务，因此 run方法称为 线程执行体
			2. 创建Thread 子类的实例，即创建线程对象
			3. 调用线程对象的start 方法来启动线程
				import threading
				class FKThread(threading.Thread):
					def __init__(self):
						threading.Thread.__init__(self)
						self.i = 0 
					def run(self):
						while self.i < 100:
							print(threading.current_thread().getName() + " " + str(self.i))
						self.i += 1
				for i in range(100):
					print(threading.current_thread().getName() + " " + str(i) )
					if i == 20:
						ft1 = FKThread()
						ft1.start()
						ft2 = FKThread()
						ft2.start()
				
				print('threading is ok !')
					



