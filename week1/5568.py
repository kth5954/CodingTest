import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = []
for i in range(n):
    cards.append(int(sys.stdin.readline()))

nums = list(permutations(cards, k))

res = []
for n in nums:
    s = ''
    for i in list(n):
        s += str(i)
    res.append(s)

print(len(set(res)))
