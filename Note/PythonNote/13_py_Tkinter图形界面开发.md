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


