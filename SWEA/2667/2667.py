from collections import deque

N = int(input())
map = []
for _ in range(N):
    map.append(input())

visited = [[False] * N for _ in range(N)]

queue = deque([])
block = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if not visited[x][y]:
            cnt += 1
            visited[x][y] = True

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < N and ny >= 0 and ny < N and map[nx][ny] == '1':
                    # block[-1] += 1
                    # visited[nx][ny] = True
                    queue.append([nx, ny])

    return cnt


set_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and map[i][j] == '1':
            queue.append([i, j])
            # block.append(0)
            set_cnt += 1
            cnt = bfs()
            block.append(cnt)

print(set_cnt)
for b in sorted(block):
    print(b)
