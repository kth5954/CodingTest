from bisect import bisect_left, bisect_right

a = [1, 2, 3, 4, 4, 6, 7, 8]
x = 4
bl = bisect_left(a, x)  # 정렬을 유지하며 x를 삽입할 가장 왼쪽의 인덱스를 반환
br = bisect_right(a, x)  # 정렬을 유지하며 x를 삽입할 가장 오른쪽의 인덱스를 반환

# 값이 특정 범위에 속하는 데이터 개수 구하기
def counter(arr, left_value, right_value):
    arr = sorted(arr)
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)


print(counter(a, 3, 5))