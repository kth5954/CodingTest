import sys
test = []
n = int(input())
for i in range(n):
    num = int(sys.stdin.readline())
    test.append(num)

for i in sorted(test):
    print(i)
