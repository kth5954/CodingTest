arr = []
for i in range(9):
    arr.append(int(input()))

test = [*arr]
cnt = 0
res = []
for i in range(9):
    for j in range(i + 1, 9):
        test = [*arr]
        test[i], test[j] = 0, 0
        if sum(test) == 100:
            res = test
            cnt += 1
            break
    if cnt:
        break

for i in sorted(res):
    if i:
        print(i)

