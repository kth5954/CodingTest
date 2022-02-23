import sys

def day_order(m, d):
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    day_28 = [2]
    if m == 1:
        return d
    if m - 1 in day_31:
        return day_order(m - 1, 31) + d
    elif m - 1 in day_30:
        return day_order(m - 1, 30) + d
    else:
        return day_order(m - 1, 28) + d

def day_finder(m, d):
    weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return weeks[day_order(m, d) % 7]


x, y = map(int, sys.stdin.readline().split())
print(day_finder(x, y))
