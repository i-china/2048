创建表：
	create table tb [if not exists] _name(
		`id` int(10) auto_incrementl,
		`name` varchar(20) not null default '',
		`user_id` int(10) default 1,	
		`salary` float unique,
		`create_at` time,
		primary key(id,user_id),
		contraint fk_name foreign key (field) references other_tb(id)
	);

	主键约束： primary key
	外键约束： foreign key
	非空约束： not null
	唯一性约束：unique
	默认约束：default value
	自动增加： auto__increment

查看表：
	describe
	describe tb_name / desc tb_name;

查看表结构：
	show create table tb_name \G

查看警告信息：
	show warnings;

修改数据表: 

修改表名：
	alter table tb_oldName rename tb_newName;

修改自增ID值
	alter table tb_name auto_increment = 1

修改字段的数据类型：
	alter table tb_name modify id int(11);

修改字段名：
	alter table tb_name change tb_old_field  tb_new_field int(10);

添加字段：
	alter table tb_7 add name varchar(100) [first|after id];

删除字段：
	alter table tb_7 drop fieldName;

修改字段的排列位置：
	alter table tb_7 modify name varchar(30) [first|after] id;
	
修改表的存储引擎：
	alter table tb_7 engine = myisam;

删除表的外键约束：
	alter table tb_7 drop foreign key FK_Name;

删除数据表:
	drop table [if exists] tb_name;

删除没有被关联的表:
	drop table tb_name;
删除被其他表关联的表的主表：
	全部删除：删除会破坏表的参照完整性，先删除与之关联的子表，再删除父表，这样会删除两个表中的数据。
	单独删除：如果保存子表，只需将关联表的外键约束条件取消，然后删除父表

	alter table tb_name drop foreign key FK_Name;


数据类型:
整数类型:
	tinyint		smallint	mediumint	int(integer)	bigint

浮点类型:
	浮点类型：float	double
	定点类型：decimal

字符串类型：
	char	varchar		binary		varbinary	blob	text	enum	set

二进制类型：
	bit		binary		varbinary		tinyblob	blob	mediumblob		longblob


运算符：
	算数运算：
		+	-	 *	 /
	比较运算:结果为 0，1 或者 null
		=	<=>	  <>	(!=)	<=	 >=	   >	is null		it not null		
		least	  greatest		between		and		isnull		in		not in  
		like		regexp
	逻辑运算：
		false	null	
		not		null 
		and		&&
		or		|| 
		xor
	位操作运算：
		|		&		异或：^		<<		>>		取反：~	

函数：

数学函数：
	绝对值函数： abc()
	平方根函数|求余函数： mod(x,y)
	获取整数函数： ceil(x), ceiling(x) , floor(x)
	随机整数函数： rand()	rand(x)
	四舍五入函数： round(x), round(x,y), truncate(x,y)
	符号函数：	sign(x)
	幂运算函数： pow(x,y), power(x,y), exp(x)
	对数运算函数： log(x) , log10(x)
	角度与弧度相互转换的函数： radians(x), degrees(x)
	正弦函数： sin(x)， 反弦函数: asin(x)
	余弦函数： cos(x),  反余弦函数： acos(x)
	正切函数、反正切函数、余切函数

字符串函数：
	计算长度的函数： length(), char_length()
	合并字符串的函数： concat(str,str1...),		concat_ws(str,str1...)
	替换字符串的函数： insert(str1, x ,len,str2)
	大小写转换函数： lower(),		upper()
	获取指定长度的字符串的函数： left(s,n), right(s,n)
	填充字符串的函数： lpad(str1,len,str2), rpad(str1,len,str2)
	删除空格的函数： ltrim(s), rtrim(s), trim(s)
	删除指定字符串的函数： trim(str1 from s)
	重复生成字符串的函数： repeat(s,n)
	比较字符串大小的函数：	strcmp(str,str1)
	获取字串的函数： substring(s,n,len),	mid(s,n,len)
	匹配字串开始位置的函数： locate('s','str'); position('s' in 'str'); instr('str','s');
	字符串逆序的函数： reverse(s)
	返回指定位置的字符串的函数：	
	返回指定字符串位置的函数： field(s,s1,s2)
	返回字串位置的函数： find_in_set(s1,s2)
	选取字符串的函数： make_set(x,s1,s2...)


