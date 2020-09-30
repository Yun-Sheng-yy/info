import socket
import machine as m


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp_server_socket用来监听客户端
    tcp_server_socket.bind(("", 8888))
    tcp_server_socket.listen(128)
    led14 = m.Pin(14, m.Pin.OUT)
    led2 = m.Pin(2, m.Pin.OUT)
    led2.value(0)
    led14.value(0)
    while True:
        print("------1-------")
        new_clint_socket, client_socket = tcp_server_socket.accept()
        print(client_socket)  # 是客户端信息
        recv_date = new_clint_socket.recv(1024).decode()
        print(recv_date)
        new_clint_socket.close()
        if recv_date == "quit":
            print("kankanakn")
            break
        elif recv_date == "1":
            led2.value(1)
        elif recv_date == "2":
            led2.value(0)
        elif recv_date == "3":
            led14.value(1)
        elif recv_date == "4":
            led14.value(0)
    # 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
