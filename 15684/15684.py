N, M, H = map(int, input().split())

board = [[False for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True

# print(board)

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
    if depth == 4:
        return

    check = is_itoi()
    if check:
        answer = min(answer, depth)
        return

    for i in range(idx, H*(N-1)):
        y = i // H
        x = i % H
        if board[x][y]:
            continue
        if 0 < y and board[x][y-1]:
            continue
        if y < N-1 and board[x][y+1]:
            continue

        board[x][y] = True
        dfs(depth+1, i+1)
        board[x][y] = False


dfs(0, 0)

if answer == 4:
    answer = -1
print(answer)
