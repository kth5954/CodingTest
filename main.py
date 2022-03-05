import sys

t = int(sys.stdin.readline())
for _ in range(t):
    inp = list(sys.stdin.readline().rstrip())
    total = 0
    cnt = 0
    for i in range(len(inp)):
        if inp[i] == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)

