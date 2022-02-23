import sys

n = int(sys.stdin.readline())
p = list(map(int ,sys.stdin.readline().split()))
stack = []
ans = [-1] * n

for i in range(n):
    while stack and p[stack[-1]] < p[i]:
        ans[stack.pop()] = p[i]
    stack.append(i)

print(*ans)