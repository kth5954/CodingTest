import sys

n = int(sys.stdin.readline())
orders = []
for i in range(n):
    inp = list(map(str, sys.stdin.readline().split()))
    orders.append(inp)

print(orders)
