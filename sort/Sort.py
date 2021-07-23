import heapq
def bubbleSort(arr):  # O(N^2),  stable
  for j in range(len(arr)):
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def selectionSort(arr):  # O(N^2), unstable
    for i in range(len(arr-1)):
        min_idx = j
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def quickSort(arr):  # O(NlogN) ~ O(n^2), unstable
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []

    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return quickSort(left) + [pivot] + quickSort(right)

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


def heapq_sort(arr):   # O(NlogN), unstable
    heapq.heapify(arr)
    for i in range(len(arr)):
        val = heapq.heappop(arr)
        print(val)

def countingSort(arr, K):  # O(N), stable
    c = [0] * K
    result = [0] * len(arr)

    for i in arr:
        c[i] += 1

    for i in range(1, K):
        c[i] += c[i - 1]

    for i in range(len(arr)):
        result[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1
    return result

