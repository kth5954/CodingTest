import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    inp = sys.stdin.readline().rstrip()
    stack = []
    for i in range(len(inp)):
        if stack and stack[-1] == inp[i]:
            stack.pop()
        else:
            stack.append(inp[i])
    if not stack:
        cnt += 1

print(cnt)