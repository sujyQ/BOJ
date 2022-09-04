R, C, M = list(map(int, input().split()))

sharks = []
for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))
    sharks.append([r - 1, c - 1, s, d-1, z])

dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

alive = [True] * M


def fish(c):
    # print('------', c, '-------')
    r = R
    index = M
    for i in range(len(sharks)):
        if alive[i] and sharks[i][1] == c and r > sharks[i][0]:
            # print(i, sharks[i], sharks[i][0])
            r = sharks[i][0]
            index = i
    # print(r)
    eaten = 0
    if r < R:
        eaten = sharks[index][4]
        alive[index] = False
        # sharks.pop(index)
    return eaten


def move():
    for i, shark in enumerate(sharks):
        # res = shark[2]
        # while res > 0 and alive[i]:
        #     shark[0], shark[1] = shark[0]+dr[shark[3]], shark[1]+dc[shark[3]]
        #     if shark[0] >= R or shark[0] < 0:
        #         shark[0], shark[1] = shark[0] - 2*dr[shark[3]], shark[1] - 2*dc[shark[3]]
        #         shark[3] = 1-shark[3]
        #     elif shark[1] >= C or shark[1] < 0:
        #         shark[0], shark[1] = shark[0] - 2*dr[shark[3]], shark[1] - 2*dc[shark[3]]
        #         shark[3] = 5-shark[3]
        #     res -= 1

        if alive[i]:
            print(i, shark)
            r, c, s, d, z = shark
            if d == 0 or d == 1:
                res = r + s*dr[d]
                change = abs(res) // R
                while change > 0:
                    print(res, change, d, R)
                    if res > 0:
                        res = res - R
                    else:
                        res = -res-r
                    d = 1-d
                    change -= 1
                sharks[i] = [res, c, s, d, z]
            else:
                res = c + s*dr[d]
                change = abs(res) // C
                while change > 0:
                    print(res, change, d, R)
                    res = res - C
                    d = 5 - d
                    change -= 1
                sharks[i] = [r, res, s, d, z]
            print(i, sharks[i])





            # shark[0], shark[1] = shark[0]+shark[2]*dr[shark[3]], shark[1]+shark[2]*dc[shark[3]]
            # # print(i, shark)
            # if shark[0] < 0:
            #     shark[0] = abs(shark[0])
            #     shark[3] = 1
            # elif shark[0] >= R:
            #     shark[0] = shark[0] - R
            #     shark[3] = 0
            # if shark[1] <= 0:
            #     shark[1] = abs(shark[1])
            #     shark[3] = 2
            # elif shark[1] >= C:
            #     shark[1] = shark[1] - C
            #     shark[3] = 3
            # print(i, shark)


def merge():
    for i in range(len(sharks)-1):
        if alive[i]:
            for j in range(i+1, len(sharks)):
                if alive[j] and sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1]:
                    if sharks[i][-1] > sharks[j][-1]:
                        alive[j] = False
                    else:
                        alive[i] = False


def solution():
    answer = 0
    # print(sharks)
    # print(alive)
    # fish(0)
    # print(sharks)
    # print(alive)
    # move()
    # print(sharks)
    # print(alive)

    for i in range(C):
        print(i, fish(i))
        answer += fish(i)
        print(answer)
        move()
        merge()
    print(answer)


solution()
