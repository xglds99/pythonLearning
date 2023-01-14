import os
import socket

if __name__ == '__main__':
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(('127.0.0.1', 8888))
    BufferSize = 1024 * 10
    SendSize = 1024 * 1024
    filename = input('请输入文件名:')
    print('client send starting!!')
    file_size = os.path.getsize(filename)
    file_size = str(file_size).encode('utf-8')
    tcp_client.send(file_size)
    with open(filename, 'rb') as f:
        while True:
            read_bytes = f.read(BufferSize)
            if not read_bytes:
                break
            tcp_client.send(read_bytes)
    print('client send finished!')
    file_size = tcp_client.recv(1024).decode("utf-8")
    count = int(file_size)
    print('client recv starting!')
    with open('xjtlu2.jpg', 'wb') as f1:
        while count > 0:
            recv_bytes = tcp_client.recv(BufferSize)
            f1.write(recv_bytes)
            count -= len(recv_bytes)
    print('client recv finished!')
    tcp_client.close()
