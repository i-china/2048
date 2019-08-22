### 字符串常用方法详解
	拼接字符串、截取字符串、格式化字符串

字符串拼接(+拼接数字)
	使用加号 (+) 作为字符串的拼接运算符
	字符串拼接数字
		先将数字转换为 字符串
			数字转换为字符串： str()	repr()
				直接拼接字符串和数字，会报错

截取字符串(字符串切片)
	通过索引来操作字符：
		string[index]				// index 表示索引值，从0开始递增，最后一个为-1
	使用范围获取字符串的中间值：
		string[start: end: step]
			string : 要截取的字符串
			start : 要截取的第一个字符所在的索引，默认为0
			end ：要截取最后一个字符所在的索引。如不指定，默认字符串的长度
			step ：从start字符开始，step 距离获取一个字符，end索引出的字符。step默认值为1
				支持用 in 运算符判断是hi否包含某个子串

split() : 分割字符串
	将一个字符串按照指定的分隔符切分成多个子串，字串被保存在列表中，不包含分隔符
		str.split(sep,maxsplit)
				1. str：要分割的字符串
				2. set：指定分隔符，默认使用空字符分割
				3. maxsplit：可选参数，指定分割的次数，如不指定，次数不限

join() ：合并字符串
	将列表(或元组)中多个字符串采用固定的分隔符连接在一起
		join_str = str.join(iterable)
			1. join_str : 合并后生成的新字符串
			2. str ： 指定合并时的分隔符
			3. iterator： 做合并操作的源字符串数据，允许：列表、元组等

count() ：统计字符串出现的次数
	用于检索指定字符串在另一个字符中出现的次数，如检索的字符串不存在，返回 0，否则返回出现的次数
		str.count(sub[,start[,end]])
			1. str : 原字符串	
			2. sub : 要检索的字符串
			3. start : 起始位置
			4. end : 终止位置

find() ：检测字符串中是否包含某字串
	检索字符串中是否包含目标字符串，如包含：出现第一次该字符串的索引，返回-1
		1. str：原字符串
		2. sub：目标字符串
		3. start： 起始位置，若不指定，默认从头开始索引
		4. end ：结束位置，若不指定，一直检索到结尾
	rfind() ：字符串从右边开始检索

index() ：检测字符串中是否包含某子串
	检索是否包含指定的字符串，若指定的字符串不存在，抛出异常
		str.index(sub[,start[,end]])
			1. str : 原字符串
			2. sub : 子字符串
			3. start : 起始位置，默认从头开始
			4. end : 结束位置，默认到结尾

startswith() 和 endswith
	startswith() ： 检索字符串是否以指定字符串开头，是返回True，反之False
		str.startswith(sub[,start[,end]])
			1. str ： 原字符串
			2. sub ： 要检索的字串
			3. start ：起始位置，默认从头开始
			4. end ： 结束索引
	end.swith(sub[,start[,end]]) : 是否以指定字符结尾，是返回True，反之Flase
		str.endswith(sub[,start[,end]])
			1. str : 原字符串
			2. sub : 检索的字符串
			3. start : 起始位置
			4. end : 结束位置
			
字符串大小写转换的三种函数
	title()	: 将字符串中每个单词的首字符转为大写，其他转为小写
		str.title()
			str 要进行转换的字符串
	lower() : 将字符串所有大写字符转为小写
		str.lower()
	upper() : 将字符串所有小写字母转为大写
		str.upper()

去除字符串中空格(删除指定字符)的3种方法
	去除字符串中的空格和特殊字符
		特殊字符： 制表符 \t、回车符 \r 、换行符 \n
	strip() 	lstrip() 	rstrip() 
	1. strip()	:	删除字符串前后(左右两侧)的空格或特殊字符
		str.strip([chars]) 
			str : 原字符串
			chars ：指定要删除的字符，可同时指定多个，若不指定，默认为空格、制表符、回车符、换行符等特殊字符
	2. lstrip() :	删除字符左边的空格或特殊字符
		str.lstrip([chars])
	3. rstrip() :	删除字符右边的空格或特殊字符
		str.rstrip([chars])

format() 格式化输出
	str.format(args)
		str : 指定字符串显示样式
		args: 指定要进行格式化转换的项，如多项，逗号分割
			str 格式：
				{ [index][:[fill] align] [sign] [#] [width] [.precision] [type] ]}
					index :  指定 ；后边设置的格式要作用到args中第几个数据，索引值从0开始
					fill : 指定空白处填充的字符
					align : 指定数据的对齐方式
						< :	左对齐
						> : 右对齐
						= : 右对齐，放在填充内容的最左侧，只对数字类型有效
						^ : 居中，和width参数一起使用
					sign：
						+	： 
						-	：
						空格：
						#	：
					width ：指定输出数据时所占的宽度
					.precision : 指定保留的小数位数
					type ：指定输出数据的具体类型
						s	： 字符串
						d	： 十进制整数
						c	： 将十进制整数自动转换为对应的Unicode字符
						e|E	： 转为科学技术后，再格式化输出
						g|G	： 自动再e|f E|F 中切换
						b	： 将十进制自动转换为二进制，再格式化
						o	： 转为八进制，再格式化
						x|X	： 转为十六进制
						f|F	： 转为浮点数
						%	： 显示百分比，默认小数点后6位

encode() 和 decode() 字符串编码转换
	2中常用字符串类型： str 、bytes。 str：Unicode 。 bytes：二进制数据。使用encode 和decode 进行转换
	encode() : 将str类型转换为bytes类型，成为 编码
		str.encode([encoding="utf-8"][,errors="strict"])
			str ：要进行转换的字符串
			encoding="utf-8" : 采用的字符编码，默认位utf-8 中文：gb2312
			errors="strict"	 : 指定错误处理方法：
					strict :	遇到非法字符就抛出异常
					ignore :	忽略非法字符
					replace:	用 "?" 替换非法字符
					xmlcharrefreplace: 使用xml的字符引用

	decode() ： 将bytes类型的二进制数据转换为str类型，过程称为"解码"
		bytes.decode([encoding="utf-8"][,errors="strict"])
			bytes : 要进行转换的二进制数据
			encoding="utf-8": 解码时采用的字符编码
			errors="strict"

dir() 和 help() 帮助函数
	dir() : 列出指定类或模块名包含的全部内容，包括函数、方法、类、变量等
	help() : 查看某个函数或方法的帮助文档


