N, L = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cnt = 0

def walk(road):
    ladder = [False for _ in range(N)]
    # print(road)

    for i in range(1, N):
        diff = road[i] - road[i-1]
        # print(diff)
        # print(ladder)
        if abs(diff) > 1:
            # print('return 1')
            return 0
        else:
            if diff == 0:
                continue
            # upstairs
            elif diff == 1:
                for j in range(i-1, i-L-1, -1):
                    if j < 0 or j >= N:
                        return 0
                    # print(j, i-1)
                    if road[j] != road[i-1] or ladder[j]:
                        # print('return 2')
                        return 0
                ladder[i-L:i] = [True for _ in range(L)]

            # downstairs
            elif diff == -1:
                for j in range(i, i+L):
                    if j < 0 or j >= N or road[j] != road[i] or ladder[j]:
                        # print(j, i, road[j], road[i], ladder[j])
                        # print('return 3')
                        return 0
                ladder[i:i+L] = [True for _ in range(L)]
    # if go:
    #     print(road)
    return 1


for i in range(N):
    cnt += walk(board[i])
    # print([board[j][i] for j in range(N)])
    cnt += walk([board[j][i] for j in range(N)])


print(cnt)

