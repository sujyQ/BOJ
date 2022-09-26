N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    cnt = 0
    rainbow = 0
    block = [[x, y]]
    i, j = N, N
    c = board[x][y]
    visited[x][y] = True

    queue = [[x, y]]

    while queue:
        x, y = queue.pop(0)
        cnt += 1
        # print(x, y)
        # if board[x][y] == 0:
        #     rainbow += 1

        if board[x][y] != 0 and i > x:
            i, j = x, y
        elif board[x][y] != 0 and i == x and j > y:
            i, j = x, y

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] <= -1:
                continue

            if board[nx][ny] == 0 and [nx, ny] not in block:
                block.append([nx, ny])
                queue.append([nx, ny])
                visited[nx][ny] = True
                rainbow += 1
            elif not visited[nx][ny] and board[nx][ny] == c:
                queue.append([nx, ny])
                block.append([nx, ny])
                visited[nx][ny] = True

    # print(block)

    return cnt, rainbow, i, j, block


def gravity():
    for i in range(N):
        for j in range(N-1, -1, -1):
            stop = N-1
            # print(j, i, board[j][i])
            if board[j][i] < 0:
                continue
            for k in range(j, N-1):
                # print(k)
                if board[k+1][i] > -2:
                    stop = k
                    break
            board[j][i], board[stop][i] = -2, board[j][i]


def deepcopy(ref):
    copied = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            copied[i][j] = ref[i][j]
    return copied


score = 0
while True:
    group_cnt = 0
    targets = []
    max_cnt = 0
    max_r = 0
    pos = [N, N]
    visited = [[False for _ in range(N)] for _ in range(N)]
    # print(score)
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                cnt, r, x, y, block = bfs(i, j)
                # print(i, j, cnt, block)
                if cnt >= 2:
                    group_cnt += 1
                    if max_cnt < cnt:
                        max_cnt = cnt
                        max_r = r
                        pos = [x, y]
                        targets = block
                    elif max_cnt == cnt and max_r < r:
                        max_r = r
                        pos = [x, y]
                        targets = block
                    elif max_cnt == cnt and max_r == r and pos[0] < x:
                        pos = [x, y]
                        targets = block
                    elif max_cnt == cnt and max_r == r and pos[0] == x and pos[1] < y:
                        pos = [x, y]
                        targets = block
    # print(targets)

    if group_cnt == 0:
        break

    for t1, t2 in targets:
        board[t1][t2] = -2
    score += max_cnt ** 2

    # print(board)

    gravity()
    # print(board)

    new_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N-1-j][i] = board[i][j]

    board = deepcopy(new_board)
    # print(board)

    gravity()
    # print(board)

print(score)

# N = 4
# board = [[1, 2, 3, 4], [-2, -2, 0, 0], [0, 0, 0, 0], [-1, -1, -1, -1], [0, 0, 0, 0], ]
# gravity()
# print(board)



