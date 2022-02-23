import sys

col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]

inp = sys.stdin.readline()

col_start = inp[0]
row_start = int(inp[1])
cnt = 8

for i in range(len(col)):
    if col_start == col[i]:
        col_start = i + 1

if col_start == 1 or col_start == 8:
    cnt -= 4
    if row_start == 1 or row_start == 8:
        cnt -= 2
    elif row_start == 2 or row_start == 7:
        cnt -= 1
elif col_start == 2 or col_start == 7:
    cnt -= 2
    if row_start == 1 or row_start == 8:
        cnt -= 3
    elif row_start == 2 or row_start == 7:
        cnt -= 1

print(cnt)







