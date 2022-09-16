from collections import deque

N, M, x, y, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

move = list(map(int, input().split()))

dx = [0, 0, -1, +1]
dy = [+1, -1, 0, 0]

dice = [0 for _ in range(6)]

FLOOR = 1
BOTTOM = 3


for i in range(K):
    direction = move[i] - 1
    nx, ny = x + dx[direction], y + dy[direction]

    # if dice in board
    if nx >= 0 and nx < N and ny >= 0 and ny < M:
        x, y = nx, ny
        if direction == 0:
            dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
        elif direction == 1:
            dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
        elif direction == 2:
            dice[:4] = dice[1:4] + [dice[0]]
        elif direction == 3:
            dice[:4] = [dice[3]] + dice[:3]

        if board[x][y] == 0:
            board[x][y] = dice[BOTTOM]
        else:
            dice[BOTTOM] = board[x][y]
            board[x][y] = 0

        print(dice[FLOOR])


