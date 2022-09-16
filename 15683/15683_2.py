N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cameras = []
D = 0
for i in range(N):
    for j in range(M):
        c = board[i][j]
        if c != 0 and c != 6:
            cameras.append([i, j, c])
            D += 1


def deepcopy(ref):
    copied = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copied[i][j] = ref[i][j]

    return copied


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

mode = [
    [[0]],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]


visited = [False for _ in range(len(cameras))]
answer = N*M+1

# print(cameras)

def watch(tmp, x, y, m):
    for direction in m:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx[direction], ny + dy[direction]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if tmp[nx][ny] == 6:
                break
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = '#'


def dfs(board, depth):
    global answer
    if depth == D:
        score = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    score += 1
        answer = min(score, answer)
        return

    camera = cameras[depth]
    x, y, c = camera
    tmp = deepcopy(board)
    for m in mode[c]:
        watch(tmp, x, y, m)
        dfs(tmp, depth+1)
        tmp = deepcopy(board)

    # for i in range(len(mode[c])):
    #     tmp = deepcopy(board)
    #     watch(tmp, x, y, )


dfs(board, 0)
print(answer)
