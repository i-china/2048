```
 @Author : Hale Lv
 @Created Time : 2019-08-29 13:27:28
 @Description : 
```

## Python Scrapy 爬虫框架
	网络爬虫：自动获取多个页面中的所有天气信息，使用正则表达式、XPath 来提取页面中所有的链接 <a.../>元素，顺着这些链接递归打来对应的页面，然后提取页面中的信息
		网路爬虫具体的核心工作：
			1. 通过网络向指定的URL发送请求，获取服务器响应内容
			2. 使用如正则表达式、XPath等提取页面中需要的信息
			3. 高效地识别响应页面中的链接信息，顺着这些链接递归执行第1、2、3步
			4. 使用多线程有效地管理网络通信交互
		网络爬虫的核心工作:
			1. 向URL发送请求,获取服务器响应内容,此核心工作是所有网络爬虫都需要做的通用工作,通用工作由爬虫框架来实现,可提供更稳定的性能.提高开发效率
			2. 提取页面中感兴趣的信息.使用XPath提取信息的效率更高,正则表达式效率比较低
			3. 识别响应页面中的链接信心,使用XPath效率高,正则表达式则底
			4. 多线程管理: 核心工作是通用,由框架完成

		Scrapy 是一个专业,高效的爬虫框架.试用专业的Twisted包,基于事件驱动的网络引擎包,使用lxml专业的XML处理包,cssselect高效地提取HTML页面的有效信息,同时也提供了有效的线程管理

	Scrapy 安装
		pip install scrapy
		python -m pip install scrapy 
		Scrapy需要依赖的第三方包：
			1. pyOpenSSL: 用于支持SSL：Security Socket Layer 
			2. cryptography: 用于加密的包
			3. CFFI ：调用C的接口库
			4. zope.interface : 为Python缺少接口而提供扩展的库
			5. lxml ：一个处理XML、HTML文档的库，比python内置的xml模块更好用
			6. cssselect ： 处理css选择器的扩展包
			7. Twisted ： 为python提供的基于事件驱动的网络引擎包
			pip install Twisted-xxx-xxx-xxx.whl

	Scrapy 项目创建
		创建一个名为 xxxSplider的项目：
			scrapy startproject xxxSplider
			scrapy 是Scrapy框架提供的命令； startproject 是scrapy 的子命令，用于创建项目； xxxSplider是要创建的项目名
				scrapy 提供的子命令： 
					startproject: 创建项目
					fetch ：从指定URL获取响应
					gensplider ：生成蜘蛛
					shell ：启动交互式控制台
					version : 查看Scrapy版本
			项目目录和文件:
				scrapy.cfg: 项目的总配置文件，无需修改
				xxxSplider :项目的Python模块，程序将从此处导入Python代码
				xxxSplider/items.py ：用于定义项目用到的Item类，Item是一个DTO数据传输对象，定义N个属性，该类需由开发者来定义
				xxxSplider/pipelines.py ：项目的管道文件，负责处理爬取到的信息
				xxxSplider/settings.py : 项目的配置文件
				xxxSplider/spiders : 存放项目所需的蜘蛛，负责抓取项目感兴趣的信息
		Scrapy包含的核心组件：
			调度器： 由Scrapy框架实现，负责调度下载中间件从网络上下载资源
			下载器： 由Scrapy框架实现，负责从网络上下载数据，下载得到的数据会由Scrapy引擎自动交给蜘蛛
			蜘蛛：由开发者实现，负责从下载数据中提取有效信息，提取到的信息会由Scrapy引擎以Item对象的形式转交给Pipeline
			Pipeline：该组件由开发者实现，该组件接收到Item对象，包含蜘蛛提取的信息后，可将这些信息写入文件或数据库中

		Scrapy Shell 调式工具及用法
			使用shell调式工具抓取页面中的信息：
				scrapy shell https://wwww.zhihu.com/xxx/xxx/
			让Scrapy伪装为浏览器，需在发送请求时设置 User-Agent头
				scrapy shell -s USER_AGENT='Mozilla/5.0/xxx/xxx' 
				https://www.zhipin.com/xxx/xxx
			使用XPath 或 CSS 选择器提取感兴趣的信息
			XPath简化写法：
				nodename			匹配此节点的所有内容
				/					匹配根字节
				//					匹配任意位置的节点
				.					匹配当前节点
				..					匹配父节点
				@					匹配属性
			使用//div匹配页面中任意位置处的<div.../>元素，也可使用//div/span匹配页面中任意位置处的 <div...>元素内的<span.../>子元素
			XPath支持谓词，在节点后增加一个方括号，在方括号内放一个限制表达式对该节点进行限制
			使用//div[@class]来匹配页面中任意位置处、由class属性的 <div.../>元素，也可使用 //div/span[1]匹配页面中任意位置处的 <div.../>元素内的最后一个 <span.../>子元素
			使用 //div/span/[last()]来匹配页面中任意位置处的 <div.../>元素内的最后一个 <span.../>子元素
			使用 //div/span[last()-1] 匹配页面中任意位置处的 <div.../>元素内的倒数第二个 <span.../>子元素 
			XPath :
				//div[@class="job-primary"]
			extract() 提取节点的内容
			[More](http://c.biancheng.net/view/2750.html)

	Scrapy 爬虫项目开发过程详解
		步骤：
			1. 定义 Item 类，该类仅用于定义项目需要爬虫的N个属性，如：名称、工资、公司等信息，可在items.py 中增加如下类定义：
				import scrapy
				class xxSpliderItem(scrapy.Item):
					title = scrapy.Field()
					salary = scrapy.Field()
					company = scrapy.Field()
					url = scrapy.Field()
					addr = scrapy.Field()
					industry = scrapy.Field()
					publish = scrapy.Field()
			2. 编写Spider类，将该Spider 类文件放在spiders目录下， 需要使用XPath或CSS选择器来提取HTML中感兴趣的信息
				创建Splider：
					scrapy genspider [options] <name> <domain>
				在命令行中进入xxxSpider 目录下，执行如下命令行创建一个Spider：
					scrapy genspider job_position "xxx.com"
				可在xxSpider项目的xxxSpider/spider 目录下找到一个job_position.py，包含的内容如下：
					import scrapy 
					class JobPositionSpider(scrapy.Spider):
						name = 'job_position'
						allowd_domains = ['zhipin.com']
						start_urls = ['https://zhipin.com/xxx/xx/']
					def parse(self,response):
						pass
					是Spider类的模板，该类的name属性用于指定该Spider的名字，allow_domains用于限制该Spider所爬取的域名，start_urls 指定该Spider会自动爬取的页面URl
					Spider 需继承scrapy,Spider，并重写parse(slef,response)方法， 注意字符集问题
					开发者要做的两件事情：
						1. 将要爬取的各页面URL定义在start_urls列表中
						2. 在parse(self,response)方法中通过XPath或CSS选择器提取项目感兴趣的信息
						import scrapy

			3. 编写pipelines.py 文件，该文件负责将所爬取的数据写入文件或数据库中
				[More](http://c.biancheng.net/view/2753.html)

	scrapy 爬虫数据保存到MySQL数据库
		将爬虫的信息写入到文件中之外，也可通过修改Pipeline文件将数据库存到数据库中
		创建数据库：
		CREATE TABLE job_inf (
			id int(11) not null primary key auto_increment,
			title varchar(100),
			salary varchar(100)
			url varchar(100),
			...
		)
		修改Pipeline文件，将爬取到的信息保存到MySQL数据库中：
			improt mysql.connector
			class xxxPipeline(object):
				def __init__(self):
					self.conn = mysql.connector.connect(user='root',password='pass',host='localhost',port='3306',database='dbname',use_unicode=True)
					self.cur = self.conn.cursor()
				def close_spider(self,spider):
					print('---------close mysql----')
					self.cur.close()
					slef.conn.close()
				def process_item(self,item,spider):
					self.cur.execute('insert into job_inf values(null,%s,%s,%s,%s,...%s)',(item['title'],item['salary'],item['company'],...item['xxx']))
					self.conn.commit()
			程序为该Pipeline类定义了构造器，用于初始化数据库链接、游标，还为该Pipeline类重写了close_spider方法， 负责关闭构造器中初始化的数据库资源

	Scrapy 突破反爬虫机制
		使用shell调试工具分析目标站点
		使用Scrapy 爬去高清图片

	Python Scrapy反爬虫常见解决方案
		1. IP地址验证
		2. 禁用Cookie
		3. 违反爬虫规则文件
		4. 限制访问频率
		5. 图形验证码

	Python Scrapy Selenium 整合： 启动浏览器并登陆
		安装Selenium
			1. pip install selenium 
			2. 
			3. 安装目标浏览器




