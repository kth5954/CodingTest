import sys

T = int(sys.stdin.readline())
ps_list = []
output_list = []
for i in range(T):
    ps_list.append(sys.stdin.readline().strip())


for ps in ps_list:
    i = 0
    while i < 50:
        ps = ps.replace("()", "")
        i += 1
    if ps == '':
        output_list.append("YES")
        continue
    else:
        output_list.append("NO")
for output in output_list:
    print(output)