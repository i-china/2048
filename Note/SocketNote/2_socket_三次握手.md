```
 @Author : Hale Lv
 @Created Time : 2019-09-02 09:45:17
 @Description : 
```

## 图解TCP数据报结构以及三次握手
	TCP： Transmission Control Protocol，传输控制协议。 一种面向连接的、可靠的、基于字节流的通信协议，数据在传输前要建立连接，完毕后要断开连接
	客户端在收发数据前要使用connect 函数和服务器建立连接，建立连接的目的是保证IP地址、端口、物理链路等正确无误，为数据的传输开辟通道
	TCP建立连接时要传输三个数据包，俗称：三次握手 Three-way Handshaking ：
		[Shake 1]套接字A： "你好，套接字B，我这里有数据包传给你，建立连接吧"
		[Shake 2]套接字B："好的，这边已经准备就绪"
		[Shake 3]套接字C："谢谢你受理我的请求"
		TCP三次握手:![三次握手](http://c.biancheng.net/uploads/allimg/190219/1155315343-0.jpg)
		图片中带阴影的字段说明：
			1. 序号： Seq： Sequence Number ： 序号占32位，用来识别从计算机A发送到计算机B的数据包的序号，计算机发送数据时对此进行标记
			2. 确认号：Ack：Acknowledge Number： 确认号占32位， 客户端和服务器端都可以发送， Ack=Seq+1
			3. 标志位： 每个标志位占用1Bit， 共有6个，分别为：URG、ACK、PSH、RST、SYN、FIN，具体含义：
				URG： 紧急指针urgent pointer 有效
				ACK： 确认序号有效
				PSH： 接收方应该尽快将这个报文交给应用层
				RST： 重置连接
				SYN： 建立一个连接
				FIN： 断开一个连接
				Seq 是 Sequence 的缩写，表示序列； Ack 是 Acknowledeg 缩写，表示确认； SYN 是 Synchronous 的缩写， 愿意是 同步的， 表示建立同步连接； FIN是Finish的缩写，表示完成
	
		连接的建立(三次握手)
			使用Connect 建立连接
			Three-hand:![Hands](http://c.biancheng.net/uploads/allimg/190219/1155312401-1.jpg)
			客户端调用socket 函数创建套接字后，因没建立连接，所以套接字处于CLOSED状态，服务器调用listen函数后，套接字进入LISTEN状态，开始监听客户端请求
			客户端开始发起请求：
				1. 当客户端调用connect 函数后，TCP协议会组建一个数据包，并设置SYN标志位，表示该数据包用来建立同步连接的，同时生成一个随机数字1000， 填充 序号Seq 字段，表示该数据包的序号。完成这些工作，开始想服务器端发送数据包，客户端进入SYN-SEND状态
				2. 服务器端收到数据包，检测到已经设置了SYN标志位， 检测到是客户端发来的建立连接的请求包，服务器也组建一个数据包， 并设置SYN和ACK标志位，SYN表示该数据包用来建立连接，ACK用来确认收到刚才客户端发送的数据包
				服务器生成一个随机数2000，填充 序号 Seq 字段，2000 和客户端数据包没有关系
				服务器将数据包发出，进入SYN-RECV状态
				3. 客户端收到数据包，检测到已经设置 SYN 和ACK 标志位， 检测到服务器发来的 确认包， 客户端检测 确认号 Ack 字段，看值是否为1000+1，如是说明连接成功
				客户端将数据包发出，进入ESTABLISED状态，表示连接已经成功建立
				4. 服务器端收到数据包，检测到已经设置ACk标志位，知道是客户端发来的 确认包，服务器会检测 确认号Ack字段， 看值是否为2000+1，如是说明连接建立成功，服务器进入ESTABLISED状态
				至此，客户端和服务器都进入ESTABLISED状态，连接建立成功，接下可收发数据
		最后的说明：
			三次握手的关键是要确认对方收到了自己的数据包，目标就是通过 确认号 Ack 字段实现的，计算机会记录下自己发送的数据包序号Seq，待收到对方的数据包后，检测 确认号Ack字段，看Ack = Seq + 1 是否成立， 如成立说明对方正确收到了自己的数据包

### TCP数据的传输过程
	Ack 号  = Seq号 + 传递的字节数 + 1
	重传超时事件 RTO ， Retransmission Time Out
	重传次数
		
### TCP四次握手断开连接
	[More](http://c.biancheng.net/view/2353.html)

#### shotdown 函数： 优雅地断开TCP连接
	[More](http://c.biancheng.net/view/2354.html)

### Socket 实现文件传输
	Client 从Server 下载一个文件并保存到本地
	需注意：
		1. 文件大小不确定该，调用一次write /send 函数不能完成文件内容的发送，接收数据也同样
		解决方案： 可使用while 循环：
			int nCount;
			while(nCount = fread(buffer, 1, BUF_SIZE, fp)) > 0 {
				send(sock, buffer, nCount, 0);
			}	
			// Client
			int nCount;
			while((nCount = recv(clntSock, buffer, BUF_SIZE, 0)) > 0 ) {
				fwrite(buffer, nCount, 1, fp);
			} 
			[More](http://c.biancheng.net/view/2355.html)

###		网络数据的大小端问题
			大端序和小端序
				
			网络字节序转换函数

	gethostbyname: 通过域名获取IP地址
		通过域名获取IP地址
		[More](http://c.biancheng.net/view/2359.html)


