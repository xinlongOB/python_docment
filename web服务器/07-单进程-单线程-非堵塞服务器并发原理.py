import socket
import time

client_list = list()  # client_list = []


def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.bind(("192.168.0.114", 7777))
    tcp_client.listen(128)

    # 所有的套接字默认都堵塞  想要不堵塞添加 .setblocking(False)
    tcp_client.setblocking(False)  # 设置套接字为非堵塞的方式
    while True:

        time.sleep(0.5)
        # 设置为非堵塞后   没有连接的话会产生异常  所以添加try  主动抛出
        try:
            new_socket, new_addr = tcp_client.accept()
        except Exception as ret:
            print("----无新客户端连接----")
        else:
            print("----只要没有产生异常，那么意味着来了一个新的客户端连接----")
            new_socket.setblocking(False)  # 设置套接字为非堵塞的方式
            client_list.append(new_socket)
        for c_list in client_list:
            try:
                request = c_list.recv(1024)
            except Exception as ret:
                print(ret)
                print("---客户端未发送数据---")
            else:
                if request:
                    # print("---客户端已发送数据---")
                    print(request)
                    response = "HTTP/1.1 200 OK \r\n"
                    response += "\r\n"
                    # 2.2 、准备发送给浏览器的数据---boy
                    response += "<h1>who are you</h1>"
                    c_list.send(response.encode("utf-8"))
                    # 如果这里不关闭套接字  第一个客户端连接后会有一个报错--[WinError 10035] 无法立即完成一个非阻止性套接字操作。
                    # 第二次如果没有发送数据  recv如果无法接受到数据, 就会报异常
                    client_list.remove(c_list)
                    c_list.close()
                else:
                    # 3、 关闭套接字
                    client_list.remove(c_list)
                    c_list.close()

    tcp_client.close()


if __name__ == "__main__":
    main()
