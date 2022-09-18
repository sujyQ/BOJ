from collections import deque
T = int(input())

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(queue, board):
    possible = True

    while queue:
        x, y, color = queue.popleft()
        # popped = queue.popleft()
        # print(popped)
        # x, y, color = popped
        board[x][y] = color

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == '?' and color == '.':
                queue.append([nx, ny, '#'])
            elif board[nx][ny] == '?' and color == '#':
                queue.append([nx, ny, '.'])
            elif board[nx][ny] != '?' and board[nx][ny] == color:
                possible = False
                break

        if not possible:
            break

    if possible:
        print('possible')
    else:
        print('impossible')


for i in range(1, T + 1):
    N, M = map(int, input().split())

    board = []
    s_x, s_y = 0, 0
    for j in range(N):
        c = input()
        board.append([])
        for k in range(M):
            board[j].append(c[k])
            if c[k] != '?':
                s_x, s_y = j, k

    print('#{}'.format(i), end=' ')

    if s_x == 0 and s_y == 0:
        print('possible')

    else:
        queue = deque([[s_x, s_y, board[s_x][s_y]]])
        bfs(queue, board)

