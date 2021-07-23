t = int(input())
testCase = []
for i in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  testCase.append([x1, y1, r1, x2, y2, r2])



def turret(x1,y1,r1,x2,y2,r2):
  l = ((x1-x2)**2 + (y1-y2)**2)**0.5 

  if (x1, y1) == (x2, y2):
    if r1 == r2:
      print(-1)
    else:
      print(0)

  else:
    if r1 + r2 < l:
      print(0)

    elif r1 + r2 == l or min(r1, r2) + l == max(r1, r2):
      print(1)

    elif r1 + r2 > l:
      print(2)

for l in testCase:
  turret(l[0], l[1], l[2], l[3], l[4], l[5])