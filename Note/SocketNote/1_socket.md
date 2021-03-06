```
 @Author : Hale Lv
 @Created Time : 2019-08-29 21:26:32
 @Description : 
```
## Socket 

	socket： 套接字，通信技术就是两台联网的计算机之间交换数据的技术。
		原意是插座，是计算机之间进行通信的一种约定或一种方式。 通过socket，计算机可接收、可发送数据	
		典型应用：web服务器和浏览器：浏览器获取用户输入的URL，向服务器发起请求，服务器分析接收到的URL，将对应的网页内容返回给浏览器，浏览器再经过解析和渲染，将文字、图片、视频元素呈现给用户
		为了表示和区分已经打开的文件，Linux给每个文件分配一个ID整数，被称为：文件描述符File Descriptor如：	
		0： 输入文件 stdin，键盘
		1:	输出文件 stdout ，显示器
			网络连接也是一个文件，也有文件描述符
				socket() 创建网络连接，打开一个网络文件，返回值即文件描述符。有文件描述符，即可使用普通的文件操作函数来传输数据，如：
					read() ：读取从远程计算机传来的数据
					write()：向远程计算机写入数据
		
		Windows 系统中的socket 
			Windows：文件句柄		
			Liunx ： 文件描述符

###	套接字的类型，socket的类型
		有很多如：DARPA Internet 地址： Internet套接字、 本地节点的路径名：Unix套接字，CCITT X.25地址：X.25套接字等。
		Internet 套接字：最常用、具有代表性
		Internet套接字的数据传输方式：
			1. 流格式套接字 SOCK_STREAM
				流格式套接字：Stream Sockets 也叫"面向连接的套接字"，使用SOCK_STREAM 表示
				SOCK_STREAM： 是一种可靠、双向的通信流数据。可准确无误到达另一台计算机，可损坏或丢失、可重新发送
				SOCK_STREAM 的特征：
					1. 数据在传输过程中不会消失
					2. 数据是按照顺序传输的
					3. 数据的发送和接收不是同步的。也成 不存在数据边界
					使用TCP协议 The Transmission Control Protocol，传输控制协议，TCP控制数据按照顺序到达并且没有错误
					IP Internet Protocol 网络协议，控制数据如何从源头到达目的地，即路由
			2. 数据报格式套接字 SOCK_DGRAM
				数据报格式套接字 Datagram Sockets 也叫 无连接的套接字，使用SOCK_DGRAM表示
					只管传输数据，不做数据校验，如损坏或丢失，不补救，无法重传。
				SOCK_DGRAM 的特征：
					1. 强调快速传输而非传输顺序
					2. 传输的数据肯跟丢失或损坏
					3. 限制每次传输的数据大小
					4. 数据的发送和接收是同步的，存在数据边界
				SCOK_DGRAM：是一种不可靠、不按传序传递的、以追求速度为目的的套接字
					使用UDP协议 User Datagram Protocol 用户数据报协议

	面向连接和无连接的套接字
		流格式套接字Stream Sockets： 面向连接的套接字，基于TCP协议
		数据报格式套接字 Datagram Sockets： 无连接的套接字，基于UDP协议
			无连接的套接字
				每个数据包可选择不同的路径
				每个数据包之间是独立的
			面向连接的套接字
				路径是由路由器维护的，所有路由器都要存储该路径的信息
		优缺点：
			无连接套接字传输效率高，不可靠、丢失数据报、捣乱数据
			有连接套接字可靠、传输效率低，耗费资源
		有连接的套接字TCP：HTTP、FTP等
		无连接的套接字UDP：DNS、即时聊天工具等
	
