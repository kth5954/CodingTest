import sys

visited = [0] * 1000001
res = []
for i in range(2, int(1000001 ** 0.5)):
    if not visited[i]:
        for j in range(i * 2, 1000001, i):
            visited[j] = 1


while True:
    n = int(sys.stdin.readline())
    check = 0
    if not n:
        break
    left = 3
    right = n - 3
    for i in range(n):
        if not visited[left] and not visited[right]:
            print("%d = %d + %d" % (n, left, right))
            check = 1
            break
        else:
            left += 1
            right -= 1
    if not check:
        print("Goldbach's conjecture is wrong.")
