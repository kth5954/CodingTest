import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
stack = []
res = [0] * n

for i in range(n - 1, -1, -1):
    if len(stack) == 0:
        stack.append([i, towers[i]])
    else:
        while towers[i] > stack[len(stack) - 1][1]:
            t = stack.pop()
            if t[1] < towers[i]:
                res[t[0]] = i + 1
            if len(stack) == 0:
                break
        stack.append([i, towers[i]])

print(*res)


