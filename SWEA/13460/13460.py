N, M = list(map(int, input().split()))
map = [input() for _ in range(N)]

x_b, y_b, x_r, x_y = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        # print(i, j)
        if map[i][j] == 'B':
            x_b, y_b = i, j
        elif map[i][j] == 'R':
            x_r, y_r = i, j

visited = [[[[False] * M for _ in range(N)]
                        for _ in range(M)]
                        for _ in range(N)]

queue = []
queue.append([x_b, y_b, x_r, y_r, 0])
visited[x_b][y_b][x_r][y_r] = True

dx = [-1, 1, 0, 0]      # up down left right
dy = [0, 0, -1, 1]

def move(x, y, _dx, _dy):
    cnt = 0
    while map[x+_dx][y+_dy] != '#' and map[x][y] != 'O':
        x += _dx
        y += _dy
        cnt += 1

    return x, y, cnt


def bfs():
    while queue:
        x_b, y_b, x_r, y_r, d = queue.pop(0)
        # print(x_b, y_b, x_r, y_r, d)

        if d >= 10:
            break

        for i in range(4):
            nx_b, ny_b, cnt_b = move(x_b, y_b, dx[i], dy[i])
            nx_r, ny_r, cnt_r = move(x_r, y_r, dx[i], dy[i])
            # print(nx_b, ny_b, cnt_b, x_r, ny_r, cnt_r)

            if map[nx_b][ny_b] == 'O':
                continue
            if map[nx_r][ny_r] == 'O':
                print(d+1)
                return

            if nx_b == nx_r and ny_b == ny_r:
                if cnt_b > cnt_r:
                    nx_b -= dx[i]
                    ny_b -= dy[i]
                else:
                    nx_r -= dx[i]
                    ny_r -= dy[i]

            if not visited[nx_b][ny_b][nx_r][ny_r]:
                visited[nx_b][ny_b][nx_r][ny_r] = True
                queue.append([nx_b, ny_b, nx_r, ny_r, d+1])
    print(-1)

bfs()

