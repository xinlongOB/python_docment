"""
TCP协议--传输控制协议 是一种面向连接的、可靠的、基于字节流的传输层通信协议

tcp通信需要经过 创建连接、数据传送、终止连接  三个步骤

"""
import socket


def main():
    # 创建tcp 套接字socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    # tcp_socket.connect(("192.168.1.1",7780))
    server_ip = input("请输入服务器IP：")
    server_port = int(input("请输入服务器port："))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    # 发送数据    tcp 使用send 发送消息
    while True:
        send_data = input("请输入要发送的数据：")
        if send_data:
            tcp_socket.send(send_data.encode("gbk"))
        else:
            break
    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
