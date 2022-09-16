N = int(input())
board = []
for i in range(N):
    b = list(map(int, input().split()))
    for j in range(N):
        if b[j] == 9:
            shark = [2, i, j]
    board.append(b)

# print(shark)
# print(board)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[shark[1], shark[2], 0]]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[shark[1]][shark[2]] = True
    while queue:
        i, j, d = queue.pop(0)
        # print(i, j, d)
        # print(queue)
        if i == x and j == y:
            return d

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if not visited[ni][nj] and board[ni][nj] <= shark[0]:
                visited[ni][nj] = True
                queue.append([ni, nj, d+1])

    return 999


def update_target(target, d, i, j):
    if d < target[0]:
        return [d, i, j]
    elif d == target[0] and i < target[1]:
        return [d, i, j]
    elif d == target[0] and i == target[1] and j < target[2]:
        return [d, i, j]
    else:
        return target


time = 0
eat = 0
while True:
    target = [999, -1, -1]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 or board[i][j] == 9:
                continue
            if board[i][j] < shark[0]:
                d = bfs(i, j)
                # print(time, i, j, d)
                # print(target)
                if d < target[0]:
                    target = update_target(target, d, i, j)
                # print(target)
    if target[0] == 999:
        break
    else:
        board[shark[1]][shark[2]] = 0
        shark[1], shark[2] = target[1], target[2]
        time += target[0]
        board[shark[1]][shark[2]] = 9
        eat += 1
    if shark[0] == eat:
        shark[0] += 1
        eat = 0
    # print(time, eat, shark)
    # print(board)

# print(bfs(0, 2))
print(time)