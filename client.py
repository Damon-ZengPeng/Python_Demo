import socket
import threading
import random


msgs = ['Hello','Bye','Good', 'Hah']


def sendMsg(num, msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s: socket.socket
    s.connect(('localhost',8001))
    s.send(f'{num}--{msg}'.encode())
    s.close()

threads = []
for i in range(100):
    msg =  random.choice(msgs)
    t =  threading.Thread(target=sendMsg,args=[i, msg])
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

