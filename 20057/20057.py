N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

direction = [0, 1, 2, 3] * (N//2) + [0]

distance = []
for i in range(1, N):
    distance += [i, i]
distance.append(N-1)
# print(distance)
# print(direction)
x, y = N//2, N//2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

spread = [[[-1, -1], [1, -1], [-1, 0], [1, 0], [0, -2], [-2, 0], [2, 0], [-1, 1], [1, 1]],
            [[1, -1], [1, 1], [0, -1], [0, 1], [2, 0], [0, -2], [0, 2], [-1, -1], [-1, 1]],
            [[-1, 1], [1, 1], [-1, 0], [1, 0], [0, 2], [-2, 0], [2, 0], [-1, -1], [1, -1]],
            [[-1, -1], [-1, 1], [0, -1], [0, 1], [-2, 0], [0, -2], [0, 2], [1, -1], [1, 1]]]
percent = [0.1, 0.1, 0.07, 0.07, 0.05, 0.02, 0.02, 0.01, 0.01]

answer = 0
for i in range(len(direction)):
    d = direction[i]
    for j in range(distance[i]):
        # print(x, y)
        x, y = x + dx[d], y + dy[d]
        amount = board[x][y]
        for k in range(9):
            nx, ny = x + spread[d][k][0], y + spread[d][k][1]
            out = int(board[x][y]*percent[k])
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                answer += out
            else:
                board[nx][ny] += out
            amount -= out
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            answer += amount
        else:
            board[nx][ny] += amount
print(answer)
