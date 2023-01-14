import socket
from time import sleep

import tqdm
import os
import threading


# 使用UDP传输视频，全双工，但只需一方接，一方收即可

# 设置服务器的ip和 port
# 服务器信息
# sever_host = '127.0.0.1'
# sever_port =1234
def create_socket(sever_host, sever_port) -> socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((sever_host, sever_port))
    return s


def recvived(udp_socket):
    # 传输数据间隔符
    SEPARATOR = '<SEPARATOR>'
    # 文件缓冲区
    Buffersize = 4096 * 10
    SendSize = 4096 * 10

    print('准备接收新的文件...')
    recv_data = udp_socket.recvfrom(Buffersize)
    recv_file_info = recv_data[0].decode('utf-8')  # 存储接收到的数据,文件名
    print(f'接收到的文件信息{recv_file_info}')
    c_address = recv_data[1]  # 存储客户的地址信息
    # 打印客户端ip
    print(f'客户端{c_address}连接')
    # recv_data = udp_socket.recv()
    # 接收客户端信息
    # received = udp_socket.recvfrom(Buffersize).decode()
    filename, file_size = recv_file_info.split(SEPARATOR)
    # 获取文件的名字,大小
    filename = os.path.basename(filename)
    file_size = int(file_size)

    # 文件接收处理
    progress = tqdm.tqdm(range(file_size), f'接收{filename}', unit='B', unit_divisor=1024, unit_scale=True)

    with open('xjtlu1.jpg', 'wb') as f:
        for _ in progress:
            # 从客户端读取数据
            bytes_read = udp_socket.recv(Buffersize)
            # 如果没有数据传输内容
            # print(bytes_read)
            if bytes_read == b'file_download_exit':
                print('完成传输！')
                print(bytes_read)
                break
            # 读取写入
            f.write(bytes_read)
            # 更新进度条
            #progress.update(len(bytes_read))
    print("服务端发送数据")
    with open('xjtlu1.jpg', 'rb') as f1:
        while True:
            bytes_send = f1.read(SendSize)
            if not bytes_send:
                print('exit退出传输，传输完毕1111！')
                udp_socket.sendall('file_download_exit'.encode('utf-8'))
                break
            udp_socket.sendall(bytes_send)
    udp_socket.close()



if __name__ == '__main__':
    # address = ("127.0.0.1", 1234)
    # address = str(input("请输入IP地址："))
    # port = int(input("请输入端口:"))
    address = "127.0.0.1"
    port = 1234
    udp_socket = create_socket(address, port)
    # t1 = threading.Thread(target=recvived, args=(udp_socket,))
    # t1.start()
    recvived(udp_socket)
    # send(address)
