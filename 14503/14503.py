from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# print(board)
visited = [[False for _ in range(M)] for _ in range(N)]

cnt = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn(direction):
    nd = direction - 1
    return nd if nd >= 0 else 3

x, y, d = r, c, d

while True:
    visited[x][y] = True

    nd = d
    cleaned = False
    for i in range(4):
        nd = turn(nd)
        nx, ny = x + dx[nd], y + dy[nd]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0 and not visited[nx][ny]:
            x, y, d = nx, ny, nd
            cnt += 1
            cleaned = True
            break

    if not cleaned:
        nx, ny = x - dx[d], y - dy[d]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
            x, y, d = nx, ny, d
        elif nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 1:
            break

print(cnt)



