from collections import deque
N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def deepcopy(ref):
    copied = [[-1 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copied[i][j] = ref[i][j]

    return copied


def spread(copied):
    for i in range(N):
        for j in range(M):
            if copied[i][j] == 2:
                virus = deque([[i, j]])
                while virus:
                    x, y = virus.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx >= 0 and nx < N and ny >= 0 and ny < M and copied[nx][ny] == 0:
                            copied[nx][ny] = 2
                            virus.append([nx, ny])
    return copied


def score_func(copied):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copied[i][j] == 0:
                cnt += 1
    return cnt


answer = -1
def DFS(depth, x, y):
    global answer
    if depth == 3:
        polluted = spread(deepcopy(board))
        answer = max(answer, score_func(polluted))
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                DFS(depth + 1, i, j)
                board[i][j] = 0


DFS(0, 0, 0)
print(answer)
