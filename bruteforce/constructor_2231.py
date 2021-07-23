n = int(input())
m = 0
for i in range(n):
    a = list(map(int, str(i)))
    b = i + sum(a)
    if b == n:
        m = i
        break

print(m)