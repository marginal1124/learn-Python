#UDP  Server
#UDP 协议是不可靠协议，不需要建立连接。只需要对方的IP 地址和端口号就可以直接发送数据
#这样速度比较快

import  socket

#1,首先绑定端口号--这里SOCK_DGRAM 指定了UDP 类型
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))

print('build  UDP  on 9999')
#不需要监听建立连接，而是直接接受来自任何客户端的数据
while  True:
	#接受数据
	data,addr = s.recvfrom(1024)
	print('Recived  from %s:%s'%addr)
	#这里因为不是连接的所以 sendto 需要address才可以确定接收方
	s.sendto(b'hello,%s'+data,addr)