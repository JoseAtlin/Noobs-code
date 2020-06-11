import socket
import threading
from datetime import datetime


def start():
    s.listen()
    print("[LISTENING]...server : {}".format(SERVER))
    while 1:
        conn, addr = s.accept()
        thread = threading.Thread(target=client_server, args=(conn, addr))
        thread.start()
        conn_ip_dict[conn] = addr
        print("[ACTIVE CONNECTIONS] : ", threading.activeCount() - 1)


def client_server(conn, addr):
    print("[NEW CONNECTION] : {}".format(addr))
    while 1:
        msg_length = conn.recv(16).decode('utf-8')
        if msg_length:
            message_details = []                                            # [sender, receiver, message, time]
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            sender_length = conn.recv(4).decode('utf-8')
            sender_length = int(sender_length)
            sender = conn.recv(sender_length).decode('utf-8')
            receiver_length = conn.recv(4).decode('utf-8')
            receiver_length = int(receiver_length)
            receiver = conn.recv(receiver_length).decode('utf-8')
            time = datetime.now().strftime("%I:%M:%P")
            message_details.extend((sender, receiver, msg, time))
            server_messages.append(message_details)
            conn_name_dict[conn] = sender
            if msg == "DISCONNECT":
                print("[{}] : DISCONNECTED".format(addr))
                conn.close()
                del conn_name_dict[conn]
                break
            print(message_details)
            for socks in conn_name_dict:
                if conn_name_dict[socks] != sender:
                    if receiver == "EVERYONE":
                        socks.send('1'.encode('utf-8'))
                        s_l = len(sender)
                        s_l = str(s_l).encode('utf-8')
                        s_l += b' ' * (4 - len(s_l))
                        socks.send(s_l)
                        socks.send(sender.encode('utf-8'))
                        m_l = len(msg)
                        m_l = str(m_l).encode('utf-8')
                        m_l += b' ' * (16 - len(m_l))
                        socks.send(m_l)
                        socks.send(msg.encode('utf-8'))
                        socks.send(time.encode('utf-8'))
                    else:
                        if conn_name_dict[socks] == receiver:
                            socks.send('2'.encode('utf-8'))
                            s_l = len(sender)
                            s_l = str(s_l).encode('utf-8')
                            s_l += b' ' * (4 - len(s_l))
                            socks.send(s_l)
                            socks.send(sender.encode('utf-8'))
                            m_l = len(msg)
                            m_l = str(m_l).encode('utf-8')
                            m_l += b' ' * (16 - len(m_l))
                            socks.send(m_l)
                            socks.send(msg.encode('utf-8'))
                            socks.send(time.encode('utf-8'))
                else:
                    socks.send('3'.encode('utf-8'))                         # correct
                    socks.send("Message Delivered".encode('utf-8'))
                    socks.send(time.encode('utf-8'))


def client_receive():
    while 1:
        person = c.recv(1).decode('utf-8')
        if person == '1' or person == '2':
            s_l = c.recv(4).decode('utf-8')
            s_l = int(s_l)
            receiver = c.recv(s_l).decode('utf-8')
            m_l = c.recv(16).decode('utf-8')
            m_l = int(m_l)
            msg = c.recv(m_l).decode('utf-8')
            time = c.recv(8).decode('utf-8')
            print(receiver, '-' * 5, msg, '-' * 5, time)
            print()
        elif person == '3':
            msg = c.recv(17).decode('utf-8')
            time = c.recv(8).decode('utf-8')
            print("status : ", msg, '-'*5, time)
            print()


def client_send(receiver, msg):
    send_message = msg.encode('utf-8')
    receiver = receiver.encode('utf-8')
    sender = name.encode('utf-8')
    msg_length = len(send_message)
    msg_length = str(msg_length).encode('utf-8')
    msg_length += b' ' * (16 - len(msg_length))
    c.send(msg_length)
    c.send(send_message)
    sender_length = len(sender)
    sender_length = str(sender_length).encode('utf-8')
    sender_length += b' ' * (4 - len(sender_length))
    c.send(sender_length)
    c.send(sender)
    receiver_length = len(receiver)
    receiver_length = str(receiver_length).encode('utf-8')
    receiver_length += b' ' * (4 - len(receiver_length))
    c.send(receiver_length)
    c.send(receiver)


PORT = 6060
SERVER = socket.gethostbyname(socket.gethostname())
server_messages = []                                # [[sender, receiver , message, time],......]
conn_name_dict = {}                                 # {(connection : sender_name)......}
conn_ip_dict = {}                                   # {(connection : ip_address).......}


ch = int(input("1. Server\n2. Client\n"))
if ch == 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[SERVER STARTING]...")
    s.bind((SERVER, PORT))
    t = threading.Thread(target=start)
    t.start()
    t.join()
else:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((SERVER, PORT))
    th = threading.Thread(target=client_receive)
    th.start()
    name = (input("Enter Your Name : ")).upper()
    print("[CONNECTED] TO SERVER : {} AS {}".format(SERVER, name))

    while 1:
        print("Do you want to ::\n1.Broadcast\n2.Personal")
        print("To quit using Broadcast or Personal, type \"quit\"")
        option = int(input("Enter your Option : "))
        if option == 1:
            print("\n-----> Message Format ::\n-----> 1st line : Message\n")
        else:
            print("\n-----> Message Format ::\n-----> 1st line : Receiver's Name\n-----> 2nd line : Message\n")

        while 1:
            if option == 1:
                to_whom = "everyone".upper()
            else:
                to_whom = input().upper()
            if to_whom == "":
                continue
            if to_whom == "quit":
                break
            type_here = input()
            if type_here == "":
                continue
            if type_here == "quit":
                break
            client_send(to_whom, type_here)