日期和时间函数：
	当前日期和时间的函数：curdate(), current_date(), curdate()
	时间函数获取系统当前时间：curtime(), current_time(), curtime() 
	获取当前系统日期和时间： current_timestamp(), localtime(), now(), sysdate()
	Unix时间戳函数：unix_timestamp()
	将UNIX时间戳转为普通格式时间： from_unixtime('1232131')
	返回UTC日期的函数和返回UTC时间的函数：utc_date(), utc_time(),
	返回月份的函数： month(date), monthname(date)
	获取日期的函数： dayname(d)， dayofweek(d), weekday(d)
	获取天数的函数： dayofyear(d), dayofmonth(d) 
	获取年份、季度、小时、分钟、秒钟的函数：year(),	quarter(), minute(), second()
	获取日期的指定值的函数：  extract(type from d)
	时间和秒钟转换的函数：time_to_sec(), sec_to_time(), 
	计算日期和时间的函数：date_add(), adddate(), date_sub(), subdate(), addtime(), datediff(),subtime(), 
	将日期和时间格式化的函数：date_format(), time_format(), get_format(), 


条件判断函数：
	if(expr,v,v1)
	ifnull(v1,v2)
	case, case value when, case when

系统信息函数:
	获取版本号、连接数、数据库名的函数：select version(), connect_id(), show processlist() select database(), select schema()
	获取用户名的函数：select user() | current_user() | system_user()
	获取字符串的字符集和排序方式的函数：charset('abc'), charset(convert('abc' using latin1), charset(version))
	获取最后一个自动生成的ID值的函数：select last_insert_id() 

加密函数：
	password(str)
	md5(str)
	加密函数：encode(str,pswd_str)
	解密函数：decode(crypt_str,pswd_str)


其他函数：
	格式化函数：format()
	不同进制的数字进行转换的函数：conv() 
	IP地址与数字相互转换的函数：inet_aton(), inet_ntoa()
	加锁函数和解锁函数：select get_lock(), is_used_lock(), is_free_lock(), release_lock()
	重复执行指定操作的函数：denchmark() 
	改变字符集的函数：convert() 
	改变数据类型的函数：cast(), convert()


查询语句：
	基本查询：
		select { *  | } [from table_name  [ where <>] [group by <>] [ having <> ] [ order by <> ] [ limit [<>,] <row count>]  ]
		select filed,field1...fieldN from [table | view] where [<condition>]	
	单表查询：
		查询所有字段：select * from table;
		查询指定字段：select filed,field1... from table;
		查询指定记录：select filed,filed1... from table where condition;
		带 IN 关键字的查询：select filed,filed1... from table where filed in (a,z) order by field;
		带 Between and 的范围查询：select filed from table where filed between a and z;
		带 Like 的字符匹配查询：select filed from table where filed like '%'
			% 匹配任意长度的字符，     _ 下划线只能匹配任意一个字符
		查询空值：select filed from table where filed is null | is not null 
		带 And 的多条件查询：select field, field1 from table where filed > condition and filed > condition;
		带 Or 的多条件查询：select field, filed1 from table where field = condition or filed1 = condition;
		查询结果不重复：select distinct field from table;
		对查询结果排序：select field,filed1 from table order by field | desc | asc 
		分组查询：
			gourp by field having condition
			创建分组，使用having过滤分组， 在group by 字句中使用with rollup， 多字段分组  group by 和order by 一起使用
			select filed,filed1 from table gourp by filed having count(filed1) > condition;<F8><F9>
			select filed,field1 from table gourp by filed with rollup;
		用Limit 限制查询结果的数量：select * from table limit n | n,m;

	集合函数查询：
		count(),	sum()	avg()	max()	min()	
	连接查询：
		内连接：inner join 
			select tb_1.field from table where tb_2.filed = tb_1.id;
		外连接：left join, right join
		复合条件连接查询：
		子查询：
	子查询：
	合并查询：
	为表和字段取别名：
	正则表达式查询：


