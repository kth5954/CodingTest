import sys
from fractions import Fraction


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def joinAttack(i):
    try:
        return arr[i] + Fraction(1, joinAttack(i + 1))
    except IndexError:
        return arr[i]


print(joinAttack(0))