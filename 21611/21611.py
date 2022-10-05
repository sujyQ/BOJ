N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
orders = []
for i in range(M):
    orders.append(list(map(int, input().split())))
    orders[i][0] -= 1

tor_d = [2, 1, 3, 0] * (N // 2) + [2]
tor_s = [ (i+1)//2 for i in range(1, 2*N-1)] + [N-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark = [(N+1)//2 - 1, (N+1)//2 - 1]

tornado = []
x, y = shark
for i in range(len(tor_d)):
    d = tor_d[i]
    for j in range(tor_s[i]):
        x, y = x + dx[d], y + dy[d]
        tornado.append([x, y])

# print(tornado)

answer = [0, 0, 0]

def make_1dim_board():
    _b = []
    for i in range(len(tornado)):
        x, y = tornado[i]
        _b.append(board[x][y])
    return _b


def make_board_matrix(vector):
    _b = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(tornado)):
        x, y = tornado[i]
        if i < len(vector):
            _b[x][y] = vector[i]
        else:
            _b[x][y] = 0
    return _b


def deepcopy(ref):
    copied = [0 for _ in range(len(ref))]
    for i in range(len(ref)):
        copied[i] = ref[i]
    return ref

for m in range(M):
    #-----shark moving-----
    d, s = orders[m]
    x, y = shark
    for i in range(s):
        x, y = x + dx[d], y + dy[d]
        if x < 0 or x >= N or y < 0 or y >= N:
            break
        board[x][y] = 0

    # print(m, board)

    board_vector = make_1dim_board()
    while True:
        #-----element moving-----
        # print(len(board_vector))
        start, keep = 0, 0
        passed = 0
        explosion = False
        new_vector = [0 for _ in range(len(board_vector))]
        copy = False
        # print(m, board_vector)
        for i in range(len(board_vector)):
            # print(i, start, keep, passed)
            if board_vector[i] != 0:
                keep += 1
                copy = True
            else:
                if copy:
                    new_vector[start:start+keep] = board_vector[start+passed:i]
                    start += keep if keep > 0 else 1
                    # passed += keep
                    keep = 0
                    copy = False
                    # print(new_vector)
                passed += 1
        if keep > 0:
            new_vector[start:start + keep] = board_vector[start + passed:]


        board_vector = deepcopy(new_vector)
        # print(m, board_vector)
        # print(len(board_vector))

        start = 0
        c = board_vector[0]
        cnt = 1
        for i in range(1, len(board_vector)):
            # if board_vector[i] == 0:
            #     break
            if board_vector[i] == c:
                cnt += 1
            elif cnt >= 4:
                # print(start, cnt)
                explosion = True
                for k in range(start, start + cnt):
                    # print(k)
                    answer[board_vector[k]-1] += 1
                    board_vector[k] = 0
                cnt = 1
                start = i
                c = board_vector[i]
            else:
                cnt = 1
                start = i
                c = board_vector[i]
        #     print(i, start, c, cnt)
        # print(board_vector)
        if not explosion:
            break


    # grouping
    new_vector = []
    count = 1
    c = board_vector[0]
    if c != 0:
        for i in range(1, len(board_vector)):
            if board_vector[i] == 0:
                new_vector.append(count)
                new_vector.append(c)
                break
            if len(new_vector) >= N*N-1:
                new_vector = new_vector[:N*N-1]
                break
            if board_vector[i] == c:
                count += 1
            else:
                new_vector.append(count)
                new_vector.append(c)
                c = board_vector[i]
                count = 1
        # print(i, new_vector)
    # board_vector = deepcopy(new_vector)
    # print(m, new_vector)
    board = make_board_matrix(new_vector)
    # print(m, board)


ans = 0
for i in range(len(answer)):
    ans += (i+1)*answer[i]
print(ans)