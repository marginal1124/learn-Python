# TCP编程，连接sina  并将接收到的数据写入文件
#但是这里不知道为什么  33  行，split 之后只有一个数据，提示need more  than 1 value to unpack
#所以就把接受到的data 全部写入 sina.html。。但是打开后提示页面没有找到。不知道是什么问题
import socket

#创建一个socket
#AF_INET指定使用IPV4，SOCK_STREAM 指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接，网页服务器端口固定为80，这里参数是一个tuple
s.connect(("www.sina.com.cn",80))

#发送数据 （TCP建立的连接是双向通道，双方可以同时给对方发送数据）
s.send(b'GET /HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')

#接收数据
buffer = []
while True:
	#每次最多接受1K 字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

#关闭socket
s.close()

#将接受到的数据保存，打印
#后面的1 是指分隔num个子字符串，所以这是找到第一个\r\n 进行分割
#print(data)
#header，html = data.split(b'\r\n\r\n',1)

#print('header:',header.decode('gb2312'))

#把接受的数据写入文件
with open('sina.html','wb') as f :
	f.write(data)
print('html:',data.decode('gb2312'))