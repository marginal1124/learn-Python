
#连接服务端
import socket 

#客户端：
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
print(s.recv(1024))

for data  in [b'Mary',b'Tracy',b'Sarah']:
	#发送数据
	s.send(data)
	print(s.recv(1024))
s.send(b'exit')
s.close()