M, S = map(int, input().split())
fish = []
board = [[[] for _ in range(4)] for _ in range(4)]
for i in range(M):
    line = list(map(int, input().split()))
    fish.append([line[0]-1, line[1]-1, line[2]-1])
    # board[fish[i][0]][fish[i][1]].append(i)
sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
print(fish)
print(board)

def deepcopy(ref):
    copied = []
    dead_copied = []
    for i in range(len(ref)):
        # dead_copied[i] = dead[i]
        if not dead[i]:
            x, y, d = ref[i]
            copied.append([x, y, d])
            dead_copied.append(False)
    return copied, dead_copied


directions = [2, 6, 0, 4]
max_score = 0
max_root = [4, 4, 4]
dead = [False for _ in range(M)]
def dfs(depth, root):
    global max_score, max_root
    if depth >= 3:
        # print(root)
        score = 0
        x, y = sx, sy
        movable = True
        _d = []
        visited = [[False for _ in range(4)] for _ in range(4)]
        for i in root:
            d = directions[i]
            x, y = x + dx[d], y + dy[d]
            if x < 0 or x >= 4 or y < 0 or y >= 4:
                movable = False
                break
            if board[x][y] and not visited[x][y]:
                score += len(board[x][y])
                visited[x][y] = True

        if movable:
            # print(max_root, root)
            if max_score < score:
                max_root = root
                max_score = score
            elif max_score == score:
                max_root = min(max_root, root)

                # print(max_root, max_score, root, score)
        return

    for i in range(len(directions)):
        dfs(depth+1, root+[i])


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
smell = [[-1 for _ in range(4)] for _ in range(4)]
turn = 0

while True:
    if turn >= S:
        break
    fish, dead = deepcopy(fish)
    copied, dead_copied = deepcopy(fish)
    board = [[[] for _ in range(4)] for _ in range(4)]
    print(turn, dead)
    print(turn, fish)
    for i in range(len(fish)):
        if dead[i]:
            continue
        x, y, d = fish[i]
        moved = False
        for j in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                d = (d - 1) % 8
                continue
            if smell[nx][ny] > -1:
                d = (d - 1) % 8
                continue
            if sx == nx and sy == ny:
                d = (d - 1) % 8
                continue
            else:
                moved = True
                break

        if moved:
            fish[i] = [nx, ny, d]
            board[nx][ny].append(i)
        else:
            board[x][y].append(i)

    print(turn, fish)
    print(turn, board)

    max_score = 0
    max_root = [4, 4, 4]
    dfs(0, [])
    print(turn, max_root, max_score)
    # smell[x][y].append([2 for _ in range(len(board[x][y]))])
    # for f in board[x][y]:
    #     fish.pop(f)
    # board[x][y] = 0
    # for _d in dead:
    #     smell[_d[0]][_d[1]].append(2)
    x, y = sx, sy
    for r in max_root:
        _d = directions[r]
        x, y = x + dx[_d], y + dy[_d]
        for f in board[x][y]:
            smell[x][y] = turn
            dead[f] = True
        board[x][y] = []
        sx, sy = x, y
    print(turn, sx, sy)
    print(turn, dead)

    # print(board)
    # print(max_root, max_score)
    # print(fish)
    # print(smell)

    for i in range(4):
        for j in range(4):
            if smell[i][j] > -1 and smell[i][j] + 2 == turn:
                smell[i][j] = -1

    fish += copied
    dead += dead_copied

    print(turn, board)
    print(turn, fish)
    print(turn, dead)
    print(turn, smell)
    turn += 1


answer = 0
for i in range(len(fish)):
    if not dead[i]:
        answer += 1
print(answer)
