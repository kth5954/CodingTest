import sys


inp_list = []
brackets = ['(', ')', '[', ']']
br_list = []
output_list = []

while True:
    inp = sys.stdin.readline().rstrip()
    if inp == '.':
        break
    inp_list.append(inp)
for inp in inp_list:
    br = []
    for i in inp:
        for b in brackets:
            if i == b:
                br.append(i)
    br = ''.join(br)
    br_list.append(br)


for br in br_list:
    i = 0
    while i < 100:
        br = br.replace("()", "")
        br = br.replace("[]", "")
        i += 1
    if br == '':
        output_list.append("yes")
        continue
    else:
        output_list.append("no")
for output in output_list:
    print(output)