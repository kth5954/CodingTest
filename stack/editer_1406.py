import sys
from collections import deque

arr = list(sys.stdin.readline().rstrip())
cur = len(arr)
left = deque(arr[:cur])
right = deque(arr[cur:])

n = int(sys.stdin.readline())
for i in range(n):
    inp = list(sys.stdin.readline().rstrip().split())
    if inp[0] == 'L' and cur != 0:
        cur -= 1
        right.appendleft(left.pop())
    elif inp[0] == 'D' and cur != len(left) + len(right):
        cur += 1
        left.append(right.popleft())
    elif inp[0] == 'P':
        left.append(inp[1])
        cur += 1
    elif inp[0] == 'B' and cur != 0:
        left.pop()
        cur -= 1

print("".join(list(left + right)))