#
import socket
import threading


def recv_date(udp_socket):
    # 接收数据
    while True:
        recv = udp_socket.recvfrom(1024)
        print(recv)


def send(udp_socket, dest_ip, dest_port):
    # 发送数据
    while True:
        data = input("请输入要发送的内容：")
        udp_socket.sendto(data.encode("utf-8"), (dest_ip, dest_port))


def main():
    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2、绑定本地信息
    udp_socket.bind(("192.168.1.51", 7890))
    # 3、定义要发送的端口和IP
    dest_ip = input("请输入对方的IP：")
    dest_port = int(input("请输入对方的PORT："))

    t1 = threading.Thread(target=recv_date, args=(udp_socket,))
    t2 = threading.Thread(target=send, args=(udp_socket, dest_ip, dest_port))

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
