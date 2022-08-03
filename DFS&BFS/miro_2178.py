import sys
from collections import deque

def bfs(graph, x0, y0):
    queue = deque([[x0, y0]])
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(graph[x][y])
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y - dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 or graph[nx][ny] >= 2:
                continue
            graph[nx][ny] = graph[x][y] + 1
            queue.append([nx, ny])
    return False


n, m = map(int, sys.stdin.readline().split())
miro = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    miro.append(arr)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

bfs(miro, 0, 0)



