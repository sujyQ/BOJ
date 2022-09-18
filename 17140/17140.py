r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

R = 3
C = 3


def operate(A):
    max_len = 0
    for i in range(R):
        count = [[i, 0] for i in range(1, 101)]
        for j in range(C):
            if A[i][j] == 0:
                continue
            count[A[i][j]-1][1] += 1
        count.sort(key=lambda x: (x[1], x[0]))
        new_row = []
        for c in count:
            if c[1] > 0:
                new_row.append(c[0])
                new_row.append(c[1])
        A[i] = new_row
        max_len = max(max_len, len(A[i]))

    for i in range(R):
        if len(A[i]) < max_len:
            A[i] += [0 for _ in range(max_len - len(A[i]))]
        if len(A[i]) > 100:
            A[i] = A[i][:100]

    return A


def transpose(A):
    _A = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            _A[i][j] = A[j][i]

    return _A


time = 0
while True:
    if time == 101:
        print(-1)
        break
    if r <= R and c <= C and A[r-1][c-1] == k:
        print(time)
        break

    if R >= C:
        A = operate(A)
        R, C = len(A), len(A[0])

    else:
        # print(A)
        _A = transpose(A)
        R, C = len(_A), len(_A[0])
        # print(A)
        _A = operate(_A)
        # print(A)
        A = transpose(_A)
        R, C = len(A), len(A[0])
        # print(A)

    # R = len(A)
    # C = len(A[0])

    # print(A)

    time += 1
