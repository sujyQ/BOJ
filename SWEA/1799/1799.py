## 틀림 ##

N = int(input())
chess = []
for _ in range(N):
    chess.append(list(map(int, input().split())))

print(chess)

bis = 0
dx = [-1, 1, -1, 1]
dy = [-1, 1, 1, -1]

# def DFS(depth, x, y):
#     global bis
#     if depth <= N:

for i in range(N) :
    for j in range(N) :
        if chess[i][j] == 1:
            print('visited', i, j)
            chess[i][j] = 0
            bis += 1
            if i-j >= 0:
                x_list = [x for x in range(i-j, N)]
                y_list = [y for y in range(0, N-(i-j))]
                # s_x, s_y = diff, 0
                # e_x, e_y = 4, 4-diff
            else:
                x_list = [x for x in range(0, N+i-j)]
                y_list = [y for y in range(-(i-j), N)]

            if i+j <= N-1:
                x_list += [x for x in range(0, i+j+1)]
                y_list += [y for y in range(i+j, -1, -1)]
            else:
                x_list += [x for x in range(i+j-(N-1), N)]
                y_list += [y for y in range(N-1, i+j-(N-1)+1, -1)]

            for x, y in zip(x_list, y_list):
                print(x, y)
                chess[x][y] = 0


# for i in range(N):
#     for j in range(N):
#         if i < N and j < N and i >= 0 and j >= 0:
#             if chess[i][j] == 1:
#                 bis += 1
#                 checkpoint(0, i, j)


# DFS(0, 0, 0)
print(bis)
