n, m = map(int, input().split())
cards = list(map(int, input().split()))

sum_list = []


for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            if i <= j or j <= k:
                continue
            else:
                sum_list.append(cards[i]+cards[j]+cards[k])


blackjack = sorted([i for i in sum_list if i <= m])

print(blackjack[len(blackjack)-1])