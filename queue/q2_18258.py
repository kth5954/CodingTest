import sys
from collections import deque

n = int(sys.stdin.readline())
orders = []
queue = deque()
for i in range(n):
    orders.append(list(map(str, sys.stdin.readline().rstrip().split())))

for order in orders:
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        try:
            print(queue.popleft())
        except IndexError:
            print(-1)
    elif order[0] == "front":
        try:
            print(queue[0])
        except IndexError:
            print(-1)
    elif order[0] == "back":
        try:
            print(queue[-1])
        except IndexError:
            print(-1)
    elif order[0] == "empty":
        try:
            if queue[0]:
                print(0)
        except IndexError:
            print(1)
    elif order[0] == "size":
        print(len(queue))

