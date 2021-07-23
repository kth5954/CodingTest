t = int(input())
k = []
n = []
for i in range(t):
  k_ = int(input())
  n_ = int(input())
  k.append(k_)
  n.append(n_)
  
for i in range(t):
  array = [[0 for col in range(n[i]+1)] for row in range(k[i]+1)]
  for col in range(n[i]+1):
    array[0][col] = col+1
  for row in range(k[i]+1):
    array[row][0] = 1
  for row in range(1, k[i]+1):
    for col in range(1, n[i]+1):
      array[row][col] = array[row-1][col] + array[row][col-1]

  print(array[k[i]][n[i]-1])