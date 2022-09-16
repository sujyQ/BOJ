N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T_shape = [[[0,0], [0, -1], [-1, 0], [1, 0]],
            [[0,0], [0, -1], [0, 1], [-1, 0]],
            [[0,0], [-1, 0], [0, 1], [1, 0]],
            [[0,-1], [0,0], [0,1], [1,0]]]

answer = -1
def dfs(depth, score, i, j):
    global answer
    if depth == 3:
        answer = max(answer, score)
        return

    for idx in range(len(dx)):
        ni, nj = i+dx[idx], j+dy[idx]
        if 0 <= ni and ni < N and 0 <= nj and nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(depth+1, score+board[ni][nj], ni, nj)
            visited[ni][nj] = False


def check_T(x, y):
    global answer
    for i in range(len(T_shape)):           # 4
        score = 0
        cnt = 0
        for j in range(len(T_shape[i])):    # 4
            _dx, _dy = T_shape[i][j]
            nx, ny = x+_dx, y+_dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                score += board[nx][ny]
                cnt += 1
            else:
                continue
        if cnt == 4:
            answer = max(answer, score)


for i in range(0, N):
    for j in range(0, M):
        visited[i][j] = True
        dfs(0, board[i][j], i, j)
        check_T(i, j)
        visited[i][j] = False

print(answer)
# print(final_trace)
