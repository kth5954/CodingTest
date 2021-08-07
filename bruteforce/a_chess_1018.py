import sys

#입력
M, N = map(int, input().split())
inp = []
for i in range(M):
    inp.append(sys.stdin.readline())

# 체스판 자르기
def cut_board(first_board):
    length = len(first_board)
    width = len(first_board[0])
    board_list = []

    for w in range(width - 7):
        for l in range(length - 7):
            board = []
            for i in range(8):
                board.append(list(first_board[l+i][w:w+8]))
            board_list.append(board)
    return board_list

# 바뀐 횟수 체크
def cnt_change(board):
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'W':
                    cnt1 += 1
            else:
                if board[i][j] != 'B':
                    cnt1 += 1
            if (i + j) % 2 == 0:
                if board[i][j] != 'B':
                    cnt2 += 1
            else:
                if board[i][j] != 'W':
                    cnt2 += 1
    return min(cnt1, cnt2)


# 결과 출력
board_list = cut_board(inp)
min_cnt = 12345678765
for board in board_list:
    min_cnt = min(cnt_change(board), min_cnt)

print(min_cnt)

