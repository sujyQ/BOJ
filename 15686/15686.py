N, M = map(int, input().split())
board = []
sellers = []
houses = []
for i in range(N):
    b = list(map(int, input().split()))
    board.append(b)
    for j in range(N):
        if board[i][j] == 2:
            sellers.append([i, j, False])
        if board[i][j] == 1:
            houses.append([i, j])

opened = [False for _ in range(len(sellers))]
answer = 1e5

# print(sellers)

def deepcopy(ref):
    copied = []
    for i in range(N):
        copied.append([])
        for j in range(N):
            copied[i].append(ref[i][j])
    return copied


# def get_score(arr, i, j):
#     # print(arr)
#     queue = deque([[i, j]])
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     visited = [[False for _ in range(N)] for _ in range(N)]
#
#     while queue:
#         x, y = queue.popleft()
#         # print(x, y)
#         visited[x][y] = True
#         if arr[x][y] == 2:
#             return abs(x - i) + abs(y - j)
#
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 queue.append([nx, ny])


def bfs():
    tmp = deepcopy(board)
    for i in range(len(sellers)):
        x, y, o = sellers[i]
        if o:
            tmp[x][y] = 2
        else:
            tmp[x][y] = 0

    score = 0
    for i in range(len(houses)):
        x, y = houses[i]
        score += get_score(tmp, x, y)

    return score


def get_score():
    score = 0
    for i in range(len(houses)):
        min_distance = 1e5
        x, y = houses[i]
        for j in range(len(sellers)):
            if sellers[j][-1]:
                min_distance = min(min_distance, abs(x-sellers[j][0])+abs(y-sellers[j][1]))
        score += min_distance
    return score


def dfs(depth, idx):
    # print(depth, i, j)
    global answer
    if depth > M:
        return

    if 0 < depth:
        score = get_score()
        # print(sellers, score)
        answer = min(answer, score)
        # return
        # pass

    # tmp = deepcopy(arr)
    # for x in range(i, N):
    #     for y in range(j, N):
    #         if arr[x][y] == 2:
    #             print(depth, x, y)
    #             arr[x][y] = 0
    #             # visited[x][y] = True
    #             dfs(depth+1, arr, x+1, y+1)
    #             # visited[x][y] = False
    #             # tmp = deepcopy(arr)
    #             arr[x][y] = 2
    for i in range(idx, len(sellers)):
        if not sellers[i][-1]:
            sellers[i][-1] = True
            # opened[i] = True
            dfs(depth+1, i+1)
            sellers[i][-1] = False
            # opened[i] = False


dfs(0, 0)
print(answer)

