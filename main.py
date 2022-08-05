import os


def main():
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))

    arr = ['32','123', '1234','214', '12', '21', '321', '32112']
    print(sorted(arr))
    return 0


def solution(phone_book):
    array = sorted(phone_book)
    for i in range(1, len(array)):
        if array[i-1] == array[i][:len(array[i-1])]:
            return False
    return True



if __name__ == "__main__":
    main()

