#UDP client
import  socket
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#不需要连接，直接通过sendto 发送给服务器端

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()