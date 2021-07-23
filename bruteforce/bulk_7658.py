n = int(input())
k = []
rank = []
for i in range(n):
    k.append(list(map(int, input().split())))
    rank.append(1)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif k[i][0] < k[j][0] and k[i][1] < k[j][1]:
            rank[i] += 1


print(' '.join([str(x) for x in rank]))
