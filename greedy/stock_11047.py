import sys

t = int(sys.stdin.readline())
for _ in range(t):
    days = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    stocks = 0
    total = 0
    benefit = 0
    for i in range(days):
        buy = False
        for j in range(i + 1, days):
            if prices[j] >= prices[i]:
                buy = True
                break
        if buy:
            stocks += 1
            total += prices[i]
            continue
        benefit += prices[i] * stocks - total
        total, stocks = 0, 0
    print(benefit)



