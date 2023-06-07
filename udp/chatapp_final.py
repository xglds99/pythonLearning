import json
import signal
import socket
import sys
import threading
import time
from queue import Queue

args = sys.argv
clients_map = dict()
groups_map = dict()
BUFSIZ = 8192


def send_msg(UDPCliSock, own_client_name, queue, SERVER_ADDR):
    global groups_map
    online_clients_map = queue.get(timeout=2)
    while True:
        ##step.1##
        if not queue.empty():
            online_clients_map = queue.get(timeout=2)
        data = input('>>> ')
        if data == 'ctrl+c':
            print("exit.")
            break
        user_msg = data.split(' ')
        if not queue.empty():
            online_clients_map = queue.get(timeout=2)
        if user_msg[0] == 'send':
            chat_client_name = user_msg[1]
            if chat_client_name in online_clients_map and online_clients_map[chat_client_name][1] == 1:
                to_addr = (online_clients_map[chat_client_name][0][0], online_clients_map[chat_client_name][0][1])
                UDPCliSock.sendto(bytes("private#@" + own_client_name + "#@" + ' '.join(user_msg[2:]), 'utf-8'),
                                  to_addr)
                # start_time = time.time()
                is_recv = False
                # while (time.time() - start_time) < 0.5:
                time.sleep(0.5)
                if not queue.empty():
                    ack = queue.get(timeout=0.5)
                    if ack == chat_client_name:
                        # Acknowledgment received
                        is_recv = True
                        print(f">>> [Message received by <{chat_client_name}>.]")
                if not is_recv:
                    print(f">>> [No ACK from <{chat_client_name}>, message not delivered]")
                if not queue.empty():
                    online_clients_map = queue.get(timeout=2)
            else:
                print(f">>> {chat_client_name} is offline")
        elif user_msg[0] == 'dereg':
            UDPCliSock.sendto(bytes("dereg#@" + own_client_name, 'utf-8'), SERVER_ADDR)
            # wait 500msc and retry 5 times
            time.sleep(2)
            for i in range(5):
                if not queue.empty():
                    ack = queue.get()
                    if ack == 'deregrecv':
                        print(">>> [You are Offline. Bye.]")
                        sys.exit(0)
            print(">>>  [Server not responding]")
            print(">>>  [Exiting]")
        elif user_msg[0] == 'create_group':
            group_name = user_msg[1]
            UDPCliSock.sendto(bytes(user_msg[0] + "#@" + group_name + "#@" + own_client_name, 'utf-8'), SERVER_ADDR)
            time.sleep(0.5)
            is_ack = False
            if not queue.empty():
                ack = queue.get(timeout=0.5)
                is_ack = True
                if ack == 'success':
                    print(f">>> [Group {group_name} created by Server.]")
                elif ack == 'exist':
                    print(f">>> [Group {group_name} already exists.]")
            if not is_ack:
                print('>>> [Server not responding.]')
                print('>>> [Exiting]')
        elif user_msg[0] == 'list_groups':
            UDPCliSock.sendto(bytes("list_groups#@" + own_client_name, 'utf-8'), SERVER_ADDR)
            time.sleep(1)
            if not queue.empty():
                list_groups_map = queue.get(0.5)
                print('>>> [Available group chats:]')
                groups_map = list_groups_map
                for c in list_groups_map:
                    print(f'>>> <{c}>')
        elif user_msg[0] == 'join_group':
            group_name = user_msg[1]
            UDPCliSock.sendto(bytes("join_group#@" + group_name + "#@" + own_client_name, 'utf-8'), SERVER_ADDR)
            time.sleep(1)
            if not queue.empty():
                ack = queue.get(0.5)
                if ack == 'success':
                    print(f'>>> [Entered group <{group_name}> successfully]')
                    while True:
                        data = input(f'>>> (<{group_name}>)')
                        user_msg = data.split(' ')
                        command = user_msg[0]
                        if command == 'send_group':
                            message = user_msg[1]
                            # 发往服务端
                            UDPCliSock.sendto(
                                bytes("send_group#@" + group_name + "#@" + own_client_name + "#@" + message, 'utf-8'),
                                SERVER_ADDR)
                            time.sleep(0.5)
                            is_success = False
                            if not queue.empty():
                                ack = queue.get(timeout=0.5)
                                if ack == 'success':
                                    is_success = True
                                    print(f"\n>>> (<{group_name}>) [Message received by Server.]")
                            if not is_success:
                                print(f'\n>>> (<{group_name}>) [Server not responding.]')
                                print(f">>> (<{group_name}>) [Exiting]")
                        elif command == 'list_members':
                            UDPCliSock.sendto(bytes("list_members#@" + group_name + "#@" + own_client_name, 'utf-8'),
                                              SERVER_ADDR)
                            time.sleep(0.5)
                            is_success = False
                            if not queue.empty():
                                list_members = queue.get()
                                print(f"\n>>> (<{group_name}>) [Members in the group <{group_name}>:]")
                                for u in list_members:
                                    print(f">>> (<{group_name}>) <{u}>")
                                is_success = True
                            if not is_success:
                                print(f"\n>>> (<{group_name}>) [Server not responding.]")
                                print(f'>>> (<{group_name}>) [Exiting]')
                        elif command == 'leave_group':
                            UDPCliSock.sendto(bytes("leave_group#@" + group_name + "#@" + own_client_name, 'utf-8'),
                                              SERVER_ADDR)
                            time.sleep(0.5)
                            is_recv = False
                            if not queue.empty():
                                ack = queue.get()
                                is_recv = True
                                if ack == 'success':
                                    print(f">>> [Leave group chat <{group_name}>]")
                            if not is_recv:
                                print(">>> [Server not responding.]")
                                print(f'>>> (<{group_name}>) [Exiting]')
                            time.sleep(0.5)
                            if not queue.empty():
                                private_messages_store = queue.get()
                                if private_messages_store and len(private_messages_store) > 0:
                                    for msg in private_messages_store:
                                        m = msg.split('#@')
                                        print("\n>>> " + m[0] + " : " + m[1])
                            break
                        elif user_msg[0] == 'dereg':
                            UDPCliSock.sendto(bytes("dereg#@" + own_client_name, 'utf-8'), SERVER_ADDR)
                            # wait 500msc and retry 5 times
                            time.sleep(2)
                            for i in range(5):
                                if not queue.empty():
                                    ack = queue.get()
                                    if ack == 'deregrecv':
                                        print(">>> [You are Offline. Bye.]")
                                        sys.exit(0)
                            print(">>>  [Server not responding]")
                            print(">>>  [Exiting]")
                elif ack == 'fail':
                    print(f' >>> [Group <{group_name}> does not exist]')


