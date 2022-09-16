N, M, H = map(int, input().split())

board = [[False for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True

# print(board)
combi = []
for i in range(H):
    for j in range(N-1):
        # print(i, j, board[i][j])
        if board[i][j]:
            continue
        if 0 < j and board[i][j-1]:
            continue
        if j < N-1 and board[i][j+1]:
            continue
        combi.append([i, j])
        # if not board[i][j] and 0 < j and not board[i][j-1] and j < N-1 and not board[i][j]:
        #     combi.append([i,j])

# print(combi)
answer = 4
# dx = [1, -1]
dy = [1, -1]

def is_itoi():
    for x in range(N):
        m = x
        for y in range(H):
            if board[y][m]:
                m += 1
            elif m > 0 and board[y][m - 1]:
                m -= 1
        # print(x, m)
        if m != x:
            return False
    return True

def dfs(depth, idx):
    global answer
    if depth >= answer:
        return

    if is_itoi():
        answer = min(answer, depth)
        return

    for i in range(idx, len(combi)):
        x, y = combi[i]
        if not board[x][y-1] and not board[x][y+1]:
            board[x][y] = True
            dfs(depth+1, i+1)
            board[x][y] = False


dfs(0, 0)

if answer == 4:
    answer = -1
print(answer)
