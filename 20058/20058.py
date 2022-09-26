N, Q = map(int, input().split())
W = 2 ** N
board = []
for _ in range(W):
    board.append(list(map(int, input().split())))
level = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate(x, y):
    for i in range(_w):
        for j in range(_w):
            new_board[x+j][y+_w-1-i] = board[x+i][y+j]


def deepcopy(ref):
    copied = [[0 for _ in range(W)] for _ in range(W)]
    for i in range(W):
        for j in range(W):
            copied[i][j] = ref[i][j]
    return copied


def bfs(x, y):
    queue = [[x, y]]
    cnt = 0
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)
        cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= W or ny < 0 or ny >= W:
                continue
            if not visited[nx][ny] and board[nx][ny] >= 1:
                queue.append([nx, ny])
                visited[nx][ny] = True

    return cnt


for q in range(Q):
    L = level[q]
    _w = 2**L

    if _w > 1:
        new_board = [[0 for _ in range(W)] for _ in range(W)]

        for i in range(0, W, _w):
            for j in range(0, W, _w):
                rotate(i, j)

        board = deepcopy(new_board)

    delete = []

    for i in range(W):
        for j in range(W):
            if board[i][j] <= 0:
                continue
            # if (i == 0 and j == 0) or (i == 0 and j == W-1) or (i == W-1 and j == 0) or (i == W-1 and j == W-1):
            #     continue
            cnt = 0
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if ni < 0 or ni >= W or nj < 0 or nj >= W:
                    continue
                if board[ni][nj] > 0:
                    cnt += 1
            if cnt < 3:
                delete.append([i, j])
                # board[i][j] -= 1

    for i, j in delete:
        board[i][j] -= 1


visited = [[False for _ in range(W)] for _ in range(W)]
answer = 0
ice = 0
for i in range(W):
    for j in range(W):
        ice += board[i][j]
        if not visited[i][j] and board[i][j] > 0:
            answer = max(answer, bfs(i, j))

print(ice)
print(answer)
