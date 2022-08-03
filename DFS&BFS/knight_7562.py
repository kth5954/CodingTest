import sys
from collections import deque

def bfs(graph, x, y, X, Y, l):
    visited[x][y] = 0
    queue = deque([[x, y]])
    while queue:
        a, b = queue.popleft()
        if a == X and b == Y:
            print(visited[a][b])
            return True
        for i in range(len(graph)):
            nx, ny = a + graph[i][0], b + graph[i][1]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = visited[a][b] + 1
                queue.append([nx, ny])
    return False


n = int(sys.stdin.readline())
for _ in range(n):
    l = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().split())
    X, Y = map(int, sys.stdin.readline().split())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    route = [[2, 1], [2, -1], [-2, 1], [-2, -1],
             [1, 2], [1, -2], [-1, 2], [-1, -2]]
    bfs(route, x, y, X, Y, l)




