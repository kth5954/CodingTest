t = int(input())
hight = []
width = []
number = []

for i in range(t):
  h, w, n = map(int, input().split())

  hight.append(h)
  width.append(w)
  number.append(n)

for i in range(t):
  if number[i] % hight[i] == 0:
    room_number = number[i] // hight[i]
    room_hight = hight[i]
    
  else:
    room_number = number[i] // hight[i] + 1
    room_hight = number[i] % hight[i]

  if room_number >= 10:
    print("%d%d"%(room_hight, room_number))
  else:
    print("%d0%d"%(room_hight, room_number))