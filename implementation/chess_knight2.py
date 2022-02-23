import sys


inp = sys.stdin.readline()
col = int(ord(inp[0])) - int(ord('a')) + 1
row = int(inp[1])
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2),
         (2, 1), (-2, 1), (2, -1), (-2, -1)]
cnt = 0

for step in steps:
    next_col = col + step[0]
    next_row = row + step[1]
    if 1 <= next_col <= 8 and 1 <= next_row <= 8:
        cnt += 1

print(cnt)