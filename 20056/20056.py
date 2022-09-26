N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
dead = []
for i in range(M):
    dead.append(False)
    line = list(map(int, input().split()))
    fireball.append([line[0]-1, line[1]-1, line[2], line[3], line[4]])
    board[line[0]-1][line[1]-1].append(i)

# print(board)
# print(fireball)
# print(dead)

turn = 1
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def merge(targets):
    m, s = 0, 0
    dir_odd, dir_even = True, True
    for t in targets:
        m += fireball[t][2]
        s += fireball[t][3]
        dir_odd = dir_odd and fireball[t][4] % 2 == 1
        dir_even = dir_even and fireball[t][4] % 2 == 0
        dead[t] = True

    return m // 5, s // len(targets), dir_odd or dir_even


for turn in range(K):
    if False not in dead:
        break

    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(fireball)):
        if dead[i]:
            continue

        x, y, m, s, d = fireball[i]
        x, y = x + s * dx[d], y + s * dy[d]
        x %= N
        y %= N
        board[x][y].append(i)
        fireball[i] = [x, y, m, s, d]

    # print(turn, board)
    # print(turn, fireball)

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                m, s, d = merge(board[i][j])

                if m > 0:
                    start = len(fireball)
                    board[i][j] = [start + k for k in range(4)]

                    for k in range(4):
                        if d:
                            fireball.append([i, j, m, s, k*2])
                        else:
                            fireball.append([i, j, m, s, 1+k*2])
                        dead.append(False)

    for i in range(len(fireball)):
        if fireball[i][2] == 0:
            dead[i] = True

    # print(turn, board)
    # print(turn, fireball)
    # print(turn, dead)

    # turn += 1

answer = 0
for i in range(len(fireball)):
    if dead[i]:
        continue
    answer += fireball[i][2]
print(answer)