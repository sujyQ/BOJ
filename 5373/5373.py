n = int(input())

char_2_int = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5,}
int_2_color = {0: 'w', 1: 'y', 2: 'r', 3: 'o', 4: 'g', 5: 'b'}

def deepcopy(ref):
    copied = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(6)]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                copied[i][j][k] = ref[i][j][k]
    return copied


def rot90(s, d):
    # print(s, d)
    new_board = deepcopy(board)
    if d == '+':
        for i in range(3):
            for j in range(3):
                new_board[s][j][2-i] = board[s][i][j]
    elif d == '-':
        for i in range(3):
            for j in range(3):
                new_board[s][2-j][i] = board[s][i][j]

    # print(new_board)

    if s == 0 and d == '-':
        for i in range(3):
            new_board[2][0][i] = board[4][0][i]
            new_board[5][0][i] = board[2][0][i]
            new_board[3][0][i] = board[5][0][i]
            new_board[4][0][i] = board[3][0][i]
    elif s == 0 and d == '+':
        for i in range(3):
            new_board[4][0][i] = board[2][0][i]
            new_board[3][0][i] = board[4][0][i]
            new_board[5][0][i] = board[3][0][i]
            new_board[2][0][i] = board[5][0][i]
    elif s == 1 and d == '+':
        for i in range(3):
            new_board[3][2][i] = board[5][2][i]
            new_board[4][2][i] = board[3][2][i]
            new_board[2][2][i] = board[4][2][i]
            new_board[5][2][i] = board[2][2][i]
    elif s == 1 and d == '-':
        for i in range(3):
            new_board[5][2][i] = board[3][2][i]
            new_board[2][2][i] = board[5][2][i]
            new_board[4][2][i] = board[2][2][i]
            new_board[3][2][i] = board[4][2][i]
    elif s == 2 and d == '+':
        for i in range(3):
            new_board[0][2][i] = board[4][2-i][2]
            new_board[5][i][0] = board[0][2][i]
            new_board[1][2][i] = board[5][i][0]
            new_board[4][i][2] = board[1][2][2-i]
    elif s == 2 and d == '-':
        for i in range(3):
            new_board[4][2-i][2] = board[0][2][i]
            new_board[0][2][i] = board[5][i][0]
            new_board[5][i][0] = board[1][2][i]
            new_board[1][2][2-i] = board[4][i][2]
    elif s == 3 and d == '+':
        for i in range(3):
            new_board[0][0][i] = board[5][i][2]
            new_board[4][2-i][0] = board[0][0][i]
            new_board[1][0][i] = board[4][2-i][0]
            new_board[5][i][2] = board[1][0][i]
    elif s == 3 and d == '-':
        for i in range(3):
            new_board[5][i][2] = board[0][0][i]
            new_board[0][0][i] = board[4][2-i][0]
            new_board[4][2-i][0] = board[1][0][i]
            new_board[1][0][i] = board[5][i][2]
    elif s == 4 and d == '+':
        for i in range(3):
            new_board[0][2-i][0] = board[3][i][2]
            new_board[2][i][0] = board[0][i][0]
            new_board[1][2-i][2] = board[2][i][0]
            new_board[3][i][2] = board[1][i][2]
    elif s == 4 and d == '-':
        for i in range(3):
            new_board[3][i][2] = board[0][2-i][0]
            new_board[0][i][0] = board[2][i][0]
            new_board[2][i][0] = board[1][2-i][2]
            new_board[1][i][2] = board[3][i][2]
    elif s == 5 and d == '+':
        for i in range(3):
            new_board[0][i][2] = board[2][i][2]
            new_board[3][i][0] = board[0][2-i][2]
            new_board[1][i][0] = board[3][i][0]
            new_board[2][i][2] = board[1][2-i][0]
    elif s == 5 and d == '-':
        for i in range(3):
            new_board[2][i][2] = board[0][i][2]
            new_board[0][i][2] = board[3][2-i][0]
            new_board[3][i][0] = board[1][i][0]
            new_board[1][i][0] = board[2][2-i][2]

    return new_board


for _ in range(n):
    N = int(input())
    turns = input().split()
    board = [[[int_2_color[i] for _ in range(3)] for _ in range(3)] for i in range(6)]

    for i in range(N):
        t = turns[i]
        rotated = rot90(char_2_int[t[0]], t[1])
        board = deepcopy(rotated)

    #     print(board)
    # print('---------')
    for i in range(3):
        for j in range(3):
            print(board[0][i][j], end='')
        print()



