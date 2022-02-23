from collections import deque
import sys

n = int(sys.stdin.readline())
p = []
for i in range(n):  # O(N)
    p.append(int(sys.stdin.readline()))
num_list = deque([i + 1 for i in range(n)])  # O(N)
a = deque([])
power = deque(p)

def isEmpty(stack):
    if not len(stack):
        return 1

def a_push():
    try:
        if isEmpty(a) or a[0] <= num_list[0]:
            a.appendleft(num_list.popleft())
        else:
            return 0

    except IndexError:
        return

def a_pop():
    try:
        return a.popleft()
    except IndexError:
        return


res = []
while num_list or a:
    # print("num: ", list(num_list))
    # print("a: ", list(a))
    # print("power:", list(power))
    if not a:
        a_push()
        res.append("+")
    if power[0] > a[0]:
        res.append("+")
        a_push()
    elif power[0] < a[0]:
        res.append("-")
        a_pop()
    else:
        res.append("-")
        power.popleft()
        a_pop()

try:
    if power[0]:
        print("NO")
except IndexError:
    for i in res:
        print(i)

