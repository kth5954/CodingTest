import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
coc = list(itertools.combinations(cards, 3))  # coc = combinations of cards
result = 0  # 결과값 초기화

for i in range(1, len(coc)):
    sum_of_cards = sum(coc[i])  # 카드 세 장의 합
    if sum_of_cards > m:  # 합이  m보다 클 경우 무시
        continue
    elif sum_of_cards > result:  # 카드 합이 result 보다 클 경우 result에 카드 합 넣어주기
        result = sum_of_cards

print(result)