N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

board = [[[5] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    board[x-1][y-1].append([z])

# print(board)

# Spring + Summer

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

iter_cnt = 0
while iter_cnt < K:
    iter_cnt += 1
    for x in range(N):
        for y in range(N):
            # if tree exists
            if len(board[x][y]) > 1:
                death = False
                for t in range(len(board[x][y][1])-1, -1, -1):
                    if board[x][y][0] >= board[x][y][1][t]:
                        board[x][y][0] -= board[x][y][1][t]
                        board[x][y][1][t] += 1
                    else:
                        death = True
                        break
                if death:
                    # print(x, y, t, board[x][y][1][t+1:])
                    food = 0
                    for _t in range(t, -1, -1):
                        food += board[x][y][1][_t] // 2
                        M -= 1
                    board[x][y][1] = board[x][y][1][t+1:]
                    board[x][y][0] += food

    # print(iter_cnt, 'spring & summer')
    # print(board)

    for x in range(N):
        for y in range(N):
            # if tree exists
            if len(board[x][y]) > 1:
                # print(board[x][y][1])
                for t in board[x][y][1]:
                    if t % 5 == 0:
                        # print(x, y, t)
                        for i in range(8):
                            nx, ny = x + dx[i], y + dy[i]
                            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                continue
                            if len(board[nx][ny]) > 1:
                                board[nx][ny][1].append(1)
                            else:
                                board[nx][ny].append([1])
                            M += 1

    # print(iter_cnt, 'fall')
    # print(board)

    for x in range(N):
        for y in range(N):
            board[x][y][0] += A[x][y]

    # print(iter_cnt, 'winter')
    # print(board)

print(M)
