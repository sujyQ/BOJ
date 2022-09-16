N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    stop = True

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                opened = [[i, j]]
                queue = [[i, j]]
                population = 0
                country_cnt = 0
                visited[i][j] = True
                while queue:
                    x, y = queue.pop(0)
                    population += A[x][y]
                    country_cnt += 1
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(A[nx][ny] - A[x][y]) <= R:
                            opened.append([nx, ny])
                            queue.append([nx, ny])
                            visited[nx][ny] = True
                            stop = False

                avg_population = population // country_cnt
                for c in opened:
                    A[c[0]][c[1]] = avg_population
                # print(opened)
                # print(A)

    if stop:
        break
    else:
        answer += 1

print(answer)

