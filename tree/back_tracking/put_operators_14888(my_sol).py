from itertools import *

n = int(input())
inp1 = list(map(int, input().split()))
inp2 = list(map(int, input().split()))

# 계산기(수열, 연산자) => 결과값 출력
def acc(arr, operators):
    value = arr[0]
    for i in range(1, n):
        if operators[i-1] == '+':
            value += arr[i]
        elif operators[i-1] == '-':
            value -= arr[i]
        elif operators[i-1] == '*':
            value *= arr[i]
        else:
            if value >= 0:
                value //= arr[i]
            else:
                value = -(abs(value)//arr[i])
    return value

def findMax(arr, operators):
    result = -1000000001
    for k in range(len(key)):
        if acc(inp1, key[k]) > result:
            result = acc(inp1, key[k])
    return result

def findMin(arr, operators):
    result = 1000000001
    for k in range(len(key)):
        if acc(inp1, key[k]) < result:
            result = acc(inp1, key[k])
    return result


#  연산자 타입, 배열 생성
operator_types = ['+', '-', '*', '//']
dummy = []

for j in range(4):
    for i in range(inp2[j]):
        dummy.append(operator_types[j])
key = list(permutations(dummy, n - 1))


print(findMax(inp1, key))
print(findMin(inp1, key))
