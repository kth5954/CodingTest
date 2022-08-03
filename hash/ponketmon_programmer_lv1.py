def solution(nums):
    hash = dict()
    for num in set(nums):
        hash[num] = []
    for num in nums:
        hash[num].append(num)

    arrLen = len(nums)
    hashLen = len(hash)
    # print("length of hash: ", len(hash))
    # print("length of arr: ", len(nums))
    if (arrLen // hashLen) >= 2:
        return hashLen
    else:
        return arrLen // 2