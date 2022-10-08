R, C, M = map(int, input().split())
shark = []
board = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    shark.append([r-1, c-1, s, d-1, z])
    board[r-1][c-1].append(i)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
row = [i for i in range(R)] + [i for i in range(R - 2, 0, -1)]
col = [i for i in range(C)] + [i for i in range(C - 2, 0, -1)]
# print(board)
# print(shark)

# R = 4
# C = 6
def get_loc(r, c, s, d):
    if d == 0:
        idx = (s - r) % len(row)
        # if ((-s+r) // (R-1)) % 2 == 0:
        #     d = 1
        if ((s-r)//(R-1)) % 2 == 0:
            d = 1
        r = row[idx]

    elif d == 1:
        idx = (s + r) % len(row)
        # if ((s+r) // (R-1)) % 2 == 1:
        #     d = 0
        if ((s+r)//(R-1)) % 2 == 1:
            d = 0
        r = row[idx]

    elif d == 2:
        idx = (s + c) % len(col)
        # if ((s+c) // (C-1)) % 2 == 1:
        if ((s+c)//(C-1)) % 2 == 1:
            d = 3
        # c = col[(s+c) % len(col)]
        c = col[idx]

    elif d == 3:
        # if ((-s+c) // (C-1)) % 2 == 0:
        #     d = 2
        idx = (s - c) % len(col)
        # print(idx)
        if ((s-c)//(C-1)) % 2 == 0:
            d = 2
        c = col[idx]
    # print(r, c, s, d)
    return r, c, s, d


def deepcopy(ref):
    copied = [[0 for _ in range(len(ref[0]))] for _ in range(len(ref))]
    for i in range(len(ref)):
        for j in range(len(ref[0])):
            copied[i][j] = ref[i][j]
    return copied


score = 0
for _c in range(C):
    # 1. fishing
    eaten = -1
    for i in range(R):
        if board[i][_c]:
            eaten = board[i][_c][0]
            break

    if eaten != -1:
        score += shark[eaten][4]
        shark.pop(eaten)
    # print(_c, eaten)

    # 2. moving
    board = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(len(shark)):
        r, c, s, d, z = shark[i]
        r, c, s, d = get_loc(r, c, s, d)
        shark[i] = [r, c, s, d, z]
        board[r][c].append(i)
    #
    # print(_c, shark)
    # print(_c, board)


    new_fish = []
    for i in range(R):
        for j in range(C):
            max_shark = -1
            for k in range(len(board[i][j])):
                if max_shark == -1:
                    max_shark = board[i][j][k]
                elif shark[max_shark][4] < shark[board[i][j][k]][4]:
                    max_shark = board[i][j][k]
            if max_shark != -1:
                new_fish.append(shark[max_shark])

    shark = deepcopy(new_fish)

    board = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(len(shark)):
        r, c, s, d, z = shark[i]
        board[r][c].append(i)

    # print(_c, shark)
    # print(_c, board)

print(score)


