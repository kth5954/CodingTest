import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = list(map(int, sys.stdin.readline().split()))
g = [[] for i in range(N + 1)]  # 0 1 2 3 4
for i in range(M):
    inp = list(map(int, sys.stdin.readline().split()))
    g[inp[0]].append(inp[1])
    g[inp[1]].append(inp[0])

rg = []
for k in g:
    rg.append(sorted(k))
g = rg

visited_arr_dfs = [False] * (N + 1)
visited_arr_bfs = [False] * (N + 1)

dfs(g, V, visited_arr_dfs)
print("")
bfs(g, V, visited_arr_bfs)




