N = int(input())
used = [0] * N
mtx = []
for _ in range(N) :
    mtx.append(list(map(int, input().split())))

min_diff = 1e9


def DFS(N, mtx, used, depth, start) :
    # print(arr, r, depth, team, target)
    global min_diff
    if depth >= N//2:
        start = 0
        link = 0
        for i in range(N) :
            for j in range(i+1, N):
                if used[i] == 1 and used[j] == 1:
                    start += mtx[i][j] + mtx[j][i]
                elif used[i] == 0 and used[j] == 0:
                    link += mtx[i][j] + mtx[j][i]
        min_diff = min(min_diff, abs(start-link))

    else:
        for i in range(start, N):
            if used[i] == 0:
                used[i] = 1
                DFS(N, mtx, used, depth+1, i+1)
                used[i] = 0


DFS(N, mtx, used, 0, 0)
print(min_diff)