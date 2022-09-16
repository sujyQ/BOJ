N = int(input())
curves = []
for _ in range(N):
    curves.append(list(map(int, input().split())))

board = [[False for _ in range(101)] for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

mode = [[0]]
for i in range(1, 11):
    mode.append(mode[i - 1] + [(mode[i - 1][m] + 1) % 4 for m in range(len(mode[i - 1]) - 1, -1, -1)])

for i in range(0, 11):
    print(mode[i])

for curve in curves:
    x, y, d, g = curve
    nx, ny = x, y
    board[y][x] = True
    for m in mode[g]:
        # nm = (m+d)%4
        nx, ny = nx + dx[(m+d)%4], ny + dy[(m+d)%4]
        board[ny][nx] = True

    # print(board)
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1

print(answer)
