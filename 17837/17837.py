N, K = map(int, input().split())
board = []
horse = []
for _ in range(N):
    board.append(list(map(int, input().split())))

t = [[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    t[x-1][y-1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
change = [1, 0, 3, 2]

turn = 0
stop = False
while True:
    if turn > 1000 or stop:
        break

    turn += 1
    for i in range(K):
        x, y, d = horse[i]
        order = t[x][y].index(i)
        move = t[x][y][order:]
        # print(move)
        t[x][y] = t[x][y][:order]

        nx, ny = x + dx[d], y + dy[d]
        changed = False

        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            d = change[d]
            nx, ny = x + dx[d], y + dy[d]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            nx, ny = x, y
            t[nx][ny] += move
            for h in move:
                horse[h][0], horse[h][1] = x, y
            horse[i][2] = d

        elif board[nx][ny] == 0:
            t[nx][ny] += move
            for h in move:
                horse[h][0], horse[h][1] = nx, ny
            horse[i][2] = d

        elif board[nx][ny] == 1:
            move.reverse()
            t[nx][ny] += move
            for h in move:
                horse[h][0], horse[h][1] = nx, ny
            horse[i][2] = d

        if len(t[nx][ny]) >= 4:
            stop = True
            break
    # print(turn, horse)
    # print(turn, t)

print(turn if turn <= 1000 else -1)

