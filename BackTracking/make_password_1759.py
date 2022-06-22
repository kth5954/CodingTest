import sys

l, c = map(int, sys.stdin.readline().split())
inputValues = list(map(str, sys.stdin.readline().split()))
chars = sorted(inputValues)
vowel = ['a', 'e', 'i', 'o', 'u']
arr = []
def findPassword(password, con, vow):
    if con > l - 1 or vow > l - 2:
        return
    if len(password) == l:
        arr.append(password)
        return

    for char in chars:
        if char in password or password[-1] > char:
            continue
        if char in vowel:
            findPassword(password + char, con, vow + 1)
        else:
            findPassword(password + char, con + 1, vow)


for char in chars:
    if char in vowel:
        findPassword(char, 0, 1)
    else:
        findPassword(char, 1, 0)
for i in arr:
    print(i)

