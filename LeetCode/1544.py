"""
import socket

def server_send(client_name):
    recv_date = client_name.recv(1024)
    print(recv_date)
    response = "HTTP/1.1  200 OK \r\n"
    response += "\r\n"
    response += "<h1>test</h1>"
    client_name.send(response.encode("utf-8"))
    client_name.close()

def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定端口和IP
    tcp_socket.bind(("192.168.1.41", 8080))
    # 3、开启监听
    tcp_socket.listen(128)
    # 4、接收请求
    while True:
        client_name, client_addr = tcp_socket.accept()
        # 5、接收消息并给客户端返回消息
        server_send(client_name)
    # 关闭socket
    tcp_socket.close()


if __name__ == "__main__":
    main()
"""
test = "test\r\n"
test += "nishi"
print(test)
