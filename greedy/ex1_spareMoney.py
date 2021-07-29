N = int(input())

coin = [500, 100, 50, 10]
cnt = 0

for i in range(4):
    cnt += N//coin[i]
    N %= coin[i]

print(cnt)