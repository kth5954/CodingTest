# 1920 find_num
import sys

def binary_search(arr, x, start, end):
    while start <= end:
        mid = (end + start) // 2
        if x == arr[mid]:
            return True
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

for num in check_list:
    if binary_search(A, num, 0, n - 1):
        print(1)
    else:
        print(0)
