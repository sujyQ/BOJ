N = int(input())
S = N ** 2
order = []
favor = []
for _ in range(S):
    line = list(map(int, input().split()))
    order.append(line[0])
    favor.append(line[1:])


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

board = [[-1 for _ in range(N)] for _ in range(N)]

for idx in range(S):
    max_cnt = 0
    position = [N, N]
    max_empty = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] != -1:
                continue
            cnt = 0
            empty = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if board[ni][nj] == -1:
                    empty += 1
                elif board[ni][nj] in favor[idx]:
                    cnt += 1

            # print(i, j, max_cnt, max_empty, cnt, empty, position)

            if max_cnt < cnt:
                position = [i, j]
                max_cnt = cnt
                max_empty = empty
            elif max_cnt == cnt and max_empty < empty:
                position = [i, j]
                max_empty = empty
            elif max_cnt == cnt and max_empty == empty and position[0] > i:
                position = [i, j]
            elif max_cnt == cnt and max_empty == empty and position[0] == i and position[1] > j:
                position = [i, j]

            # print(i, j, max_cnt, max_empty, cnt, empty, position)

    # print(position)
    board[position[0]][position[1]] = order[idx]
    # print(board)


# print(board)

answer = 0
score = [0, 1, 10, 100, 1000]
for i in range(N):
    for j in range(N):
        cnt = 0
        s = board[i][j]
        ord = order.index(s)

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if board[ni][nj] in favor[ord]:
                cnt += 1
        # print(i, j, s, ord, cnt, score[cnt])

        answer += score[cnt]
print(answer)