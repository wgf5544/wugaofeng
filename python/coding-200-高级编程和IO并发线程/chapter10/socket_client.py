import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 创建客户端套接字
client_socket.setblocking(False) # 设置为非阻塞式
client_socket.connect(('127.0.0.1', 8000))  # 连接服务器
while True:
    re_data = input()
    client_socket.send(re_data.encode("utf8"))
    data = client_socket.recv(1024)
    print(data.decode("utf8"))

