import sys
from itertools import permutations

x = sys.stdin.readline().rstrip()
array = list(permutations(x, len(x)))
num_list = []
for k in array:
    if int(''.join(k)) > int(x):
        num_list.append(int(''.join(k)))

if len(num_list):
    print(sorted(num_list)[0])
else:
    print(0)