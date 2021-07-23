"""" Bertrand's postulate"""


testCase = []

while 1:
  inp = int(input())
  if inp == 0:
    break
  testCase.append(inp)

def lenOfPrimes(a,b):
  len_of_primes = 0
  
  for num in range(a, b+1):
    cnt = 0
    for i in range(2, int(num**0.5)+1):
      if num % i == 0:
        cnt += 1
      if cnt > 0:
        break
    if cnt == 0 and num != 1:
      len_of_primes += 1
  print(len_of_primes)

for i in testCase:
  lenOfPrimes(i, i*2)
