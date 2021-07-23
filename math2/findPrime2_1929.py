m, n = map(int, input().split())

prime = []
for num in range(m, n+1):
  count = 0
  for i in range(2, int(num**0.5)+1):
    
    if num % i == 0:
      count += 1
      break
  if count == 0 and num != 1:
    prime.append(num)
  
for i in prime:
  print(i)