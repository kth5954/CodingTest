import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def findDot(a1, a2, a3):
  if a1 == a2:
    a4 = a3
  elif a2 == a3:
    a4 = a1
  else:
    a4 = a2
  return a4

print(findDot(x1, x2, x3),findDot(y1, y2, y3))