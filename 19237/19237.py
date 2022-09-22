N, M, k = map(int, input().split())

shark_board = [[-1 for _ in range(N)] for _ in range(N)]
sharks = [[0, 0, 0] for _ in range(M)]
smell_board = [[[-1, -1] for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] > 0:
            shark_board[i][j] = line[j]-1
            sharks[line[j]-1] = [i, j, 0]
            smell_board[i][j] = [line[j]-1, k]

d = list(map(int, input().split()))
for i in range(M):
    sharks[i][-1] = d[i]-1

priority = [[[0, 0, 0, 0] for _ in range(4)] for _ in range(M)]
for i in range(M):
    for j in range(4):
        line = list(map(int, input().split()))
        for t in range(4):
            priority[i][j][t] = line[t]-1

# print(sharks)
# print(shark_board)
# print(priority)
# print(smell_board)
out = [False for _ in range(M)]
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def finish():
    for i in range(1, M):
        if not out[i]:
            return False
    return True


def deepcopy(ref):
    copied = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            copied[i][j] = ref[i][j]
    return copied


while True:
    if time >= 1001:
        time = -1
        break

    # print(out)
    if finish():
        break

    # print(time)
    # print(sharks)
    # print(shark_board)

    # smell -1
    # print(smell_board)
    for i in range(N):
        for j in range(N):
            if smell_board[i][j] == [-1, -1]:
                continue
            if smell_board[i][j][1] == 0:
                smell_board[i][j] = [-1, -1]
            else:
                smell_board[i][j][1] -= 1

    # seek direction and move
    movable = [[[], []] for _ in range(M)]
    moved = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(M):
        if out[i]:
            continue

        x, y, d = sharks[i]
        # print(i, x, y, d)
        # print(smell_board)
        for j in range(4):
            nd = priority[i][d][j]
            nx, ny = x + dx[nd], y + dy[nd]
            # print(i, j, nd, nx, ny)

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # print(nx, ny)
            # print(smell_board[nx][ny])
            if smell_board[nx][ny] == [-1, -1]:
                movable[i][0].append(nd)
            elif smell_board[nx][ny][0] == i:
                # print(nx, ny)
                # print(smell_board[nx][ny])
                movable[i][1].append(nd)

        # print(movable)

    for i in range(M):
        if out[i]:
            continue

        if movable[i][0]:
            nd = movable[i][0][0]
        else:
            nd = movable[i][1][0]

        nx, ny = sharks[i][0] + dx[nd], sharks[i][1] + dy[nd]
        moved[nx][ny].append(i)
        sharks[i] = [nx, ny, nd]
        smell_board[nx][ny] = [i, k]

    # print(time, moved)
    # fight
    for i in range(N):
        for j in range(N):
            if len(moved[i][j]) >= 2:
                for s in moved[i][j][1:]:
                    out[s] = True
                moved[i][j] = moved[i][j][0]
                smell_board[i][j] = [moved[i][j], k]

    shark_board = deepcopy(moved)
    # print(time, shark_board)
    # print(time, smell_board)
    # print(out)

    time += 1

print(time)

