import os
import requests
import threading
import snoop
import random
import string


# with open('a') as f1:
#     with open('b') as f2:
#         pass

session = requests.session()
# with open('a.txt') as a, open('b.txt') as b:
#     for line in a.

def rfile(path):
    with open(path) as a:
        return a.readlines()


# @snoop
def worker(inp):
    print(f'this is worker {inp}')

import queue

def queue_demo():

    q1 = queue.Queue(100)
    for i in range(10):
        q1.put(random.choice(string.ascii_letters))
    
    print(q1.qsize())

# import heapq
# def heap_demo():
#     h1 = heapq.


def main():
    tasks = [threading.Thread(target=worker, args=(num, )) for num in range(5) ]
    for ta in tasks:
        ta.start()
    for ta in tasks:
        ta.join()




queue_demo()