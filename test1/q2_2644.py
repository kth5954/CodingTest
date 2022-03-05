import sys
from collections import deque

# input, graph
n = int(sys.stdin.readline())  # 가족 수
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
for i in range(m):
    c, d = map(int, sys.stdin.readline().split())
    graph[c].append(d)
    graph[d].append(c)

visited_b = [0] * (n + 1)
def bfs(start, visited):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for num in graph[x]:
            if visited[num] == 0:
                visited[num] = visited[x] + 1
                queue.append(num)


visited_d = [0] * (n + 1)
def dfs(v, visited):
    for num in graph[v]:
        if visited[num] == 0:
            visited[num] = visited[v] + 1
            dfs(num, visited)


bfs(a, visited_b)
dfs(a, visited_d)
if visited_b[b] > 0:
    print(visited_b[b])
else:
    print(-1)

if visited_d[b] > 0:
    print(visited_d[b])
else:
    print(-1)