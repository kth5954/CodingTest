import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[[0] * 2 for i in range(m)] for j in range(n)]

def bfs(start_x, start_y, start_is_crashed):
    queue = deque([(start_x, start_y, start_is_crashed)])
    visited[start_x][start_y][start_is_crashed] = 1
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y, is_crashed = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][is_crashed]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not miro[nx][ny] and not visited[nx][ny][is_crashed]:
                visited[nx][ny][is_crashed] = visited[x][y][is_crashed] + 1
                queue.append((nx, ny, is_crashed))
            if miro[nx][ny] == 1 and not is_crashed:
                queue.append((nx, ny, is_crashed + 1))
                visited[nx][ny][is_crashed + 1] = visited[x][y][is_crashed] + 1
    return -1


print(bfs(0, 0, 0))



