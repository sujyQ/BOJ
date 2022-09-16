circles = []
for _ in range(4):
    circles.append(input())

K = int(input())
rot = []
for i in range(K):
    target, dir = map(int, input().split())
    rot.append([target-1, dir])

# [left, right, top]
index = [[6, 2, 0] for _ in range(4)]

def rotate(idxs, direction):
    return (idxs[0] - direction) % 8, (idxs[1] - direction) % 8, (idxs[2] - direction) % 8


def deepcopy(ref):
    copied = [[0 for _ in range(3)] for _ in range(4)]
    for i in range(4):
        for j in range(3):
            copied[i][j] = ref[i][j]
    return copied


for target, dir in rot:
    copied = deepcopy(index)

    nd = -dir
    for i in range(target-1, -1, -1):
        l, r = index[i][1], index[i+1][0]
        if circles[i][l] == circles[i+1][r]:
            break
        else:
            _nl, _nr, _nt = rotate(index[i], nd)
            copied[i] = [_nl, _nr, _nt]
            nd *= -1

    nd = -dir
    for i in range(target+1, 4):
        l, r = index[i-1][1], index[i][0]
        if circles[i-1][l] == circles[i][r]:
            break
        else:
            _nl, _nr, _nt = rotate(index[i], nd)
            copied[i] = [_nl, _nr, _nt]
            nd *= -1

    nl, nr, nt = rotate(index[target], dir)
    copied[target] = [nl, nr, nt]
    index = deepcopy(copied)

answer = 0
for i in range(4):
    # print(circles[i], index[i][2])
    if circles[i][index[i][2]] == '1':
        answer += 2**i
print(answer)
