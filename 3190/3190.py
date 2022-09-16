from collections import deque

N = int(input())
K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r, c = list(map(int, input().split()))
    board[r-1][c-1] = 1

L = int(input())

path = deque([])
for _ in range(L):
    r, c = input().split()
    r = int(r)
    path.append([r, c])

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

snake = deque([[0,0]])
time = 0
direction = 3
nx, ny = 0, 1
change_time, change_dir = path.popleft()

while True:
    print(time, nx, ny, snake, direction)
    if (nx < 0 or nx >= N or ny < 0 or ny >= N) or board[nx][ny] == 2:
        break


    if board[nx][ny] == 1:
        snake.append([nx, ny])
        board[nx][ny] = 2
    else:
        snake.append([nx, ny])
        board[nx][ny] = 2
        r, c = snake.popleft()
        board[r][c] = 0

    time += 1
    if time == change_time:
        if direction == 0:
            if change_dir == 'L':
                direction = 2
            elif change_dir == 'D':
                direction = 3
        elif direction == 1:
            if change_dir == 'L':
                direction = 3
            elif change_dir == 'D':
                direction = 2
        elif direction == 2:
            if change_dir == 'L':
                direction = 1
            elif change_dir == 'D':
                direction = 0
        elif direction == 3:
            if change_dir == 'L':
                direction = 0
            elif change_dir == 'D':
                direction = 1

        if path:
            change_time, change_dir = path.popleft()

    nx, ny = nx + dx[direction], ny+dy[direction]
    # time += 1


print(time+1)
