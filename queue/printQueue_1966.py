import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())  # n: 문서의 개수, m: 차례 확인할 수의 index
    doc = deque(list(map(int, sys.stdin.readline().split())))  # 문서 리스트
    cur = 0  # 현재 검사할 맨 앞의 인덱스 번호
    cnt = 0
    out_idx = []
    n = len(doc)
    while doc:
        # print(doc)
        if cur == n:
            cur = 0
        if cur in out_idx:
            cur += 1
            continue
        # print("현재 인덱스: %d, 현재 검사 값: %d" % (cur, doc[0]))
        if doc[0] == max(doc):
            if m == cur:
                cnt += 1
                # print("마지막 출력순서: %d" % cnt)
                print(cnt)
                break
            else:
                cnt += 1
                out_idx.append(cur)
                doc.popleft()
                # print("출력합니다!! \n 출력순서: %d, 출력값: %d, 출력 인덱스: %d" % (cnt, doc.popleft(), cur))
                cur += 1
                continue
        cur += 1
        doc.append(doc.popleft())














