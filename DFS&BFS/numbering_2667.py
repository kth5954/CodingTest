# 시간나면 BFS로도 풀어보기

import sys

n = int(sys.stdin.readline())
g = []

for i in range(n):
    g.append(list(map(int, sys.stdin.readline().rstrip())))

num = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def sol(graph, x, y):
    if x >= n or y >= n or x < 0 or y < 0:
        return False
    if graph[x][y] == 1:
        global inner_cnt
        inner_cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            sol(graph, nx, ny)
        return True


cnt = 0
inner_cnt = 0
for i in range(n):
    for j in range(n):
        if sol(g, i, j):
            num.append(inner_cnt)
            cnt += 1
            inner_cnt = 0

print(cnt)
for n in sorted(num):
    print(n)
