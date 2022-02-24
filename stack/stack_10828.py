import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    inp = list(map(str, sys.stdin.readline().rstrip().split()))
    if inp[0] == "push":
        stack.append(inp[1])
    elif inp[0] == "pop":
        if not stack:
            print(-1)
            continue
        print(stack.pop())
    elif inp[0] == "size":
        print(len(stack))
    elif inp[0] == "empty":
        if not stack:
            print(1)
            continue
        print(0)
    elif inp[0] == "top":
        if not stack:
            print(-1)
            continue
        print(stack[-1])

