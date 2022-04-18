import sys

T = int(sys.stdin.readline())
for i in range(T):
    inp = list(map(str, sys.stdin.readline().rstrip().split()))
    for w in inp:
        print(w[::-1], end=" ")
    print("")
