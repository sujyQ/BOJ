R, C, K = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
heater = []
target = []
for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        if line[j] == 0:
            continue
        elif line[j] == 5:
            target.append([i, j])
        else:
            heater.append([i, j, line[j]-1])
W = int(input())
wall = [[[] for _ in range(C)] for _ in range(R)]
for i in range(W):
    x, y, t = map(int, input().split())
    wall[x-1][y-1].append(t)

dx = [[-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
dy = [[1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]
dt = [
    [[[0, 0, 0], [-1, 0, 1]],
      [[0, 0, 1]],
      [[1, 0, 0], [1, 0, 1]]],
    [[[0, 0, 0], [-1, -1, 1]],
     [[0, -1, 1]],
     [[1, 0, 0],[1, -1, 1]]],
    [[[0, -1, 1], [0, -1, 0]],
     [[0, 0, 0]],
     [[0, 0, 1], [0, 1, 0]]],
    [[[0, -1, 1], [1, -1, 0]],
     [[1, 0, 0]],
     [[0, 0, 1], [1, 1, 0]]]
]

def wind(x, y, t):
    visited = [[False for _ in range(C)] for _ in range(R)]

    if t == 0:
        queue = [[x, y+1, 5]]
    elif t == 1:
        queue = [[x, y-1, 5]]
    elif t == 2:
        queue = [[x-1, y, 5]]
    elif t == 3:
        queue = [[x+1, y, 5]]

    _dx, _dy, _dt = dx[t], dy[t], dt[t]
    # print(_dx, _dy, _dt)
    while queue:
        i, j, k = queue.pop(0)
        # print(i, j, k)
        board[i][j] += k

        if k > 1:
            for d in range(3):
                ni, nj = i + _dx[d], j + _dy[d]

                if ni < 0 or ni >= R or nj < 0 or nj >= C:
                    continue
                if visited[ni][nj]:
                    continue
                movable = True
                for l in range(len(_dt[d])):
                    dti, dtj, _t = _dt[d][l]
                    # print(i, j, t, d, l)
                    # print(dti, dtj, i + dti, j + dtj)
                    if _t in wall[i+dti][j+dtj]:
                        movable = False
                        break
                if movable:
                    # print('appended', ni, nj, k-1)
                    visited[ni][nj] = True
                    queue.append([ni, nj, k-1])


def deepcopy(ref):
    copied = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            copied[i][j] = ref[i][j]
    return copied


finish = False
chocolate = 0
while True:
    if finish:
        break

    if chocolate >= 100:
        chocolate = 101
        break

    for i in range(len(heater)):
        x, y, t = heater[i]
        wind(x, y, t)

    # print(board)

    new_board = deepcopy(board)
    for i in range(R-1, -1, -1):
        for j in range(C):
            if i >= 1 and 0 not in wall[i][j]:
                d = abs(board[i][j] - board[i-1][j]) // 4
                if board[i][j] > board[i-1][j]:
                    new_board[i][j] -= d
                    new_board[i-1][j] += d
                elif board[i][j] < board[i-1][j]:
                    new_board[i][j] += d
                    new_board[i-1][j] -= d
            if j < C-1 and 1 not in wall[i][j]:
                d = abs(board[i][j] - board[i][j+1]) // 4
                if board[i][j] > board[i][j+1]:
                    new_board[i][j] -= d
                    new_board[i][j+1] += d
                elif board[i][j] < board[i][j+1]:
                    new_board[i][j] += d
                    new_board[i][j+1] -= d
    board = deepcopy(new_board)
    # print(board)

    for i in range(R):
        if board[i][0] > 0:
            board[i][0] -= 1
        if board[i][C-1] > 0:
            board[i][C-1] -= 1

    for i in range(1, C-1):
        if board[0][i] > 0:
            board[0][i] -= 1
        if board[R-1][i] > 0:
            board[R-1][i] -= 1

    # board[0][0] += 1
    # board[0][C-1] += 1
    # board[R-1][0] += 1
    # board[R-1][C-1] += 1

    chocolate += 1

    finish = True
    for i in range(len(target)):
        x, y = target[i]
        if board[x][y] < K:
            finish = False
            break

    # print(board)

print(chocolate)

