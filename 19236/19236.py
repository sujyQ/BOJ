fish = [[-1, -1, -1] for _ in range(16)]
board = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        fish[line[j*2]-1] = [i, j, line[j*2+1]-1]
        board[i][j] = line[j*2]-1

# print(fish)
# print(board)

answer = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
eat = [False for _ in range(16)]

shark = [0, 0, fish[board[0][0]][-1]]
target = board[0][0]
eat[target] = True
board[0][0] = 16


def deepcopy(ref):
    # print(len(ref), len(ref[0]))
    copied = [[0 for _ in range(len(ref[0]))] for _ in range(len(ref))]
    for i in range(len(ref)):
        for j in range(len(ref[0])):
            # print(i, j)
            copied[i][j] = ref[i][j]
    return copied


def dfs(score, board, fish, shark):
    global answer
    # print(score)
    # print(board)
    # if shark[0] == -1 and shark[1] == -1 and board[0][0] == -1:
    answer = max(score, answer)
    # print('answer', answer)
        # return

    # if shark[0] == -1 and shark[1] == -1 and board[0][0] != -1 and board[0][0] != 16:
    #     target = board[0][0]
    #     shark = [0, 0, fish[target][-1]]
    #     score += target+1
    #     board[0][0] = 16
    #     eat[target] = True
    # print(shark)
    # print(board)

    for i in range(16):
        if eat[i]:
            continue

        x, y, d = fish[i]
        # print(x, y, d)

        cnt = 0
        while True:
            if cnt == 8:
                break
            # print(d)
            nx, ny = x + dx[d], y + dy[d]
            # print(nx, ny, d)
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or board[nx][ny] == 16:
                d = (d+1) % 8
            elif board[nx][ny] == -1:
                board[nx][ny] = i
                board[x][y] = -1
                fish[i] = [nx, ny, d]
                break
            else:
                target = board[nx][ny]
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                fish[i] = [nx, ny, d]
                fish[target][:2] = [x, y]
                break
            cnt += 1
        # print(i, board)
        # print(i, fish)
    # print(board)
    # print(fish)

    x, y, d = shark
    _board = deepcopy(board)
    _fish = deepcopy(fish)
    # print(x, y, d)
    for i in range(1, 4):
        nx, ny = x + i * dx[d], y + i * dy[d]
        # print(board)
        # print(shark)
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if board[nx][ny] != -1:
            # print(board)
            target = board[nx][ny]
            board[nx][ny] = 16
            board[x][y] = -1
            eat[target] = True
            # print(x, y, d)
            # print(shark)
            # print(board)
            # print(score, target, nx, ny)
            shark = [nx, ny, fish[target][-1]]
            dfs(score + target + 1, board, fish, shark)
            eat[target] = False
            board = deepcopy(_board)
            shark = [x, y, d]
            fish = deepcopy(_fish)

    # if not moved:
    #     board[shark[0]][shark[1]] = -1
    #     shark = [-1, -1, -1]
    #     dfs(score, board, shark)


dfs(target+1, board, fish, shark)
print(answer)

