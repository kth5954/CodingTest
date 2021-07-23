a, b, c = map(int, input().split())

while True:
  try:
    bep = int(a/(c-b)) + 1 #try문 밖에 쓰면 ZeroDivsionError 발생
    if bep > 0:
      print(bep)
    else:
      print(-1)
  except ZeroDivisionError:
    print(-1)
  break
