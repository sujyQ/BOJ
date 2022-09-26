from collections import deque
N, M, fuel = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

taxi = list(map(int, input().split()))
taxi[0], taxi[1] = taxi[0] - 1, taxi[1] - 1

customer = [[] for _ in range(M)]
for i in range(M):
    line = list(map(int, input().split()))
    customer[i] = [line[0]-1, line[1]-1, line[2]-1, line[3]-1]

finish = [False for _ in range(M)]
# print(board)
# print(customer)

def bfs(positions, target_distance):
    sx, sy, tx, ty = positions
    queue = deque([[sx, sy, 0]])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = True
    distance = N*N

    # dx = [0, 0, -1, 1]
    # dy = [-1, 1, 0, 0]

    if sx >= tx and sy >= ty:
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

    elif sx >= tx and sy < ty:
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

    elif sx < tx and sy < ty:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

    else:
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

    while queue:
        x, y, d = queue.popleft()

        if (x == tx and y == ty) or target_distance < d:
            distance = d
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append([nx, ny, d+1])

    return distance


move_distance = []
for i in range(M):
    distance = bfs(customer[i], N*N)
    if distance == N*N:
        fuel = -1
        break
    move_distance.append(distance)


# movable = True
while True:
    if fuel < 0:
        # movable = False
        break
    if False not in finish:
        break

    target = -1
    target_distance = N * N
    for i in range(M):
        if finish[i]:
            continue

        distance = bfs(taxi + customer[i][:2], target_distance)
        if target_distance > distance:
            target = i
            target_distance = distance
        elif target_distance == distance:
            if customer[i][0] < customer[target][0]:
                target = i
                target_distance = distance
            elif customer[i][0] == customer[target][0] and customer[i][1] < customer[target][1]:
                target = i
                target_distance = distance

    if target_distance == N*N:
        fuel = -1
        break

    fuel -= target_distance + move_distance[target]
    if fuel < 0:
        # movable = False
        break
    else:
        fuel += 2 * move_distance[target]
        taxi = [customer[target][2], customer[target][3]]
        finish[target] = True


print(fuel if fuel >= 0 else -1)
