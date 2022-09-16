N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

rots = [0, 4, 2, 4, 4, 1]
cameras = []
D = 0
for i in range(N):
    for j in range(M):
        c = board[i][j]
        if c != 0 and c != 6:
            cameras.append([i, j, rots[c], -1])
            D += 1

# print(cameras)
# print(D)
# print('-----')


def deepcopy(ref):
    copied = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copied[i][j] = ref[i][j]

    return copied


def watch(board, x, y, direction):
    if direction == 0:
        for j in range(y+1, M):
            if board[x][j] == 6:
                break
            if board[x][j] == 0:
                board[x][j] = '#'

    elif direction == 1:
        for i in range(x-1, -1, -1):
            if board[i][y] == 6:
                break
            if board[i][y] == 0:
                board[i][y] = '#'

    elif direction == 2:
        for j in range(y-1, -1, -1):
            if board[x][j] == 6:
                break
            if board[x][j] == 0:
                board[x][j] = '#'

    elif direction == 3:
        for i in range(x+1, N):
            if board[i][y] == 6:
                break
            if board[i][y] == 0:
                board[i][y] = '#'

    return board


def get_score(board, cameras):
    # print(cameras)
    # copied = watch(copied, 2, 2, 3)
    for camera in cameras:
        x, y, c, k = camera
        cam = board[x][y]
        # print(x, y, cam, k)
        if cam == 1:
            board = watch(board, x, y, k)
        elif cam == 2:
            for i in range(k, 4, 2):
                # print(k,c, i)
                board = watch(board, x, y, i)
            #     watch(x, y, (k+2)%3)
        elif cam == 3:
            for i in range(2):
                # print(i, (k+i)%4)
                board = watch(board, x, y, (k+i)%4)
        elif cam == 4:
            for i in range(3):
                board = watch(board, x, y, (k+i)%4)

        elif cam == 5:
            for i in range(4):
                board = watch(board, x, y, i)

    # print(board)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    return cnt

visited = [False for _ in range(len(cameras))]
answer = N*M+1

def dfs(board, depth, idx):
    global answer
    if depth == D:
        copied = deepcopy(board)
        score = get_score(copied, cameras)
        answer = min(score, answer)
        return

    # for i in range(x, N):
    #     for j in range(y, M):
    #         if board[i][j] != 0 and board[i][j] != 6:
    #             for k in range(rots[board[i][j]]):
    #                 # cameras[i][j][k] = True
    #                 cameras[i][j] = k
    #                 dfs(depth+1, i+1, j+1)

    for i in range(idx, len(cameras)):
        x, y, c, k = cameras[i]
        if not visited[i]:
            for j in range(c):
                cameras[i][-1] = j
                visited[i] = True
                dfs(board, depth+1, idx+1)
                visited[i] = False


dfs(board, 0, 0)
print(answer)
