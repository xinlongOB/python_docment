"""
#使用同一个套接字进行收发数据
import socket

def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    #udp_socket.sendto("hello",("IP",port))
    #第一个参数是发送的字符串，第二个是对方的IP和端口    ip和端口是字符串
    #udp_socket.sendto(b"hello",("192.168.1.41",8080))    #b  表示转为字节  u代表Unicode
    #或者写成这种方式

    #获取对方的IP/PORT
    dest_ip = input("请输入对方的IP：")

    try:
        dest_port = int(input("请输入对方的端口:"))
    except :
        dest_port = int(input("请输入对方的端口:"))


    #发送方可以不绑定端口    接收方必须绑定端口
    local_addr = ('',7890)   #ip地址和端口号，ip一般不用写，表示本机的任何一个IP
    udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip以及port


    while True:

        data = input("请输入要发送的数据：")
        if data == "exit":
            break

        udp_socket.sendto(data.encode("utf-8"), (dest_ip, dest_port))
        #接收用户的输入数据  然后.encode转为utf-8

        #接收回的消息
        reve = udp_socket.recvfrom(1024)
        reve_data = reve[0]

        #套接字是一个可以同时收发数据的     打印对方回复 并转码
        print("对方回复 %s" % reve_data.decode("gbk"))

    #关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
"""

import socket


def send_msg(udp_socket):
    # 获取要发送的内容
    dest_ip = input("请输入对方的IP：")
    dest_port = int(input("请输入对方的端口："))
    send_data = input("请输入要发送的消息：")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1], recv_data[0].decode("utf-8"))))  # 如果接收ubuntu的消息是utf-8
    # 如果是Windows  需要的编码是 gbk


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(('', 7788))
    # 循环来进行处理事情
    while True:
        print("....聊天器.....")
        print("1：发送消息")
        print("2：接收消息")
        print("0：退出系统")
        op = input("请输入功能：")

        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收并显示
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("请输入正确的功能")


if __name__ == '__main__':
    main()
