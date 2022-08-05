def solution(phone_book):
    array = sorted(phone_book)
    for i in range(1, len(array)):
        if array[i-1] == array[i][:len(array[i-1])]:
            return False
    return True
