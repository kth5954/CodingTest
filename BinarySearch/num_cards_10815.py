import sys

n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
res = []

def binary_search(arr, target, start, end):
    mid = (start + end) // 2
    while start <= end:
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


for i in range(m):
    if binary_search(cards, check[i], 0, n - 1):
        print(1, end=" ")
    else:
        print(0, end=" ")
