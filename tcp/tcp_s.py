import socket
import time
import os

if __name__ == '__main__':
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('127.0.0.1', 8888))
    tcp_server.listen(1024)
    BufferSize = 1024 * 10
    print('tcp_server listening ')
    tcp_socket, address = tcp_server.accept()
    print('连接到客户端' + str(address))
    print('server recv starting !!')
    file_size = tcp_socket.recv(1024).decode('utf-8')
    print(file_size)
    count = int(file_size)
    with open('xjtlu1.jpg', 'wb') as f:
        while count > 0:
            recv_bytes = tcp_socket.recv(BufferSize)
            f.write(recv_bytes)
            count -= len(recv_bytes)
    print('sever recv finished!')
    file_size = os.path.getsize('xjtlu1.jpg')
    file_size = str(file_size).encode("utf-8")
    tcp_socket.send(file_size)
    print('sever send starting!!')
    with open('xjtlu1.jpg', 'rb') as f1:
        while True:
            send_bytes = f1.read(BufferSize)
            if not send_bytes:
                break
            tcp_socket.sendall(send_bytes)
    print('sever send finished!!')
    time.sleep(0.001)
    tcp_socket.close()
    tcp_server.close()
