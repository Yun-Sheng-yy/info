import socket


# 相当于设置一个套接字来监听，监听到之后创建一个新的套接字来接收和回复数据
def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp_server_socket用来监听客户端

    # 2.插入手机卡（绑定本地信息）
    tcp_server_socket.bind(("", 8888))

    # 3.将手机设置为正常响铃模式（让默认的套接字由主动变为被动  listen）
    tcp_server_socket.listen(128)

    while True:
        print("------1-------")
        # 4.等待别人电话到来（等待客户端链接 accept）返回的是一个元组 之后拆包 第一个数据为创建的新套接字用来发送和接收消息，第二个为用户的信息
        new_clint_socket, client_socket = tcp_server_socket.accept()  # new_clint_socket用来接收数据和发送数据

        print(client_socket)  # 是客户端信息
        # 接收客户端发送过来的请求(数据） 一次只能接收1024
        recv_date = new_clint_socket.recv(1024).decode()
        print(recv_date)
        new_clint_socket.close()
        if recv_date == "1":
            print("kankanakn")
            break

    # 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
