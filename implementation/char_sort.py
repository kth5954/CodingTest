import sys

inp = sys.stdin.readline()
num_list = [str(i) for i in range(10)]
alp_list = []
cnt = 0
for i in inp:
    if i in num_list:
        cnt += int(i)
    else:
        alp_list.append(i)


print(''.join(sorted(alp_list)).rstrip() + str(cnt))

