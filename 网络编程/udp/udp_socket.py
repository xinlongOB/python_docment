# 发送数据
"""
import socket

def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #可以使用套接字收发数据
    #udp_socket.sendto("hello",("IP",port))
    #第一个参数是发送的字符串，第二个是对方的IP和端口    ip和端口是字符串
    #udp_socket.sendto(b"hello",("192.168.1.41",8080))    #b  表示转为字节  u代表Unicode
    #或者写成这种方式
    data = input("请输入要发送的数据：")
    udp_socket.sendto(data.encode("utf-8"), ("192.168.1.41", 8080))
    #接收用户的输入数据  然后.encode转为utf-8

    #关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
"""

import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 可以使用套接字收发数据
    # udp_socket.sendto("hello",("IP",port))
    # 第一个参数是发送的字符串，第二个是对方的IP和端口    ip和端口是字符串
    # udp_socket.sendto(b"hello",("192.168.1.41",8080))    #b  表示转为字节  u代表Unicode
    # 或者写成这种方式

    # 发送方可以不绑定端口    接收方必须绑定端口
    local_addr = ('', 7890)  # ip地址和端口号，ip一般不用写，表示本机的任何一个IP
    udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip以及port
    while True:

        data = input("请输入要发送的数据：")
        if data == "exit":
            break

        udp_socket.sendto(data.encode("utf-8"), ("192.168.1.41", 8080))
        # 接收用户的输入数据  然后.encode转为utf-8

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

# 接收数据
"""
import socket
def main():
    #1、创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2、绑定一个本地信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('',7788)   #ip地址和端口号，ip一般不用写，表示本机的任何一个IP
    udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip以及port
    #3、等待接收对方发送的数据   recv_data这个变量中存储的是一个元祖(接收到的数据，(ip,port))
    recv_data = udp_socket.recvfrom(1024)  # 1024 表示本次接收的最大字节数
    recv_msg = recv_data[0]   # 存储接收到的数据
    send_addr = recv_data[1]    # 存储发送方的地址信息
    #4、打印接收到的数据
    #print("%s:%s" % (str(send_addr),recv_msg))   #打印地址：数据   需要把地址转换为str类型
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))
        # 打印地址：数据   需要把地址转换为str类型   因为Windows的默认编码是gbk  所以解码需要指定gbk
        # 在ubuntu 解码需要指定utf-8
    #5、关闭套接字
    udp_socket.close()
if __name__ == '__main__':
    main()
"""
