N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


dice = [0, 1, 2, 3, 4, 5]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
bottom = 5
change = [2, 3, 0, 1]

score = 0
turn = 0
x, y = 0, 0
d = 0

def roll(d):
    if d == 0:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif d == 1:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    elif d == 2:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif d == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]


def bfs(x, y, c):
    queue = [[x, y]]
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)
        cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and board[nx][ny] == c:
                queue.append([nx, ny])
                visited[nx][ny] = True

    return cnt * c


while True:
    if turn >= K:
        break
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        d = change[d]
        nx, ny = x + dx[d], y + dy[d]
    # print(turn, d)
    # print(turn, nx, ny)
    roll(d)
    # print(turn, dice)

    score += bfs(nx, ny, board[nx][ny])
    # print(turn, score)
    # print(board[nx][ny], dice[bottom])
    if board[nx][ny] > dice[bottom]+1:
        d = (d - 1) % 4
    elif board[nx][ny] < dice[bottom]+1:
        d = (d + 1) % 4
    # print(turn, d)

    x, y = nx, ny
    turn += 1

print(score)