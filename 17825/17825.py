board = [
    [2*i for i in range(21)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40],
    [25, 30, 35, 40]
]

horse = [[0, 0], [0, 0], [0, 0], [0, 0]]
blue = [10, 20, 30]
answer = -1

eyes = list(map(int, input().split()))

def move(position, eye):
    x, y = position
    y += eye
    if y >= len(board[x]):
        x, y = -1, -1
    elif x == 0 and board[x][y] in blue:
        # x = blue.index(board[x][y])+1
        x = board[x][y] // 10
        y = 0
    elif x > 0 and board[x][y] in board[4]:
        y = board[4].index(board[x][y])
        x = 4
    elif board[x][y] == 40:
        x, y = 4, 3

    return x, y


def deepcopy(position):
    copied = []
    for _p in position:
        copied.append(_p)
    return copied


def dfs(depth, score):
    global answer
    if depth == 10:
        answer = max(answer, score)
        return

    for i in range(len(horse)):
        if horse[i] != -1:
            origin = deepcopy(horse[i])
            nx, ny = move(horse[i], eyes[depth])
            if nx == -1 and ny == -1:
                horse[i] = -1
                dfs(depth + 1, score)
                horse[i] = origin
            elif [nx, ny] not in horse:
                horse[i] = [nx, ny]
                dfs(depth+1, score + board[nx][ny])
                horse[i] = origin


dfs(0, 0)
print(answer)
