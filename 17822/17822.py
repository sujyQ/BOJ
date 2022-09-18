N, M, T = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
spin = []
for _ in range(T):
    spin.append(list(map(int, input().split())))
DEL = 9999

for t in range(T):
    x, d, k = spin[t]
    circle = x-1
    while circle < N:
        if d == 0:
            board[circle] = board[circle][M-k:] + board[circle][:M-k]
        elif d == 1:
            board[circle] = board[circle][k:] + board[circle][:k]

        circle += x
    # print(t, board)

    target = []
    for i in range(N):
        if board[i][M-1] != DEL and board[i][M-1] == board[i][M-2]:
            target += [[i, M-1], [i, M-2]]
        if board[i][M-1] != DEL and board[i][M-1] == board[i][0]:
            target += [[i, M - 1], [i, 0]]
        if board[i][0] != DEL and board[i][0] == board[i][1]:
            target += [[i, 0], [i, 1]]
        if board[i][0] != DEL and board[i][0] == board[i][M-1]:
            target += [[i, 0], [i, M-1]]

    for i in range(0, N):
        for j in range(0, M):
            if board[i][j] == DEL:
                continue
            if j > 0 and board[i][j] == board[i][j-1]:
                target += [[i, j], [i, j-1]]
                # print('-1', [[i, j], [i, j-1]])
            if j < M-1 and board[i][j] == board[i][j+1]:
                target += [[i, j], [i, j+1]]
                # print('-2', [[i, j], [i, j + 1]])
            if i > 0 and board[i][j] == board[i-1][j]:
                target += [[i, j], [i-1, j]]
            if i < N-1 and board[i][j] == board[i+1][j]:
                target += [[i, j], [i+1, j]]

    for j in range(M):
        if board[0][j] != DEL and board[0][j] == board[1][j]:
            target += [[0, j], [1, j]]
        if board[N-1][j] != DEL and board[N-1][j] == board[N-2][j]:
            target += [[N-1, j], [N-2, j]]

    # print(t, target)
    if len(target) == 0:
        cnt = 0
        summation = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != DEL:
                    cnt += 1
                    summation += board[i][j]

        if cnt > 0:
            avg = summation / cnt
            # print(t, summation, cnt, avg)
            for i in range(N):
                for j in range(M):
                    if board[i][j] == DEL:
                        continue
                    if board[i][j] < avg:
                        board[i][j] += 1
                    elif board[i][j] > avg:
                        board[i][j] -= 1
        else:
            break
    else:
        for _t in target:
            board[_t[0]][_t[1]] = DEL

    # print(t, board)

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != DEL:
            answer += board[i][j]
print(answer)
