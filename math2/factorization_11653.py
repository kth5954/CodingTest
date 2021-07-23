n = int(input())

def measure(k):
  measureList = [] 
  
  for i in range(1, k+1):
    if k % i == 0:
      measureList.append(i)
  return measureList

def primeNumber_filter(k):
  a_list = measure(k)
  primeNumberList = []
  for i in a_list:
    if i == 1:
      continue
    count = 0
    for j in range(2,i):
      if i % 2 == 0:
        count += 1
    if count == 0:
      primeNumberList.append(i)
  return primeNumberList

def factorization(k):
  while k > 1:
    for i in primeNumber_filter(k):
      while k % i == 0:
        k /= i
        print(i)

factorization(n)