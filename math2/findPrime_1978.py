t = int(input())
numList = list(map(int,input().split()))
primeNumber = []

for num in numList:
  num_ = 0
  for i in range(1, num+1):
    if num % i == 0:
      num_ += 1
  if num_ == 2:
    primeNumber.append(num)

print(len(primeNumber))