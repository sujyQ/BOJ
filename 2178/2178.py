N, M = list(map(int, input().split()))
map = []
for _ in range(N):
    map.append(input())
# print(map)

visited = [[False] * M for _ in range(N)]
# print(visited)
visited[0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0, 1]]

answer = 1e9

while queue:
    x, y, d = queue.pop(0)

    if x == N-1 and y == M-1:
        answer = min(answer, d)
        break

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny] and map[nx][ny]=='1':
            visited[nx][ny] = True
            queue.append([nx, ny, d+1])


print(answer)
