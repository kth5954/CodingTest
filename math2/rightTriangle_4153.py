dotList = []

while True:
  dot = list(map(int, input().split()))
  if max(dot) == 0:
    break
  dotList.append(dot)
  



for dot in dotList:
  dot = sorted(dot)
  if (dot[0])**2 + (dot[1])**2 == (dot[2])**2:
    print("right")
  else:
    print("wrong")


