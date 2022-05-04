import sys

n, m = map(int, sys.stdin.readline().split())
d_list = []
for i in range(m):
    k = int(sys.stdin.readline())
    d_list.append(list(map(int, sys.stdin.readline().split())))

cur = 1
is_poped = False
while True:
    for d in d_list:
        try:
            if cur == d[-1]:
                x = d.pop()
                cur += 1
                is_poped = True
        except IndexError:
            continue
    if not is_poped:
        break
    is_poped = False

res = True
for d in d_list:
    if d:
        res = False

if res:
    print("Yes")
else:
    print("No")

