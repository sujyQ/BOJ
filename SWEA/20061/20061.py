N = int(input())
blocks = []
for _ in range(N):
    t, x, y = map(int, input().split())
    blocks.append([t, x, y])

blue_T = [[0 for _ in range(4)] for _ in range(6)]
green = [[0 for _ in range(4)] for _ in range(6)]

def move(block):
    t, x, y = block
    if t == 1:
        for i in range(6):
            if i == 5:
                green[i][y] = 1
            elif green[i+1][y] == 1 and green[i][y] == 0:
                green[i][y] = 1
                break

        for i in range(6):
            if i == 5:
                blue_T[i][3-x] = 1
            elif blue_T[i+1][3-x] == 1 and blue_T[i][3-x] == 0:
                blue_T[i][3-x] = 1
                break

    elif t == 2:
        for i in range(5):
            if i == 4:
                blue_T[i][3-x] = 1
                blue_T[i+1][3-x] = 1
            elif blue_T[i+2][3-x] == 1 and blue_T[i][3-x] == 0 and blue_T[i+1][3-x] == 0:
                blue_T[i][3-x] = 1
                blue_T[i+1][3-x] = 1
                break

        for i in range(6):
            if i == 5:
                green[i][y] = 1
                green[i][y + 1] = 1
            elif green[i][y] == 0 and green[i][y+1] == 0 and (green[i+1][y] == 1 or green[i+1][y+1] == 1):
                green[i][y] = 1
                green[i][y + 1] = 1
                break

    elif t == 3:
        for i in range(6):
            if i == 5:
                blue_T[i][3-x] = 1
                blue_T[i][3-x-1] = 1
            elif blue_T[i][3-x] == 0 and blue_T[i][3-x-1] == 0 and (blue_T[i+1][3-x] == 1 or blue_T[i+1][3-x-1] == 1):
                blue_T[i][3-x] = 1
                blue_T[i][3-x-1] = 1
                break

        for i in range(5):
            if i == 4:
                green[i][y] = 1
                green[i+1][y] = 1
            elif green[i][y] == 0 and green[i+1][y] == 0 and green[i+2][y] == 1:
                green[i][y] = 1
                green[i+1][y] = 1
                break


def delete():
    s = 0
    i = 5
    while i >= 0:
        if 0 not in green[i]:
            s += 1
            green[0:i+1] = [[0 for _ in range(4)]] + green[0:i]
        else:
            i -= 1
    i = 5
    while i >= 0:
        if 0 not in blue_T[i]:
            s += 1
            blue_T[0:i+1] = [[0 for _ in range(4)]] + blue_T[0:i]
        else:
            i -= 1

    move_green = 0
    move_blue = 0
    for i in range(0, 2):
        if 1 in green[i]:
            move_green += 1
        if 1 in blue_T[i]:
            move_blue += 1
    green[0:6] = [[0 for _ in range(4)] for _ in range(move_green)] + green[0:6-move_green]
    blue_T[0:6] = [[0 for _ in range(4)] for _ in range(move_blue)] + blue_T[0:6-move_blue]

    return s


def sum():
    s = 0
    for i in range(2, 6):
        for j in range(4):
            s += blue_T[i][j] + green[i][j]
    return s


score = 0
for i, block in enumerate(blocks):
    move(block)
    score += delete()

print(score)
print(sum())
