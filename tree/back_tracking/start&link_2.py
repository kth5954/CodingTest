from itertools import combinations

# 입력
n = int(input())
arr = []  # (0,0) ~ (n,n)
for i in range(n):
    arr.append(list(map(int, input().split())))

# 리스트, 변수 만들기
start_point = 0
link_point = 0
player = [i+1 for i in range(n)]  # 1 2 3 4
comb = list(combinations(player, n//2))
result = 1000

# 팀 빌딩
for c in comb:
    start = list(c)
    link = list(set(player).difference(start))
    start_synergy = list(combinations(start, 2))
    link_synergy = list(combinations(link, 2))
    for (i, j) in start_synergy:
        if i in start and j in start:
            start_point += arr[i-1][j-1]
            start_point += arr[j-1][i-1]
    for (i, j) in link_synergy:
        if i in link and j in link:
            link_point += arr[i-1][j-1]
            link_point += arr[j-1][i-1]
    if abs(start_point - link_point) < result:
        result = abs(start_point - link_point)
    start_point = 0
    link_point = 0
print(result)