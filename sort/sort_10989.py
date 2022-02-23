import sys

n = int(sys.stdin.readline())
k = [0] * 10001
for i in range(n):
    inp = int(sys.stdin.readline())
    k[inp] += 1

for i in range(len(k)):
    while k[i] != 0:
        print(i)
        k[i] -= 1
