# import socket
# import tqdm
# import os
# import threading
#
# # 由客户端向服务器传数据，文件

import threading
import socket
import tqdm
import os
from time import ctime, sleep


def send(udp_socket):
    # 传输数据间隔符
    SEPARATOR = '<SEPARATOR>'
    # 服务器信息

    # 文件缓冲区
    Buffersize = 4096 * 10
    RecvSize = 4096 * 10
    # 传输文件名字
    filename = input('请输入文件名：')
    # 文件大小)
    file_size = os.path.getsize(filename)

    # 发送文件名字和文件大小，必须进行编码处理
    # s.sendto(f'{filename}{SEPARATOR}{file_size}'.encode(), ("127.0.0.1", 1234))
    udp_socket.send(f'{filename}{SEPARATOR}{file_size}'.encode('utf-8'))

    # 文件传输
    progress = tqdm.tqdm(range(file_size), f'发送{filename}', unit='B', unit_divisor=1024)

    with open(filename, 'rb') as f:
        # 读取文件
        for _ in progress:
            bytes_read = f.read(Buffersize)
            # print(bytes_read)
            if not bytes_read:
                print('exit退出传输，传输完毕！')
                udp_socket.sendall('file_download_exit'.encode('utf-8'))
                break
            # sendall 确保络忙碌的时候，数据仍然可以传输
            udp_socket.sendall(bytes_read)
            progress.update(len(bytes_read))

    with open("xjtlu2.jpg", 'wb') as f1:
        while True:
            bytes_recv = udp_socket.recv(RecvSize)
            if bytes_recv == b'file_download_exit':
                print('完成传输！')
                print(bytes_recv)
                break
            f1.write(bytes_recv)
    udp_socket.close()


if __name__ == '__main__':
    # address = str(input("请输入IP地址："))
    # port = int(input("请输入端口:"))
    address = '127.0.0.1'
    port = 1234
    # 创建socket链接
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.connect((address, port))
    print('与服务器连接成功')
    send(udp_socket)
    # t1 = threading.Thread(target=send, args=(udp_socket,))
    # t1.start()
    # t2 = threading.Thread(target=recv, args=(udp_socket,))
    # t2.start()
    # received(address, filename)
