N, K = map(int, input().split())
A = list(map(int, input().split()))

up = 0
is_robot = [False for _ in range(2*N)]
robots = []
period = 2*N
turn = 1
# down = N-1
while True:
    up = (up-1) % period
    down = (up + N - 1) % period
    # for i in range(len(robots)):
    #     robots[i] = (robots[i] - 1) % period
    # tmp = is_robot[-1]
    # for i in range(1, period):
    #     is_robot[i] = is_robot[i-1]
    # is_robot[0] = tmp
    #
    # print(turn, robots)
    # print(turn, is_robot)
    # print(turn, up, down)
    # print(A)

    if is_robot[down]:
        is_robot[down] = False
        target = robots.index(down)
        robots.pop(target)
    #
    # print(turn, robots)
    # print(turn, is_robot)
    # print(A)

    for i in range(len(robots)):
        pos = robots[i]
        if not is_robot[(pos+1)%period] and A[(pos+1)%period] > 0:
            # if (pos + 1) % period == down:
            #     is_robot[pos] = False
            #     robots.pop(i)
            #     A[(pos+1) % period] -= 1
            # else:
            is_robot[pos] = False
            robots[i] = (pos + 1) % period
            is_robot[robots[i]] = True
            A[robots[i]] -= 1

    if is_robot[down]:
        is_robot[down] = False
        target = robots.index(down)
        robots.pop(target)

    # print(turn, robots)
    # print(turn, is_robot)
    # print(A)

    if A[up] > 0:
        A[up] -= 1
        robots.append(up)
        is_robot[up] = True

    # print(turn, robots)
    # print(turn, is_robot)
    # print(turn, A)

    cnt = 0
    for i in range(period):
        if A[i] == 0:
            cnt += 1

    if cnt >= K:
        break
    else:
        turn += 1

print(turn)
