import socket
import threading
import time
import queue

client_queue = queue.Queue(99)

def recv_all(client_socket):
    msg = b''
    while True:
        temp = client_socket.recv(1024)
        if temp == b'':
            break
        msg += temp
    return msg
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s: socket.socket
s.bind(('localhost',8001))
s.listen(99)

def accept_queue():
    global client_queue
    print(f'listin thread: {threading.current_thread().name}')
    while True:
        client_socket, address = s.accept()
        client_queue.put({"client_socket":client_socket, "address":address})

def consumer():
    global client_queue
    thread_name=threading.current_thread().name
    print(f'consumer thread: {thread_name} start...')
    while True:
        if client_queue.empty():
            time.sleep(1)
            continue
        client_dict = client_queue.get()
        client_socket, address = client_dict['client_socket'], client_dict['address']
        msg = recv_all(client_socket)
        # print(f'{thread_name}, {client_socket}, {address}, {msg}')
        print(f'{thread_name} -- {msg}')

# try:
#     while True:
#         client_socket, adddress = s.accept()
#         print('accept')
#         time.sleep(30)
#         msg = recv_all(client_socket)
#         print(client_socket, adddress, msg)
            
# except KeyboardInterrupt:
#     print('End')

def main():

    try:
        print(f'main thread start...')
        threads=[]
        accept_thread=threading.Thread(target=accept_queue)
        threads.append(accept_thread)
        for _ in range(5):
            consumer_thread=threading.Thread(target=consumer)
            threads.append(consumer_thread)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print(f'main end')
main()