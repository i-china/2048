## 文件操作I/O

	### 文件基本操作
		常见操作： 创建、删除、修改权限、读取、写入等
			1. 删除、修改权限：作用于文件本身，属于系统级操作
			2. 写入、读取： 文件常用操作，作用于文本的内容，属于应用级操作
		文件操作实现函数：
			1. 打开文件： open 函数，返回文本对象
			2. 对已打开的文件做读/写操作，读写，使用 read 、readline readlines 函数，写入：write 函数
			3. 关闭文件： close 

		open 函数：打开指定文件
			如要操作文件，需创建或者打开指定的文件，并创建一个文件对象，内置的 open 函数
				file = open(file_name [, mode [, buffering]]) 
					file: 表示要创建的文件对象
					file_mode ： 要创建或打开文件的文件名称，需用引号扩起来，注意路径
					mode ： 可选参数；指定文件的打开模式，如不写，默认只读r
					buffing ： 指定对文件做读写操作，是否使用缓存区
				open 函数文件打开模式：
					r ： 只读，指针在开头
					rb ： 二进制格式，只读模式，指针位于开头，用于打开非文本文件，如图片
					r+ ： 从头读取文件内容，从开头写入新的内容，新内容覆盖原有内容
					rb+ ： 二进制格式读写模式打开，针对非文本文件，如音频文件
					w ： 只读，清空文件原有内容
					wb ：二进制格式、只读模式，音频文件
					w+ ： 读写， 清空原有内容
					wb+ ： 二进制格式、读写模式，非文本
					a ：追加模式，只写权限，如文件不存在，则创建新文件
					a+ ： 读写，指针位于末尾，如不存在，则新建
					ab+ ： 二进制模式，追加模式，读写权限
		[读写操作](http://c.biancheng.net/uploads/allimg/190228/2-1Z22QI61c59.gif)
			open 打开文件时，默认GBK编码，指定打开文件的编码格式； 
				file = open('xx.txt',encoding="utf-8")
	
		open()是否需要缓冲区 
			一般建议打开缓冲，open函数，第三个参数是0或False，是不带缓冲的，若是1或True，则带缓冲
		open 文件对象常用属性：
			file.closed ： 判断是否关闭
			file.mode ： 返回访问模式
			file.name ： 返回文件名

		以文件格式和二进制格式打开文件的区别：
			相同点： 都是以二进制格式打开文件
			不同点： 对文件中换行符的处理不同
				Win： \r\n  转换为 \n 
				Unix/Linux ： 默认换行符是 \n
				推荐使用 b 打开二进制文件

		read 函数： 按字节、字符读取文件
			read 读取文件是字节、字符的区别： 取决于open函数打开文件时，是否使用 b 模式，如使用 b ，读取的是 字节， 如不是 b ，则是 字符
			file.read([size])
		read 抛出UnicodeDecodeErorr 异常的解决方案：
			文本的额字符集和操作系统的字符集不匹配，解决方案：
				1. 使用二进制模式读取， 然后用bytes 的decode 方法恢复为字符串
				2. 采用 codecs 模块的open函数打开文件时指定字符集
	readline 和 readlines ： 按行读取文件
		readline ： 读取一行内容 。 readlines ： 读取文件内的所有行 
			readline ： 
				file.readline([size])
					file 为打开的文件对象， size 可选参数，指定读取每一行，一次最多读取的字符数，模式使用 r 或 r+ 读写
			readlines ：
				file.readlines() : file 为文件打开对象， 模式使用r 或 r+

		write 和 writelines ： 向文件中写入数据
			file.write(string) :向文件中写入指定内容。 file。write(string)
			writefiles() 函数： 
				将字符串列表写入文件中。 向文件中写入多行数据时，不自动给各行添加换行符

		close ： 关闭文件
			flie.close()
				关闭使用open函数打开的文件
					如不在关闭文件的前提下将数据写入到文件中，使用文件对象提供的flush 函数

	seek 和 tell 函数
		tell ：判断文件指针当前所处的位置
		seek ：用于移动文件指针到文件的指定位置
			file.tell()
			file.seek(offset[, whence])
				file : 文件对象
				whence ： 指定文件指针要放置的位置，0 开头，1当前位置，2文件尾
				offset ： 相对于whence位置文件指针的偏移量
	
	with  as 用法
		使用with as 语句操作上下文管理器 context manager，自动分配并且释放资源
			with 表达式 [as target]:
				代码块
		即使没有关闭文件，修改文件内容的操作也能成功

	上下文管理器， python with as 底层原理
		包含 __enter__() 和  __exit__() 方法的对象是上下文管理器，上下文管理器必须实现一下两个方法：
			1. __enter__(self): 进入上下文管理器自动调用的方法，会在with as 执行前执行，返回值被赋值给 as 子句后的变量，可返回多个值，在as子句后可指定多个变量，必须用 () 括起来
			2. __exit__(self,exc_typ`e,exc_value,exc_traceback ) ： 退出上下文管理器自动调用的方法，在with as 代码执行后执行，如with as 因异常终止，程序自动调用该方法，使用 sys.exc_info 得到的异常信息将作为调用该方法的参数
		构建上下文管理器，实现的2种方式：
			1. 基于类的上下文管理器
				只要类实现 __enter__()  __exit__ 这两个方法，就可使用with as来管理， 通过 __exit__ 方法的参数，可判断with 代码块执行是否遇到了异常，
			2. 基于生成器的上下文管理器
				使用基于生成器的上下文管理器时，不需要定义 __enter__() 和 __exit__()方法，但必须添加 装饰器 @contextmanager 
			基于类的上下文管理器灵活，适用于大型的系统开发
			基于生成器的上下文管理器更方便、简洁、适用于小型程序
				切记： 用__exit__() 或是 finally 块中释放资源

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



