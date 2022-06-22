import sys

n = int(sys.stdin.readline())
time_table = []
for i in range(n):
    schedule = list(map(int, sys.stdin.readline().split()))
    time_table.append(schedule)

time_table.sort(key=lambda x: x[0])
time_table.sort(key=lambda x: x[1])


cnt = 1
end = time_table[0][1]
for i in range(1, n):
    if end <= time_table[i][0]:
        end = time_table[i][1]
        cnt += 1
print(cnt)