def recv_msg(udp_client_socket, own_client_name, queue, SERVER_ADDR):
    global is_group_mode
    is_group_mode = False
    private_message_store = []
    while True:
        recv_info, addr = udp_client_socket.recvfrom(BUFSIZ)
        if not recv_info:
            break
        msg = recv_info.decode('utf-8')
        message = msg.split('#@')
        if message[0] == 'ACK':
            queue.put(message[1])
        elif message[0] == 'update':
            print('>>> [Client table updated.]')
            online_clients_map = json.loads(message[1])
            queue.put(online_clients_map)
        elif message[0] == 'private':
            udp_client_socket.sendto(bytes("ACK#@" + own_client_name, "utf-8"), addr)
            if is_group_mode:
                private_message_store.append(message[1] + "#@" + message[2])
            else:
                print("\n>>> " + message[1] + " : " + message[2])
        elif message[0] == 'dereg' and message[1] == 'recv':
            if message[2] == own_client_name:
                print(">>>" + own_client_name + "is exiting")
                queue.put('deregrecv')
                sys.exit(0)
        elif message[0] == 'create':
            print(message)
            if message[1] == 'exist':
                queue.put('exist')
            elif message[1] == 'success':
                queue.put('success')
        elif message[0] == 'list_groups':
            list_groups_map = json.loads(message[1])
            queue.put(list_groups_map)
        elif message[0] == 'join_group':
            if message[1] == 'success':
                queue.put('success')
                is_group_mode = True
            elif message[1] == 'fail':
                queue.put('fail')
        elif message[0] == 'group_message':
            group_name = message[1]
            sender = message[2]
            message = message[3]
            print(f'\n>>> (<{group_name}>) Group_Message <{sender}(sender client)>: <{message}>.')
            udp_client_socket.sendto(bytes("ACK", "utf-8"), SERVER_ADDR)
        elif message[0] == 'send_group':
            if message[1] == 'success':
                queue.put('success')
        elif message[0] == 'list_members':
            list_members = json.loads(message[1])
            queue.put(list_members)
        elif message[0] == 'leave_group':
            if message[1] == 'success':
                queue.put('success')
                is_group_mode = False
                time.sleep(0.2)
            if len(private_message_store) > 0:
                queue.put(private_message_store)


