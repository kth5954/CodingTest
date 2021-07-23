n = int(input())
k = 1

while True:
  a = 3*(k**2) - 3*k + 1
  if n <= a:
    print(k)
    break
  k += 1