# coding=utf-8
import socket


def main():
    while True:
        # 创建一个udp套接字   没有绑定端口  发消息时会看到不同的端口 动态端口
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 使用套接字收发数据
        # 对方的ip以及port
        # dest_address =
        send_data = input("请输入要发送的数据:")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("utf-8", errors="strict"), ("192.168.3.50", 7788))
        # 关闭套接字  errors="strict 不要也没问题encode要使用的编码
        udp_socket.close()


if __name__ == '__main__':
    main()
