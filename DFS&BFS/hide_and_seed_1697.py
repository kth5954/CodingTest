# bfs: 숨바꼭질
# 왜 bfs인가?
# bfs는 너비 우선 탐색인데, 일단 큐 자료형을 이용해서 하나씩 넣어보면서 해당 깊이로 갈 수 있는 너비 안에 있는 모든 경우의 수를 탐색
# 원하는 값이 나왔을 때 깊이를 구하는 것임

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)

def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            return 0
        nx_list = [x + 1, x - 1, x * 2]
        for nx in nx_list:
            if 0 <= nx <= MAX and not dist[nx]:
                queue.append(nx)
                dist[nx] = dist[x] + 1


bfs()