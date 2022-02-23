import sys
from collections import deque

d = deque()

n = int(sys.stdin.readline())
for i in range(n):
    order = list(map(str, sys.stdin.readline().rstrip().split()))
    if order[0] == "push_front":
        d.appendleft(int(order[1]))
    elif order[0] == "push_back":
        d.append(int(order[1]))
    elif order[0] == "pop_front":
        try:
            print(d.popleft())
        except IndexError:
            print(-1)
    elif order[0] == "pop_back":
        try:
            print(d.pop())
        except IndexError:
            print(-1)
    elif order[0] == "size":
        print(len(d))
    elif order[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        try:
            print(d[0])
        except IndexError:
            print(-1)
    elif order[0] == "back":
        try:
            print(d[-1])
        except IndexError:
            print(-1)