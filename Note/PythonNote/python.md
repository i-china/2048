			Python类型转换为 JSON类型
				字典(dict)						对象(object)
				列表(list)和元组(tuple)			数组(array)
				字符串(str)						字符串(string)
				整形、浮点型、派生的枚举		数值型(number)
				True							true
				False							false
				None							null 
		查看模块所有属性和函数： import json -> json.__all__
		常用函数和类的功能：
			json.dump(obj,fp,*,skipkeys=False...)	// 将obj对象转换成json字符串输出到fp流中
			json.dumps(obj,*,skipkeys=False,...)	// 将obj对象转换为JSON字符串，并返回该JSON字符串
			json.load(fp,*,cls=NONE,object_hook=None,...)	// 从fp流读取JSON字符串，将其恢复成JSON对象， fp支持write()方法的类文件对象
			json.loads(s,fp,*,encoding=None,cls=None,object_hook=None,...)	// 将JSON字符串s恢复为JSON对象

	
				


## 正则表达式
	Regular Expression 描述一种字符串匹配的模式，检查一个字符串是否含有某个子串，也可从字符串中提取匹配的子串，或对字符串中匹配的子串执行替换操作，可用来开发数据抓取、网络爬虫等
	查看该模块所包含的属性和函数： import re -> re.__all__
	函数作用：
		re.complie(pattern, flags=0) : 将正则表达式字符串编译成 _sre.SRE_Pattern 对象， 该对象代表正则表达式编译之后在内存中的对象，可缓存并复用正则表达式字符串，如多次使用同一正则表达式字符串，则可先编译它。
			pattern ： 所编译的正则表达式字符串， flags ： 匹配旗标，
		re.match(pattern , string, flags=0) : 从字符串开始位置匹配正则表达式，如匹配不成功，match 函数返回None，
			pattern ： 正则表达式。 string ：匹配的字符串。 flags ： 正则表达式的匹配旗标。
		re.search(pattern, string, flags=0) : 扫描整个字符串，返回字符串中第一处匹配pattern的匹配对象，
			pattern ： 正则表达式。 string ：被匹配的字符串。 flags ： 匹配旗标
		re.findall(pattern, string, flags=0) :  扫描整个字符串，返回字符串中所有匹配pattern的子串组成的列表。 
			pattern ： 正则表达式。 string ：被匹配的字符串。 flags ： 匹配旗标
		re.finditer(pattern, string, flags=0) ： 扫描整个字符串，返回字符串所有匹配pattern 的子串组成的迭代器。
			pattern ： 正则表达式。 string ：被匹配的字符串。 flags ： 匹配旗标
	findall、finditer 、search 的区别： search 只返回字符串中第一处匹配pattern的子串，findall和finditer 返回字符串中所有匹配pattern的子串
		re.fullmatch(pattern,string, flags=0) ：要求整个字符串匹配 pattern，如匹配返回包含匹配信息的 _sre.SRE_Match对象，否则 None
		re.sub(pattern,repl,string,count=0,flags=0) ：将string字符串中所有匹配pattern的内容替换成repl
				repl ： 被替换的字符串，可是函数， count 控制替换的次数。
			import re
			date = '2019-08-22'
			print(re.sub(r'-','/',date))
				r'-' ：是原始字符串， r ： 代表原始字符串，通过原始字符串，避免对字符串中的特殊字符转译
					r'(?P<lang>\w+)' : 正则表达式用圆括号表达式创建一个组， '?P' 为该组起名为 lang ， \w+ 是正则表达式的内容，代表一个或多个任意字符，
		re.split(pattern,string, maxsplit=0, flags=0) ： 使用pattern对string进行分割，返回分割得到的多个子串组成的列表，maxsplit 参数控制分割的次数
		re.purge() : 清楚正则表达式缓存
		re.escape(pattern) ：对模式中除ASCII字符、数值、下划线之外的其他字符转义
		re模块中的Match 对象是match 、search方法的返回值，包含了详细的正则表达式匹配信息，包含匹配的位置、子串
		sre.SRE_Match 对象包含如下方法或属性：
			match.group([group1,...]) : 获取该匹配对象中指定组所匹配的字符串
			match.__getitem__(g) ： match.group(g)的简化写法。
			match.groups(default=None) : 返回match对象中所有组所匹配的字符串组成的元组
			match,groupdict(default=None) ：返回match对象中所有组所匹配的字符串组成的字典
			match.start([group]) ：获取该匹配对象中指定组所匹配的字符串的开始位置
			match.end([group]) ：获取结束位置
			match,span([group]) ：获取开始和结束位置，相当于同时返回 start 和 end方法的返回值
			match.pos : 该属性返回传给正则表达式对象的search , match等方法的pos参数
			match.lastindex : 返回最后一个匹配的捕获组的整数索引，如没有，则返回None
			match.lastgroup : 返回最后一个匹配的捕获组的名字，如没有，则返回None
			match.re : 返回执行正则表达式匹配时所用的正则表达式
			match.string : 返回执行正则表达式时所用的字符串