###	OSI 网络七层模型
		OSI模型:Open System Interconnection： 开发式系统互联
			七层：物理层、数据链路层、网络层、传输层、会话层、表示层、应用层
			TCP/Ip 模型： 网络接口层、网络层、传输层、应用层
				网络接口：针对不同物理网络的连接形式的协议，如：Ethernet、FDDI、ATM
				网络层：负责数据的传输，路径及地址选择，常用协议：IP ARP(地址解析协议)
				传输层：确认数据传输及进行纠错处理，常用协议：TCP、UDP(用户数据报协议)
				应用层：各种服务及应用程序通过该层利用网络，常用协议：HTTP、FTP、SMTP(简单邮件传输协议)等
				发送数据包时，程序或软件是通过应用层访问网络，产生的数据会一层一层往下传输，到最后的王略接口层，通过网线发送到网上，每传一层，协议增加一层包装，比原始数据多了四层包装。
				接收数据包时：从网络接口层一层一层网上传，每传一层就拆开一层包装，到最后的应用层，最原始的数据。
				socket：在传输层的基础上，使用TCP/IP协议，不能访问网页，访问网页需要HTTP协议
			计算机通信的原则：
				1. 同一层次进行通信，
				2. 功能必须相同
				3. 数据只能逐层传输，不能跃层
				4. 可使用下层提供的服务，并向上层提供服务

	TCP/IP协议族
		协议： Protocol 是网络通信过程中的约定或合同，双方必须都遵守才能正常收发数据。 协议是一种规范，通信双方需使用同一协议才能通信，
		TCP/IP模型包含 TCP、IP、UDP、Telnet、FTP、SMTP等
		TCP/UDP:![SOCKET](http://c.biancheng.net/uploads/allimg/190126/1-1Z126104435N0.gif)
	开放式系统 Open System
		以多个标准为依据设计的系统称为开放式系统
	
####	IP、MAC和端口号 - 网络通信中确认身份信息的三要素
		IP地址
			是 Internet Protocol Address ，网际协议地址
		Mac地址 
			是 Media Access Control Address , 媒体访问控制地址，称为局域网地址LAN Address，以太网地址 Ethernet Address 或 物理地址Physical Address
		端口号
			Port Number 为每个网路程序分配一个独一无二的端口号
			是一个虚拟的、逻辑上的概念

###	Linux 下的Socket 演示程序
		服务器端代码server.cpp:
			#include <stdio.h>
			#include <string.h>
			#include <stdlib.h>
			...
			int main() {
				int serv_sock = socket(AF_INET,SOCK_STREAM,IPPROPT_TCP);
				struct sockaddr_in serv_addr;

			}
		...
		[SOCKET CPP](http://c.biancheng.net/view/2128.html)
		
###	WSAStartup() 函数以及DLL的加载
		[More](http://c.biancheng.net/view/2130.html)

### Socket() 函数用法：创建套接字
		Linux 下的Socket函数
		使用<sys/socket.h> 头文件中socket函数创建套接字，原型为：
		int socket(int af, int type, int protocol);
			1. af: 地址族 Address Family， IP地址类型，常用AF_INET：表示IPv4地址 和 AF_INET6：表示IPv6地址，
			2. type 为数据传输方式/套接字类型，常用： SOCK_STREAM 流格式套接字/面向连接套接字 和 SOCK_DGRAM 数据套接字/无连接的套接字
			3. protocol 表示传输协议，常用： IPPROTO_TCP 和 IPPROTO_UDP
		TCP：
			int tcp_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
		UDP:
			int udp_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
		将 protocol的值设为0， 系统可自动推演出使用的协议：
			int tcp_socket = socekt(AF_INET, SOCK_STREAM, 0)	// TCP
			int udp_socket = socket(AF_INET, SOCK_DGRAM,  0)	// UDP

		bind() 和 connect()函数：绑定套接字并建立连接
			使用 bind函数将套接字与特定的IP地址和端口绑定起来，
			bind 函数原型：
				int bind(int sock, struct sockaddr * addr, socklen_t addrlen);	//linux
				int bind(SOCKET sock, const struct sockaddr * addr, int addrlen);	// windows
				[More](http://c.biancheng.net/view/2344.html)

		listen accept : 让套接字进入监听状态并响应客户端请求
			listen 函数：让套接字进入被监听状态，原型：
				int listen(int sock, int backlog);	//linux
				int listen(SOCKET sock, int backlog);	// windows
					sock: 进入监听状态的套接字， backlog： 请求队列的最大长度

		[More](http://c.biancheng.net/view/2345.html)

####	send()/recv()和write()/read(): 发送数据和接收数据
		Linux 下数据的接收和发送
			[More](http://c.biancheng.net/view/2346.html)		
		
	
