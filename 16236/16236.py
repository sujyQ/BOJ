N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = -1


def up(board):
    arr = []
    for i in range(N):
        arr.append([])
        for j in range(N):
            if board[j][i] != 0:
                arr[i].append(board[j][i])

    for i, el in enumerate(arr):
        cnt = 0
        for j in range(N):
            if cnt+1 < len(el) and el[cnt]==el[cnt+1]:
                board[j][i] = el[cnt]*2
                cnt += 2
            elif cnt < len(el):
                board[j][i] = el[cnt]
                cnt += 1
            else:
                board[j][i] = 0
    # print(board)
    return board


def down(board):
    arr = []
    for i in range(N):
        arr.append([])
        for j in range(N-1, -1, -1):
            if board[j][i] != 0:
                arr[i].append(board[j][i])

    for i, el in enumerate(arr):
        cnt = 0
        for j in range(N-1, -1, -1):
            if cnt+1 < len(el) and el[cnt] == el[cnt+1]:
                board[j][i] = el[cnt]*2
                cnt += 2
            elif cnt < len(el):
                board[j][i] = el[cnt]
                cnt += 1
            else:
                board[j][i] = 0

    # print(board)
    return board

def right(board):
    arr = []
    for i in range(N):
        arr.append([])
        for j in range(N-1, -1, -1):
            if board[i][j] != 0:
                arr[i].append(board[i][j])

    for i, el in enumerate(arr):
        cnt = 0
        for j in range(N-1, -1, -1):
            if cnt+1 < len(el) and el[cnt] == el[cnt+1]:
                board[i][j] = el[cnt] * 2
                cnt += 2
            elif cnt < len(el):
                board[i][j] = el[cnt]
                cnt += 1
            else :
                board[i][j] = 0

    # print(board)
    return board


def left(board):
    arr = []
    for i in range(N):
        arr.append([])
        for j in range(N):
            if board[i][j] != 0:
                arr[i].append(board[i][j])

    # print(arr)

    for i, el in enumerate(arr):
        cnt = 0
        for j in range(N):
            # print(cnt, j)
            if cnt+1 < len(el) and el[cnt] == el[cnt+1]:
                board[i][j] = el[cnt] * 2
                cnt += 2
            elif cnt < len(el):
                board[i][j] = el[cnt]
                cnt += 1
            else:
                board[i][j] = 0

    # print(board)
    return board


def deepcopy(_b):
    copied = []
    for i in range(N):
        copied.append([])
        for j in range(N):
            copied[i].append(_b[i][j])

    return copied


def dfs(depth, board):
    global answer
    if depth >= 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    else:
        board2 = deepcopy(board)

        dfs(depth + 1, up(board))
        board = deepcopy(board2)        # 원상복귀
        dfs(depth + 1, down(board))
        board = deepcopy(board2)
        dfs(depth + 1, left(board))
        board = deepcopy(board2)
        dfs(depth + 1, right(board))
        board = deepcopy(board2)



dfs(0, board)
print(answer)