### set 和 frozenset 集合操作
		set 集合是可变容器，可改变容器中的元素， frozenset集合，是set的不可变版本，他的元素不可变
		set集合：
			两个特征：
				1. set 不记录元素的添加顺序
				2. 元素不允许重复
				[e for e in dir(set) if not e.startswith('__')]
			add添加 、 remove 删除元素、discard 删除元素、clear 清空 
			remove 和 discard 区别： remove 报KeyError异常。discard 不报
		set 支持的运算符：
			<= : 相当于调用 issubset() 方法，判断前面的set集合是否为后面set集合的子集合
			>= ：调用issuperset 方法，判断是否为后面set集合的父集合
			- ： 调用difference ，前面的set集合减去后面的set集合的元素
			& ： 调用intersection，获取两个set集合的交集
			^ ： 计算两个集合异或的结果，即两个集合的并集减去交集的元素

	frozenset 集合
		是set的不可变版本，set集合中不改变集合本身的方法，fronzenset 都支持
		作用：
			1. 当集合元素不需要改变时，使用frozenset 代替 set更安全
			2. 当某些api需要不可变对象时，必须用frozenset代替set
	
	queue (双端队列) 模块
		栈：一种特殊的线性表，允许一端进行插入、删除操作。这个端为栈定(top),另一端为栈底(botton)
		从栈顶插入一个元素称为： 进栈， 压入栈。 push 
		从栈顶删除一个元素称为： 出栈， 弹出栈。 pop
		栈，陷入栈的元素位于栈底，上面元素出栈后，栈底的元素才能出栈。 栈 是一种 后进先出(LIFO)的线性表 
		队列是一种特殊的线性表，只允许在表的前段(font) 删除，在后端(rear) 插入。 插入的操作的端为 队尾， 删除操作的端为 队头
			队列：元素是从队列的rear 端进。 队列是一种 先进先出FIFO 的线性表。 
		双端队列deque 代表特殊的队列， 在两端同时进行插入、删除操作，deque 即可为队列使用，也可为 栈 使用
		deque 位于 collections 包下，[e for e in dir(collections.deque)if not e.startswith('__')]
			from collections import deque
			双端队列的特征， deque 的左边 left 相当于 它的队头front， 右边right 相当于它的队列尾rear
				append 和 appendleft ：在deque的右边或左边添加元素， 即在默认队列尾添加元素
				pop 和 popleft ：在deque的右边或左边弹出元素，默认在队列尾弹出元素
				extend 和 extendleft ： 在deque的右边或左边添加多个元素，默认在队列尾添加多个元素
			deque 中clear 方法用于清空队列，insert 方法是线性表的方法，指定位置插入元素
			deque 中 rotate 方法。将队列的队尾元素移动到队头，使之首位相连

	heapq 堆操作
		小顶堆的任意子树是小顶堆，大顶堆的任意子树是大顶堆
		import heapq	-> heapq.__all__
		函数功能：
			heappush(heap,item) ： 将item元素加入堆
			heappop(heap) : 将堆中最小元素弹出
			heapify(heap) : 将堆属性应用到列表上
			headpreplace(heap,x) : 将堆中最小元素弹出，并将元素x入堆
			merge(*iterables, key=None, reverse=False) ： 将多个有序的堆合并为一个大的有序堆，然后输出
			headppushpop(heap,item) ： 将item入堆，然后弹出并返回堆中最小的元素
			nlargest(n,iterable,key=None) ： 返回队中最大的n个元素
			nsmallest(n,iterable,key=None) : 返回堆中最小的n个元素
		
	ChainMap
		使用链的方式将多个 dict 链在一起，允许程序可直接获取任意一个dict所包含的key对应的value
		ChainMap 相当于把多个dict合并为一个大的dict，
	
	Counter 类
		可自动统计容器中个元素出现的次数
		本质是一个特殊的dict，key是所包含的元素，value记录key出现的次数 
		Counter 继承了dict， 提供三个常用的方法：
			1. elements ： 返回该counter 所包含的全部元素组成的迭代器
			2. most_common([n]) ：返回Counter 中出现最多的n个元素
			3. subtract([iterable-or-mapping]) ： 计算counter 的减法，计算减去之后各元素出现的次数
		可把Counter对象转换为 set集合、list列表、dict字典等，可对Counter执行 加、减、交、并运：
			加： 将两个Counter对象中各Key 出现的次数相加，保留为正的元素
			减： 相减，保留出现次数为正的元素
			并： 出现key且各key对应的次数的最小数
			求正： 只保留出现次数为0 或正数的key-value对
			求负： 保留次数为负的 key-value 对，将次数改为正数
		
	defaultdict ：
		是dict 的子类，与dict 的区别： 根据不存在的key访问dict中对应的value，会引发KeyError异常，defaultdict则提供default_factory属性， 指定的函数为不存在的key来生成value

	namedtuple 工厂函数功能
		可创建一个tuple类的子类，为tuple的每个元素指定字段名，可根据字段名访问namedtuple的各元素，根据索引来访问namedtuple的各元素
			namedtuple(typename,field_names, * , verbose=False, rename=False,module=None)
				typename : 指定所创建的tuple子类的类名，等于用户定义一个新类
				field_names ： 字符串序列，使用单个字符串代表所有字段名，用空格、逗号隔开
				rename ： 如参数为True， 无效字段名会被自动替换为位置名
				verbose ： 参数为True， 当子类被创建后，该类定义会被立即打印出来
				module ： 自定义类的__module__属性将被设为该参数值
			Python 为命名元组提供的方法和属性：
				_make(iterable) ：类方法，根据序列或可迭代对象创建命名元组对象
				_asdict() : 将当前命名元组对象转换为OrderdDict 字典
				_replace(**kwargs) ： 替换命名元组中一个或多个字段的值
				_source ： 返回定义该命名元组的源代码
				_fileds ： 返回该命名元组中所有字段组成的元组
			
	OrderdDict用法：
		是dict的子类，可 维护 添加 key-value 对的顺序， 先添加key-value对排的前面，后添加的key-value对排的后面
		两个方法：
			1. popitem(last=True) ： 弹出并返回最左边的最后加入的key-value对，将last参数设为False，则弹出并返回最左边最先加入的key-value对
			2. move_to_end(key,last=True) : 将指定的key-value对移动到最右边最后加入，将last改为False，则将指定的key-value对移动到最左右最先加入
			
	itertools模块：生成迭代器
		先导入 import itertools 模块， [e for e dir(itertools) if not e.startswith('__')]
		三个生成无限迭代器的函数：
			1. count(start,[step]) ：生成start、start+step、start+2*step,...的迭代器，step默认为1。 count(10) 生成的迭代器包含： 10，11，12，13，14.。。
			2. cycle(p) : 对序列p生成无限循环p0，p1.。。的迭代器。cycle('ABCD') 包含：A,B,C,D,A,B,C,D,...
			3. repeat(elem [,n]) ： 生成无限个 elem元素重复的迭代器. repeat(10,3) ：10，10，10，
		在itertools 模块中常用的迭代器函数：
				accumulate(p,[func]) ： 生成根据序列p元素累加的迭代器
				chain(p,q,...) : 将多个序列里的元素 链 在一起生成新的序列
				compress(data,selectros) ： 根据selectors序列的值对data序列的元素进行过滤
				dropwhile(pred,seq) : 使用pred函数对seq序列进行过滤，如计算为False，保留该元素到序列结束的全部元素
				takewhile(pred,seq) ：使用pred函数对seq进行过滤，去掉从该元素序列结束的全部元素
				filterfalse(pred,seq)：使用pred函数对seq序列进行过滤，保留seq中使用pred计算为True的元素
				islice(seq,[start,]stop[,step]) ：类似于slice，返回seq[start:stop:step]的结果
				starmap(func,seq)：使用func对seq每个元素进行计算，结果为新的序列元素
				zip_longest(p,q,...) ：将p、q序列中元素按索引合并成元组，元组作为新序列的元素
		在itertools 模块中生成序列排列的工具函数：
				product(p,q,...[repeat = 1])：用序列p、q，。。。进行排序组合，相当于嵌套循环组合
				permutations(p[,r]) ：从序列p中取出r个元素组成排序，将排序得到的元组作为新迭代器的元素
				combinations(p,r) ：从序列p中取出r个元素组成全组合，元素不重复，将组合得到的元组作为新迭代器的元素
				combinations with_replacement(p,r)：从序列p中取出r个元素组成全组合，元素可重复，将组合得到的元组作为新迭代器的元素

	functools 模块：
		包含函数装饰器和便捷的功能函数， import functools 
			常用函数装饰器和功能函数：
				functools.cmp_to_key(func) ：将老式的比较函数(func)转换为关键字函数(key function) py3不支持
				@function.lru

				[更多](http://c.biancheng.net/view/2443.html)







## Tkinter (GUI图形洁面开发)
	GUI ：Graphics User Interface 图形用户界面。三要素：输入数据、处理数据、输出数据
	常用库：
		wxPython ： 跨平台GUI工具集
		PyQt ： 是Py和Qt库的融合
		PyGTK ： 基于老版本GTK+2的库提供绑定，借助于底层GTK+2提供的可视化元素和组件
		Pywin32 ： 允许像VC使用Py开发win32应用
		Kivy ： 开源库，使用同源代码创建的程序跨平台
		Flexx ： 纯Py工具包，创建图形化界面程序，支持使用web技术进行界面渲染

	Tkinet GUI 编程组件及用法
		学习GUI步骤为三步：
			1. 包含的组件
			2. 容器及容器对组件布局的方法
			3. 掌握各组件的用法
			[Tkinter GUI 关系](http://c.biancheng.net/view/2451.html)
		Tkinter的GUI组件有两个根父类，直接继承object类
			1. Misc ： 所有组件的根父类
			2. Wm ： 提供窗口管理器通行的功能函数
		BaseWidget ： 所有组件的基类，派生类：Widget ，通用GUI组件，Tkinter 是所有GUI组件都是Widget的子类
		各GUI组件的功能
			Toplevel：		顶层			容器类
			Button ：		按钮			按钮组件
			Canvas ：		画布			绘图功能
			Checkbutton：	复选框			可勾选的复选框
			Entry  ：		单行输入框		用户可输入容内
			Frame ：		容器			装载其他GUI组件
			Label ：		标签			显示不可编辑的文本或图标
			LabelFrame ：	容器			容器组件，支持添加标题
			Listbox ：		列表框			列出多个选项，供用户选择
			Menu	：		菜单			菜单组件
			Menubutton ：	菜单按钮		包含菜单的按钮 包括下拉式、层叠式
			OptionMenu ：	菜单按钮		Menubutton的子类
			Message ：		消息框			类标签，显示多行文本，Lable代替，废弃
			PanedWindow：	分区窗口		该容器可划分为多个区域
			Radiobutton	：	单选钮			单选按钮
			Scale ：		滑动条			可设置起始值和结束值，显示当前精准值
			Spinbox ：		微调选择器		可通过组件向上、向下选择不同的值
			Scrollbar ：	滚动条			用于为组件(文本域、画布、列表框、文本框)提供滚动
			Text ：			多行文本框		显示多行文本
		initWidgets 方法实现的代码：
			1.创建 GUI 组件
			2.添加 GUI 组件
			3.配置 GUI 组件
		配置GUI组件的2种方法：
			1. 以关键字参数的方式配置
			2. 以字典语法进行配置
		[GUI通用选项](http://c.biancheng.net/view/2451.html)
	
	TKinter Pack 布局管理器
		[常用选项及功能]()
		anchor : 空间大于组件所需求的大小，决定被放置在容器的位置
		expand : 指定当容器增大时是否拉伸组件
		fill :	组件是否沿水平或垂直方向填充
		ipadx :	指定组件在 x 方向上的内部留白
		ipady : 在 y 方向上内部留白
		padx :  在x方向上与其他组件的间距
		pady :	在y方向上的间距
		side :  设置组件的添加位置

	Tkinter Grid 布局管理器
		Grid 把组件空间分解为一个网格进行维护
		Tkinter Grid 常用选项
			column ： 指定将组件放哪列
			columnspan : 指定组件横跨多少列
			row ：指定放入哪行
			sticky ：类 pack方法的anchor选项
	
	Tkinter Place 布局管理器
		绝对布局 ： 要求程序显式指定每个组件的绝对位置或相对其他组件的位置
		常用选项：
			x			指定组件的X坐标， x 为 0 代表最左边
			y			Y 坐标						最右边
			relx		组件的X坐标
			rely		组件的Y坐标
			width		组件的宽度
			height		组件的高度
			relwidth	组件的宽度
			relheight	组件的高度
			bordermode	设置组件的宽度、高度

	Tkinter Command 和 Bind 事件处理
		command 绑定事件处理方法：
			可通过command 来绑定，可绑函数或方法，单击时，触发绑定的函数或方法
		bind 绑定事件处理方法：
			无法为具体事件绑定事件处理方法
			无法获取事件相关信息
		bind()方法： 可为 任意 事件绑定事件处理方法
			Tkinter 支持的鼠标、键盘事件

	Tkinter ttk组件及用法
		是Tinkter 包下的模块，界面美化、包装
	
	Tkinter Variable类用法
		支持GUI组件与变量进行双向绑定，
			1. 如改变变量的值，GUI组件的显示内容或值也改变
			2. 当GUI组件的内容改变时，值也改变
		Tinkter 不能讲组件和普通变量进行绑定，只能和tkinter 包下的Variable类的子类进行绑定
		1. StringVar() :	包装str值的变量
		2. IntVar() :		整形值的变量
		3. DoubleVar() ：	浮点值的变量
		4. BooleanVar() :  包装bool值的变量
	
	Tkinter compound 选项使用方法
		如使组件同时显示文本和图片，可通过 compound 选型进行控制
			属性值：
				1. None ： 图片覆盖文字
				2. LEFT 常量： 图片在左，文本在右
				3. RIGHT 变量： 图片在右，文本在左
				4. TOP 常量： 图片在上， 文本在下
				5. BOTTON 常量： 图片在底，文本在上
				6. CENTER 常量： 文本在图片上方
	
	Tkinter Entry 和 Text 控件用法
		可接收用户输入的输入框组件，区别： Entry ： 单行。 Text： 多行

	Tkinter Radiobutton 和 Checkbutton 用法
		单选按钮，可绑定一个方法或函数。 将多个Radiobutton 编为一组，将多个Radiobutton绑定到同一个变量，当其中一个单选按钮被选中时，该变量随之改变。
	
	Tkinter Listbox 和 Combobox 控件用法
		列表框，通过列表框选择一个列表项。
			创建 Listbox 的步骤：
				1. 创建Listbox 对象，设置listbox的选择模式
				2. 调用listbox的insert(self,index,*elements)添加选项
	
	Tkinter Spinbox 控件
		通过两个小箭头调整该组件内的值
	
	Tkinter Scale 和 LabeledScale用法
		代表一个滑动条，为滑动设置最大最小值
		Scale 组件选项：
			from ： 最大值
			to ： 最小值
			resolution ： 滑动时的步长
			lable ： 设置标签内容
			length ： 设置轨道的长度
			width ： 轨道的宽度
			troughcolor ： 背景色
			sliderlength ： 长度
			sliderrelief ： 立体样式
			showvalue ： 是否显示当前值
			orient ： 设置方向
			digits ： 设置有效数字位数
			variable ： 与变量进行绑定
			command ： 为该Scale 组件绑定事件处理，函数或方法

	Tinkter LabelFrame 用法
		是Frame容器改进版，为容器添加标签，可为普通文字标签，也可为GUI组件为标签
		对标签进行定制：
			1. labelwidget ： 将任意GUI组件作为标签
			2. labelanchor ： 设置标签位置

	Tkinter Panedwindow 控件
		管理窗口布局的容器，允许添加多个子组件，并为每个子组件划分一个区域，可用鼠标移动分隔线改变各子组件的大小
		操作Panedwindow 容器中子组件的方法：
			1. add(self,child,**kw) : 添加一个子组件
			2. insert(self,pos,child,**kw) : 在pos 位置插入一个子组件
			3. remove(self,child) ： 删除一个子组件，所在区域也删除 

	Tkinter OptionMenu控件
		构建带菜单的按钮，可在按钮的四个方向上展开，通过direction选项控制
			__init__(self,master,variable ,value,*values, **kwargs)
				1. variable ； 指定该按钮上的菜单与哪个变量绑定
				2. Value ： 默认选择菜单中的哪一项
				3. values ： 将收集为此参数传入的多个值，为每个值创建一个菜单项
				4. kwargs ： 为 OptinoMenu配置选项

	Tkinter 对话框创建及使用
		1. 对话框依赖类似于顶级窗口，创建时需指定master属性
		2. 对话框有非模式noo-modal和模式modal，某个模块对话框被打开，位于它依赖的窗口之上。
		Tkinter 在 simpledialog 和dialog 模式下分别提供了 SimpleDialog 类和 Dialog 类，可作为普通对话框使用
			使用simpledialog 和dialog 创建对话框可指定：
				1. title： 标题
				2. text ：内容
				3. button： 按钮
				4. default：默认第几个按钮得到焦点
				5. cancel： 指定对话框上角的X按钮关闭对话框

	Tkinter 自定义对话框
		自定义通过继承Toplevel 实现：
			1. 继承Toplevel 实现自定义对话框需要为对话框指定 master
			2. 调用Toplevel 的grab_set 方法 把对话框变为模式对话框，否则为非模式对话框

	Tkinter 输入对话框
		工具函数：
			1. askinteger ； 生成一个让用户输入正数的对话框
			2. askfloat ： 输入浮点数的对话框
			3. askstring ： 输入字符串的对话框

	Tkinter 文件对话框创建和使用
		直接返回用户选择文件的输入/输出流：
			1. askiopenfile ： 打开单个文件的对话框
			2. askopenfiles ： 打开多个文件的对话框
			3. askopenfilename ： 打开单个文件的对话框，返回选择文件的文件路径
			4. askopenfilenames ： 多个文件的对话框
			5. asksavesfile ： 生成保存文件的对话框
			6. asksaveasfilename ： 保存文件的对话框，返回所选择文件的文件路径
			7. askdirectory ： 生成打开目录的对话框
		生成打开文件的对话框工具函数：
			1. defaulttextension ： 指定默认扩展名
			2. filetypes ： 查看的文件类型
			3. initaldir ： 初始化打开的目录
			4. parent ： 指定该对话框的属主窗口
			5. title ： 对话框的标题
			6. multiple ： 允许多选

	Tkinter askcolor 颜色选择对话框
		函数选项：	
			1. parent ： 属主窗口
			2. title ： 标题
			3. color ： 颜色

	Tkinter 消息框
		选项按钮
			1. icon  ： 定制图标
			2. type ： 定制按钮的选项
		showinfo 函数： 默认生成的消息框的图标是感叹号

	Tkinter Menu 菜单 窗口菜单和右键菜单
		添加菜单项的方法：
			1. add_command() : 添加菜单项
			2. add_checbutton(): 复选框
			3. add_radiobutton(): 单选按钮
			4. add_separator() : 菜单分隔条
		添加菜单的三个方法选项：	
			1. label ： 指定菜单项的文本
			2. command ： 指定绑定的事件处理方法
			3. image ： 指定菜单项的图标
			4. compound ： 图标位于文字的哪个方位
		Menu窗口菜单：
			创建菜单后，将菜单设为窗口的menu选项即可
				add_command 为file_menu 添加多个菜单项
				add_cascade 再次为file_menu添加子菜单
				add_radiobutton 添加多个单选菜单项
		Menu 右键菜单：
			先创建菜单，为目标组件的右键菜单绑定处理函数, 点击右键，调用菜单post 方法即可

	Tkinter Canvas 画布完全攻略
		绘制直线、矩形、椭圆等图形，提供create_rectangle 方法绘制和 create_oval 绘制椭圆，绘制方法：
			create_arc ： 绘制弧
			create_bitmap ： 位图
			create_image ： 图片
			create_polygon ： 多边形
			create_line ： 直线
			create_text ： 文本
			creat_window ： 绘制组件
				绘制指定的选项：	
					fill ： 填充颜色
					outline ： 边框颜色
					width ： 边框宽度
					dash ： 边框虚线
					stipple ： 位图平铺填充
					start ： 开始角度
					extend ： 绘制弧的角度
					style ： 绘制弧样式
					arrow ： 是否有箭头
					arrowshape ： 箭头样式
					joinstyle ： 连接点的风格
					anchor ： 绘制文字
					justify ： 文本对齐方式

	Tkinter Canvas tag_bind ：指定图形项绑定事件处理函数或方法
		tag_bind 方法： 用于为指定图形项绑定事件处理函数或方法，可用于响应用户动作
		
	Tkinter Canvas 绘制动画
		小球转动； 循环显示多张转动的小球图片
		小球移动： 改变小球的坐标程序


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







