### 防火墙

防火墙配置文件： /etc/sysconfig/iptables

	打开22端口：
		iptables -A INPUT -p tcp --dport 22 -j ACCEPT 
	
		iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT 

	打开DNS服务端口：
		iptables -A INPUT -p udp --dport 53 -j ACCEPT 
		iptables -D INPUT n		//
		iptables -D OUTPUT n	//
		iptables -nL			//

			-A	： 追加一条规则
			-D  ： 删除一条规则
			-R	： 替换一条规则
			-I	： 插入一条规则
			-p  ： 协议
			-s	： 指定源地址
			-d	： 指定目标地址
			-i	： 指定入口网卡
			-o	： 指定出口网卡
			--sport	： 指定源端口
			--dport	： 指定目的端口
			-j	： 指定要进行的处理动作
			ACCEPT	： 将封包放行
			DROP	： 丢弃封包不予处理

Linux查看状态firewall、iptable

iptables 防火墙
	1. 基本操作
		状态：
			service iptables status
		停止：
		启动：
		重启：
		永久关闭：
		永久关闭后重启：

	2. 开启80端口
		vim /etc/sysconfig/iptables
			-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
		service iptables restart

firewall 防火墙
	1. 查看：
		systemctl status firewall
	2. 状态
		firewall-cmd --state 
	3. 开启、重启、关闭
		service firewalld start 
		service firewalld restart
		service firewalld stop 
	4. 查看防火墙规则
		firewalld-cmd --list-all
	5. 查询、开发、关闭端口
		查询端口是否开放
		firewall-cmd --query-port=8080/tcp
		开放80端口
		firewall-cmd --permanent --add-port=80/tcp
		移除端口
		firewall-cmd --permanent --remove-port=8080/tcp
		重启防火墙
		firewall-cmd --reload 
		
		firewall-cmd ： 
		--permanent ：表示设置为持久
		--add-port ： 标识添加的端口


service iptables save			//

service iptables restart		//

chkconfig iptables off			//
service iptables stop			//


	
























