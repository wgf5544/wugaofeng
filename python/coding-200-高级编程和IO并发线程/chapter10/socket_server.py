import socket
import threading


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#
# server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #关闭后，可重用
server_socket.bind(('127.0.0.1', 8000))  # 绑定服务器端地址和端口号，端口号低于1024一般限制使用，用于标准服务，例如web80端口
server_socket.listen(5)  # 监听客户端建立连接请求，允许排队等待的数目为5


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024) #用一个最大字节数来作为参数，如果不确定，使用1024比较好。
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))

#获取从客户端发送的数据
#一次获取1k的数据
while True:


    try:
        '''
        这个方法接收客户端连接请求，
        会阻塞直到客户端的连接，
        返回客户端socket套接字和地址。
        建立一个连接后，等待下一个连接，通常使用无限循环实现。
        
        '''
        sock, addr = server_socket.accept()
    except KeyboardInterrupt:
        server_socket.close()
        #sock.close()
        exit(0)

    #用线程去处理连接(用户)后的操作请求
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()


