M, S = map(int, input().split())
fish = []
for i in range(M):
    x, y, d = map(int, input().split())
    fish.append([x-1, y-1, d-1])

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

smell = [[0 for _ in range(4)] for _ in range(4)]

def deepcopy(ref):
    copied = [[0 for _ in range(len(ref[0]))] for _ in range(len(ref))]
    for i in range(len(ref)):
        for j in range(len(ref[0])):
            copied[i][j] = ref[i][j]

    return copied

direction = [2, 0, 6, 4]

def dfs(depth, score, x, y, root, visited):
    global max_fish, min_root
    if depth == 3:
        if score > max_fish:
            max_fish = score
            min_root = root
        elif score == max_fish:
            min_root = min(min_root, root)
        return

    else:
        for i in range(4):
            d = direction[i]
            nx, ny = x + dx[d], y + dy[d]
            # _v = deepcopy(visited)
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            # print(nx, ny, visited[nx][ny])
            # if not visited[nx][ny]:
            if [nx, ny] not in visited:
                s = score + len(board[nx][ny])
                # _v[nx][ny] = True
            else:
                s = score
            # print(root, i, s, nx, ny)
            # print(visited)
            dfs(depth+1, s, nx, ny, root + [i], visited + [[nx, ny]])
            # visited[nx][ny] = False


for _s in range(S):
    copied_fish = deepcopy(fish)
    board = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(len(fish)):
        move = False
        x, y, d = fish[i]
        nx, ny, nd = x, y, d
        for j in range(8):
            nx, ny = x + dx[nd], y + dy[nd]
            # print(i, nx, ny, nd)
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or smell[nx][ny] > 0 or [nx, ny] == [sx, sy]:
                nd = (nd-1) % 8
                continue
            else:
                move = True
                break
        if move:
            fish[i] = [nx, ny, nd]
            board[nx][ny].append(i)
        else:
            fish[i] = [x, y, d]
            board[x][y].append(i)
    # print(_s, fish)
    # print(_s, board)

    visited = [[False for _ in range(4)] for _ in range(4)]
    min_root = [4, 4, 4]
    max_fish = 0
    # print(sx, sy)
    dfs(0, 0, sx, sy, [], [])
    # print(_s, min_root, max_fish)

    x, y = sx, sy
    dead = [False for _ in range(len(fish))]
    for i in min_root:
        d = direction[i]
        x, y = x + dx[d], y + dy[d]
        # print(x, y)
        if len(board[x][y]) > 0:
            smell[x][y] = 3
            for d in board[x][y]:
                dead[d] = True
        sx, sy = x, y

    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1
    # print(_s, smell)
    # print(_s, dead)
    new_fish = []
    for f in range(len(fish)):
        if not dead[f]:
            new_fish.append(fish[f])
    fish = deepcopy(new_fish)
    fish += copied_fish

    # print(_s, fish)

print(len(fish))