def server_input(UDPSerSock, ADDR):
    while True:
        data = input(">>> ")
        if data == 'ctrl+c':
            UDPSerSock.sendto(bytes("ctrl+c#@", 'utf-8'), ADDR)
            print(">>> Server is Offline")
            sys.exit(0)


def main():
    if len(args) == 3:
        if args[1] == "-s":
            HOST = "127.0.0.1"  # 主机号可为空白 HOST = ""
            PORT = int(args[2])
            ADDR = (HOST, PORT)  # 地址与端口
            UDPSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建udp服务器套接字
            UDPSerSock.bind(ADDR)  # 套接字与地址绑定-服务端特有
            print(">>> server is listening on")
            threading.Thread(target=server_input, args=(UDPSerSock, ADDR)).start()
            while True:
                data, addr = UDPSerSock.recvfrom(4096)
                client_msg = data.decode("utf-8")
                msg = client_msg.split('#@')
                if msg[0] == 'login':
                    client_name = msg[1]
                    if client_name in clients_map:
                        print("已经登录，无需重复上线")
                    else:
                        client_info = [addr, 1]  # 1表示在线， 0表示离线 2 群聊模式
                        clients_map[client_name] = client_info
                        print("{} is online,address is {}".format(data.decode(), addr))
                        UDPSerSock.sendto(bytes(">>> [Welcome, You are registered.]", 'utf-8'), addr)
                        clients = json.dumps(clients_map)
                        print(clients_map)
                        for c in clients_map:
                            UDPSerSock.sendto(bytes("update#@" + clients, 'utf-8'), clients_map[c][0])
                elif msg[0] == 'dereg':
                    recv_client_name = msg[1]
                    UDPSerSock.sendto(bytes("dereg#@recv#@" + recv_client_name, "utf-8"),
                                      clients_map[recv_client_name][0])
                    if recv_client_name in clients_map and clients_map[recv_client_name][1] == 1:
                        clients_map[recv_client_name][1] = 0
                        clients_map.pop(recv_client_name)
                        # 广播!
                        for c in clients_map:
                            if c != recv_client_name:
                                UDPSerSock.sendto(bytes("update#@" + json.dumps(clients_map), 'utf-8'),
                                                  clients_map[c][0])
                elif msg[0] == 'create_group':
                    group_name = msg[1]
                    group_creator = msg[2]
                    if group_name in groups_map:
                        print(f'>>> [Client {group_creator} created group {group_name} failed, group already exists]')
                        UDPSerSock.sendto(bytes("create#@exist", 'utf-8'), clients_map[group_creator][0])
                    else:
                        group = [group_creator]
                        groups_map[group_name] = group
                        print(f'>>> [Client {group_creator} created group {group_name} successfully')
                        UDPSerSock.sendto(bytes("create#@success", 'utf-8'), clients_map[group_creator][0])
                elif msg[0] == 'list_groups':
                    request_name = msg[1]
                    UDPSerSock.sendto(bytes("list_groups#@" + json.dumps(groups_map), 'utf-8'),
                                      clients_map[request_name][0])
                    print(f'>>> [Client {request_name} requested listing groups, current groups:]')
                    for g in groups_map:
                        print(f'>>> <{g}>')
                elif msg[0] == 'join_group':
                    group_name = msg[1]
                    request_name = msg[2]
                    if group_name in groups_map:
                        groups_map[group_name].append(request_name)
                        UDPSerSock.sendto(bytes("join_group#@success", 'utf-8'), clients_map[request_name][0])
                        print(f'>>> [Client <{request_name}> joined group <{group_name}>]')
                    else:
                        UDPSerSock.sendto(bytes("join_group#@fail", 'utf-8'), clients_map[request_name][0])
                        print(
                            f'>>> [Client <{request_name}> joining group <{group_name}> failed, group does not exist]')
                elif msg[0] == 'send_group':
                    group_name = msg[1]
                    sender = msg[2]
                    message = msg[3]
                    UDPSerSock.sendto(bytes("send_group#@success", 'utf-8'), clients_map[sender][0])
                    print(f">>> [Client <{sender}> sent group message: <{message}>]")
                    # 通知group其他用户
                    group_user_list = groups_map[group_name]
                    print(group_user_list)
                    for user in group_user_list:
                        if user != sender:
                            UDPSerSock.sendto(
                                bytes("group_message#@" + group_name + "#@" + sender + "#@" + message, 'utf-8'),
                                clients_map[user][0])
                            is_recv = False
                            time.sleep(0.5)
                            ack, a = UDPSerSock.recvfrom(8192)
                            if ack.decode('utf-8') == 'ACK':
                                is_recv = True
                            if not is_recv:
                                print(f'>>> [Client <{user}> not responsive, removed from group <{group_name}>]')
                elif msg[0] == 'list_members':
                    group_name = msg[1]
                    client_name = msg[2]
                    list_members = groups_map[group_name]
                    UDPSerSock.sendto(bytes("list_members#@" + json.dumps(list_members), 'utf-8'),
                                      clients_map[client_name][0])
                    print(f"\n>>> [Client <{client_name}> requested listing members of group <{group_name}>:]")
                    for u in list_members:
                        print(f'>>> <{u}>')
                elif msg[0] == 'leave_group':
                    group_name = msg[1]
                    client_name = msg[2]
                    groups_map[group_name].remove(client_name)
                    UDPSerSock.sendto(bytes("leave_group#@" + "success", 'utf-8'), clients_map[client_name][0])
                    print(f">>> [Client <{client_name}> left group <{group_name}>]")
                elif msg[0] == 'enter_group_mode':
                    client_name = msg[1]
                    UDPSerSock.sendto(bytes("enter_group_mode#@" + "success", 'utf-8'), clients_map[client_name][0])
                elif msg[0] == 'ctrl+c':
                    sys.exit(0)
    elif len(args) == 6:
        if args[1] == "-c":
            client_name = args[2]
            SERVER_HOST = args[3]  # 本机测试
            SERVER_PORT = int(args[4])  # 端口号
            CLIENT_PORT = int(args[5])  #
            BUFSIZ = 4096  # 接收消息的缓冲大小
            SERVER_ADDR = (SERVER_HOST, SERVER_PORT)
            queue = Queue()  # 实例化队列
            print(SERVER_ADDR)
            UDPCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建客户端套接字
            UDPCliSock.bind(("127.0.0.1", CLIENT_PORT))
            UDPCliSock.sendto(bytes("login#@" + client_name, 'utf-8'), SERVER_ADDR)
            data, addr = UDPCliSock.recvfrom(BUFSIZ)  # 接收客户端发来的字节数组,data.decode()='char',data.upper()='bytes'
            print(">>> Data Receive from Server {}.\n{}".format(addr, data.decode("utf-8")))
            # 每个客户端启两个线程，一个收，一个发
            send_thread = threading.Thread(target=send_msg, args=(UDPCliSock, client_name, queue, SERVER_ADDR))
            recv_thread = threading.Thread(target=recv_msg, args=(UDPCliSock, client_name, queue, SERVER_ADDR))
            send_thread.start()
            recv_thread.start()
    else:
        print(">>>Please follow the sample below")
        print(">>>server chatapp.py -s <port>")
        print(">>>client chatapp.py -c name server_ip server_port client_port")


if __name__ == '__main__':
    main()
