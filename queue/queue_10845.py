import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for i in range(n):
    inp = list(map(str, sys.stdin.readline().rstrip().split()))
    if inp[0] == "push":
        queue.append(int(inp[1]))
    elif inp[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif inp[0] == "size":
        print(len(queue))
    elif inp[0] == "empty":
        if not queue:
            print(1)

        else:
            print(0)
    elif inp[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif inp[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])