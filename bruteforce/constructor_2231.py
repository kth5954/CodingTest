n = int(input())
result = 0
for i in range(n):
    dcp = i + sum(int(j) for j in str(i))  # dcp = decomposition(분해합)
    if dcp == n:  # 분해합이 n일 경우 결과값에 i값 할당, 반복문 종료
        result = i
        break
print(result)