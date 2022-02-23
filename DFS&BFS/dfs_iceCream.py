import sys

def dfs(g, x, y):
    n, m = len(g), len(g[0])
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if not g[x][y]:
        g[x][y] = 1
        dfs(g, x + 1, y)
        dfs(g, x - 1, y)
        dfs(g, x, y + 1)
        dfs(g, x, y - 1)
        return True
    return False


graph = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(graph, i, j):
            cnt += 1

print(cnt)
