#TCP Server

import socket, threading,time

#服务器需要绑定一个端口并监听来自客户端的连接，并通过socket与客户端建立Socket 连接

#服务器地址，服务器端口，客户端地址，客户端端口 4 项来确定唯一的一个Socket

#服务器为了响应不同的用户，每个连接都需要新的进程或线程来处理

#1，创建Socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2,绑定要监听的地址和端口
#这里bind 接受一个argument
s.bind(('127.0.0.1',9999))

#3,监听端口，传入的参数指定等待连接的数量
s.listen(5)
print('waiting for  connecting...')

#4,服务器通过socket的accept() 方法等待客户的连接

# 调用accept()方法时，socket进入waiting 状态。客户请求连接时，方法建立连接并返回服务器
# accept 方法返回含有两个元素的元组，形如（connection,address）,即新的socket对象和客户的地址

#这里可以看出服务器端是一直在等待的状态
while  True:
	#接受一个新连接
	sock,addr = s.accept()
	#  之前把 tcplink 方法定义在了下面，一直提示 tcplink is  not  defined.....
	def tcplink(sock, addr):
	#5, 处理阶段，服务器与客户端通过recv,send 方法进行通信
		print('Accpet new connection from %s:%s...' %addr)
		sock.send(b'welcome')
		while True :
			#接收数据，进行打印，并发送数据
			data = sock.recv(1024)
			print('data:',data)
			time.sleep(1)
			if not data or data.decode('utf-8')=='exit':
				break
			sock.send(('hello,%s'%data).encode('utf-8'))
		sock.close()
		print('Connection from %s:%s closed' %addr)


	#创建新线程,每个连接都需要创建新线程，否则线程处理过程中无法接受其他客户端连接
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()

	



