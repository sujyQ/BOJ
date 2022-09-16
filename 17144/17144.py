R, C, T = map(int, input().split())
board = []
for i in range(R):
    board.append(list(map(int, input().split())))
    if board[i][0] == -1:
        DOWN = i
        UP = i-1


def deepcopy(ref):
    copied = []
    for i in range(R):
        copied.append([])
        for j in range(C):
            copied[i].append(ref[i][j])

    return copied


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    if T == 0:
        answer = 0
        for x in range(R):
            for y in range(C):
                if board[x][y] != -1:
                    answer += board[x][y]
        break

    n_board = deepcopy(board)
    for x in range(R):
        for y in range(C):
            if board[x][y] > 0:
                spread_cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        continue
                    if board[nx][ny] == -1:
                        continue
                    n_board[nx][ny] += board[x][y] // 5
                    spread_cnt += 1
                n_board[x][y] -= (board[x][y] // 5) * spread_cnt

    board = deepcopy(n_board)
    n_board[UP][1:] = [0] + board[UP][1:C-1]
    for i in range(0, UP):
        n_board[i][-1] = board[i+1][-1]
    n_board[0][0:C-1] = board[0][1:]
    for i in range(1, UP):
        n_board[i][0] = board[i-1][0]


    n_board[DOWN][1:] = [0] + board[DOWN][1:C-1]
    for i in range(DOWN+1, R):
        n_board[i][-1] = board[i-1][-1]
    n_board[R-1][0:C-1] = board[R-1][1:]
    for i in range(DOWN+1, R-1):
        n_board[i][0] = board[i+1][0]

    board = deepcopy(n_board)

    T -= 1

print(answer)
