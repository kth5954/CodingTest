m = int(input())
n = int(input())
primeNumber = []

for num in range(m, n+1):
  if num == 1:
    continue
  num_count = 0
  for i in range(2, num):
    if num % i == 0:
      num_count += 1
    if num_count > 0:
      break
  if num_count == 0:
    primeNumber.append(num)

count = 0
for i in primeNumber:
  count = count + i

if len(primeNumber) > 0:
  print(count)
  print(min(primeNumber))
else:
  print(-1)

