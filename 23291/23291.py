N, K = map(int, input().split())
fish = list(map(int, input().split()))


def rotate90(ref):
    h, w = len(ref), len(ref[0])
    copied = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(len(ref[0])):
        for j in range(len(ref)):
            copied[i][j] = ref[h-j-1][i]
    return copied


def deepcopy(ref):
    copied = []
    for i in range(len(ref)):
        copied.append([0 for _ in range(len(ref[i]))])
        for j in range(len(ref[i])):
            copied[i][j] = ref[i][j]
    return copied


def vectorization(mtx):
    vector = []
    for i in range(len(mtx[-1])):
        for j in range(len(mtx)-1, -1, -1):
            if i >= len(mtx[j]):
                continue
            vector.append(mtx[j][i])
    return vector


def control_fish(board):
    new_board = deepcopy(board)
    # print('--')
    # print(new_board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j != len(board[i]) - 1:
                d = abs(board[i][j] - board[i][j + 1]) // 5
                # print(d, i, j, i, j+1)
                if d > 0 and board[i][j] > board[i][j + 1]:
                    new_board[i][j] -= d
                    new_board[i][j + 1] += d
                elif d > 0 and board[i][j] < board[i][j + 1]:
                    new_board[i][j] += d
                    new_board[i][j + 1] -= d
            # print(new_board)
            if i != len(board) - 1:
                # print(d, i, j, i+1, j)
                d = abs(board[i][j] - board[i + 1][j]) // 5
                if d > 0 and board[i][j] > board[i + 1][j]:
                    new_board[i][j] -= d
                    new_board[i + 1][j] += d
                elif d > 0 and board[i][j] < board[i + 1][j]:
                    new_board[i][j] += d
                    new_board[i + 1][j] -= d
            # print(new_board)
    board = deepcopy(new_board)
    return board

turn = 0
while max(fish) - min(fish) > K:
    min_fish = min(fish)
    for i in range(N):
        if fish[i] == min_fish:
            fish[i] += 1

    board = [[fish[0]], [fish[i] for i in range(1, N)]]
    # print(board)
    while True:
        h, w = len(board), len(board[0])
        # print(h, w, len(board[-1]))
        if h > len(board[-1]) - w:
            break

        ref = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                ref[i][j] = board[i][j]

        rotated = rotate90(ref)
        board = rotated + [board[-1][w:]]
        # print(board)

    board = control_fish(board)

    # print(board)

    fish = vectorization(board)

    board = [fish]
    for i in range(2):
        left = len(board[0]) // 2
        _r, res = [], []
        for j in range(i+1):
            _r.append(board[j][:left])
            res.append(board[j][left:])
        rotated = rotate90(rotate90(_r))
        board = rotated + res
    # print(board)

    board = control_fish(board)
    # print(board)
    fish = vectorization(board)
    # print(fish)




    turn += 1

print(turn)