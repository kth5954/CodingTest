import sys

def mergeSort(arr):  # (NlogN), stable
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    merged_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr


n = int(input())
members = []
for i in range(n):
    member = list(map(str, sys.stdin.readline().split()))
    members.append(member)


sorted_members = sorted(members)
for name, age in sorted_members:
    print(name + " " + age)
