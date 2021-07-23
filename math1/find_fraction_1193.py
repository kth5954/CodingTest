x = int(input())
k = 1
while True: 
  a = ((k**2) + k)/2
  if x <= a:
    if k % 2 == 1:
      print("%d/%d"%(a-x+1, k-(a-x)))
    else:
      print("%d/%d"%(k-(a-x), a-x+1))
    break
  k += 1
