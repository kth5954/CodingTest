import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

dist = [0] * (F + 1)
visited = [0] * (F + 1)
def bfs():
    queue = deque([S])
    visited[S] = 1
    while queue:
        x = queue.popleft()
        if x == G:
            print(dist[G])
            return 0
        for r in [x + U, x - D]:
            if 0 < r <= F and not visited[r]:
                queue.append(r)
                dist[r] = dist[x] + 1
                visited[r] = 1
    if not dist[G]:
        print("use the stairs")


bfs()