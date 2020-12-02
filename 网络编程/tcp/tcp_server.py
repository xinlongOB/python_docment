"""
1、socket创建一个套接字
2、bind绑定ip和port
3、listen使用套接字变为可以被动连接
4、accept 等待客户端的连接
5、recv/send接收发送数据

import socket

def main():
    #  1、socket创建一个套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2、bind绑定ip和port
    tcp_server_socket.bind(("",11111))
    # 3、listen使用套接字变为可以被动连接
    tcp_server_socket.listen(128)

    # 4、accept 等待客户端的连接       accept 返回的是一个元祖  所以把返回值赋值给两个变量名
    # 监听套接字 负责等待新的客户端进行连接
    # accept 产生的新的套接字用来为客户端服务
    new_client_socket,client_addr = tcp_server_socket.accept()
    # 5、recv / send接收发送数据

    print("gogogo")
    print(client_addr)
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    new_client_socket.send("hahaha".encode("utf-8"))

    new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
"""
"""
1、socket创建一个套接字
2、bind绑定ip和port
3、listen使用套接字变为可以被动连接
4、accept 等待客户端的连接
5、recv/send接收发送数据

"""

# 循环等待接收客户端消息
import socket


def main():
    #  1、socket创建一个套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、bind绑定ip和port
    tcp_server_socket.bind(("", 11111))
    # 3、listen使用套接字变为可以被动连接    128 同一时间连接数
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        # 4、accept 等待客户端的连接       accept 返回的是一个元祖  所以把返回值赋值给两个变量名
        # 监听套接字 负责等待新的客户端进行连接
        # accept 产生的新的套接字用来为客户端服务
        new_client_socket, client_addr = tcp_server_socket.accept()
        # 5、recv / send接收发送数据

        print("一个新连接已经链接%s" % str(client_addr))

        # 循环多次  为一个客户服务
        while True:
            recv_data = new_client_socket.recv(1111111111)
            print("客户端发送消息%s " % str(recv_data.decode("gbk")))
            # 如果解堵塞 那么有两种方式：1、客户端发过来发过来数据   2、客户端调用close导致
            # 如果recv_data 有数据  就给客户端返回
            if recv_data:
                new_client_socket.send("hahaha".encode("utf-8"))
            else:
                break

        # 关闭本次连接的套接字
        new_client_socket.close()
        print("已经服务完毕，关闭本次连接")

    # 如果将监听套接字关闭了，那么将会导致不能再次等待客户端的到来，  即xxxx.accept 就会失败
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
