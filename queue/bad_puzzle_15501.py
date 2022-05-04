import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a = deque(a)
ra = deque(reversed(a))
b = deque(list(map(int, sys.stdin.readline().split())))


def sortedDeq(deq):
    while True:
        x = deq.popleft()
        deq.append(x)
        if x == 1:
            return deq


if sortedDeq(a) == sortedDeq(b) or sortedDeq(ra) == sortedDeq(b):
    print("good puzzle")
else:
    print("bad puzzle")