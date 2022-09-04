R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r, c, s, d, z])

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

cdir = [1, 0, 3, 2]

def get_next_loc(i, j, s, d):
    nr, nc = i + s * dr[d], j + s * dc[d]
    if 0 < nr <= R and 0 < nc <= C:
        return nr, nc, s, d

    print(nr, nc, s, d)


    if d == 0:      # 끝으로 이동
        nr -= i-1
    elif d == 1:
        nr -= R-i
    elif d == 2:
        nc -= C-j
    else:
        nc -= j-1

    print(nr, nc, s, d)

    if d == 0 or d == 1:        # 방향을 바꿔야 한다면 바꾸기
        k = nr // R
        change_dir = k % 2 == 0
        nr -= k * R
    else:
        k = nc // C
        change_dir = k % 2 == 0
    if change_dir:
        d = cdir[d]

    print(nr, nc, s, d)

    if d == 0:
        nr = R - nr
    elif d == 3:
        nc = C - nc

    return nr, nc, s, d


print(get_next_loc(1, 3, 5, 1))
print(get_next_loc(2, 4, 8, 1))
print(get_next_loc(4, 5, 0, 0))
print(get_next_loc(3, 3, 1, 1))




