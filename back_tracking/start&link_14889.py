from itertools import combinations

# 입력
n = int(input())
arr = []  # (0,0) ~ (n,n)
for i in range(n):
    arr.append(list(map(int, input().split())))

# 리스트, 변수 만들기
start = []
link = []
start_point = 0
link_point = 0
score_difference = abs(start_point-link_point)
result = 10000

player = [i+1 for i in range(n)]  # 1 2 3 4
comb = list(combinations(player, n//2))

# 팀 빌딩
for c in comb:
    start = list(c)
    for k in range(n):
        if k+1 not in start:
            link.append(k+1)
# 시너지 비교
    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            if i+1 in start and j+1 in start:
                start_point += arr[i][j]
                start_point += arr[j][i]
            if i+1 in link and j+1 in link:
                link_point += arr[i][j]
                link_point += arr[j][i]
    if result > abs(start_point-link_point):
        result = abs(start_point-link_point)
    start_point = 0
    link_point = 0
    link = []  # link 초기화
print(result)