import sys

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if graph[x][y]:
        graph[x][y] = 0
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for i in range(m)]
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    print(cnt)