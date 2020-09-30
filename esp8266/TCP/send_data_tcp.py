import socket


def main():
    # 1.创建套接字
    # tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    # tcp_socket.connect(("192.168.3.50", 8888))
    # server_ip = input("请输入要链接的服务器")

    # server_port = int(input("请输入链接服务器端口"))
    # server_addr = (server_ip, server_port)
    # tcp_socket.connect(server_addr)

    # 3.发送数据
    while True:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_socket.connect(("192.168.3.50", 8888))
        except:
            tcp_socket.close()
            break
        send_date = input("请输入要发送的数据")

        tcp_socket.send(send_date.encode("utf-8"))
        if send_date == "quit":
            tcp_socket.close()
            break
        # 4.关闭套接字
        tcp_socket.close()


if __name__ == "__main__":
    main()
