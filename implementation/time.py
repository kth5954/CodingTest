import sys

n = int(sys.stdin.readline())
time, minute, second = 0, 0, 0
cnt = 0
for t in range(n + 1):
    if '3' in str(t):
        cnt += 3600
        continue
    for m in range(60):
        if '3' in str(m):
            cnt += 60
            continue
        for s in range(60):
            if '3' in str(s):
                cnt += 1


print(cnt)