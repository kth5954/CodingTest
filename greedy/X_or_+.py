S = input()
S = list(map(int, S))
result = 0

for i in range(len(S)):
    if S[i] <= 1 or result <= 1:
        result += S[i]
    else:
        result *= S[i]

print(result)