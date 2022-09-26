N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
orders = []
for _ in range(M):
    d, s = map(int, input().split())
    orders.append([d-1, s])

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


def deepcopy(ref):
    copied = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            copied[i][j] = ref[i][j]

    return copied


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for m in range(M):
    d, s = orders[m]
    rained = [[False for _ in range(N)] for _ in range(N)]

    for i in range(len(clouds)):
        x, y = clouds[i]
        # print(x, y)
        x, y = x + s * dx[d], y + s * dy[d]
        x %= N
        y %= N
        # print(x, y)

        clouds[i] = [x, y]
        board[x][y] += 1
        rained[x][y] = True
        # print(board)

    new_board = deepcopy(board)

    for i in range(len(clouds)):
        x, y = clouds[i]
        cnt = 0
        for k in range(1, 8, 2):
            nx, ny = x + dx[k], y + dy[k]
            # print(nx, ny)
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] > 0:
                cnt += 1
        # print(x, y, cnt)
        new_board[x][y] += cnt
        # print(new_board)

    board = deepcopy(new_board)
    # print(board)

    clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not rained[i][j]:
                clouds.append([i, j])
                board[i][j] -= 2

    # print(board)
    # print(clouds)

answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]
print(answer)
