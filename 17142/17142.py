N, M = map(int, input().split())
board = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j, False])


def bfs(v):
    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    for _v in v:
        queue.append([_v[0], _v[1], 0])
        visited[_v[0]][_v[1]] = 0

    while queue:
        x, y, d = queue.pop(0)
        # print(x, y, d)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = d+1
                queue.append([nx, ny, d+1])

    # print(visited)
    path_flag = False
    max_d = -1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                return N*N+1
            if board[i][j] == 0:
                path_flag = True
                max_d = max(max_d, visited[i][j])
    # print(max_d)
    if path_flag:
        return max_d
    else:
        return 0


answer = 1e9
def dfs(depth, v, idx):
    global answer
    if depth == M:
        # print(v)
        distance = bfs(v)
        answer = min(answer, distance)
        return

    for i in range(idx, len(virus)):
        if not virus[i][2]:
            virus[i][2] = True
            dfs(depth+1, v+[virus[i]], i+1)
            virus[i][2] = False

dfs(0, [], 0)
print(-1 if answer >= N*N+1 else answer)
