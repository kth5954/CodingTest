t = int(input())
X = []; Y = []
for i in range(t): 
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

for i in range(t):
  K = (Y[i] - X[i])**0.5
  if K == int(K):
    print(2*int(K) - 1)
  elif K - int(K) <= 0.5:
    print(2*int(K))
  else:
    print(2*int(K+1)-1)