N = int(input())
board= []
for _ in range(N):
    board.append(list(map(int, input().split())))


def d1_e_d2(x, y, d1, d2):
    population = [0 for _ in range(5)]
    for i in range(N):
        # print(i)
        if i < x:
            population[0] += sum(board[i][:y + 1])
            population[1] += sum(board[i][y + 1:])
            # print(0, population)
        elif x <= i < x + d1:
            population[0] += sum(board[i][:y - (i - x)])
            population[4] += sum(board[i][y - (i - x):y + (i - x) + 1])
            population[1] += sum(board[i][y + (i - x) + 1:])
            # print(1, population)
        elif i == x+d1:
            population[2] += sum(board[i][:y-d1])
            population[4] += sum(board[i][y-d1:y+d2+1])
            population[1] += sum(board[i][y+d2+1:])
            # print(2, population)
        elif x + d1 < i <= x + d1 + d2:
            population[2] += sum(board[i][:y - d1 + (i - x - d1)])
            population[4] += sum(board[i][y - d1 + (i - x - d1):y + d2 - (i - x - d2) + 1])
            population[3] += sum(board[i][y + d2 - (i - x - d2) + 1:])
            # print(3, population)
        elif i > x + d1 + d2:
            population[2] += sum(board[i][:y + d2 - d1])
            population[3] += sum(board[i][y + d2 - d1:])
            # print(4, population)
        # else:
        #     print(i)
    # print(max(population) - min(population))
    return max(population) - min(population)


def d1_g_than_d2(x, y, d1, d2):
    population = [0 for _ in range(5)]
    for i in range(N):
        # print(i)
        if i < x:
            population[0] += sum(board[i][:y + 1])
            population[1] += sum(board[i][y + 1:])
            # print(0, population)
        elif x <= i <= x + d2:
            population[0] += sum(board[i][:y - (i - x)])
            population[4] += sum(board[i][y - (i - x):y + (i - x) + 1])
            population[1] += sum(board[i][y + (i - x) + 1:])
            # print(1, population)
        elif x + d2 < i < x + d1:
            population[0] += sum(board[i][:y - (i - x)])
            population[4] += sum(board[i][y - (i - x):y + d2 - (i - x - d2) + 1])
            population[3] += sum(board[i][y + d2 - (i - x - d2) + 1:])
            # print(y-(i-x), y+d2-(i-x-d1))
            # print(3, population)
        elif x + d1 <= i <= x + d1 + d2:
            population[2] += sum(board[i][:y - d1 + (i - x - d1)])
            population[4] += sum(board[i][y - d1 + (i - x - d1):y + d2 - (i - x - d2) + 1])
            population[3] += sum(board[i][y + d2 - (i - x - d2) + 1:])
            # print(4, population)
        elif i > x + d1 + d2:
            population[2] += sum(board[i][:y + d2 - d1])
            population[3] += sum(board[i][y + d2 - d1:])
            # print(5, population)
        # else:
        #     print(i)
    # print(max(population) - min(population))
    return max(population) - min(population)


def d1_l_than_d2(x, y, d1, d2):
    population = [0 for _ in range(5)]
    for i in range(N):
        # print(i)
        if i < x:
            population[0] += sum(board[i][:y + 1])
            population[1] += sum(board[i][y + 1:])
            # print(0, population)
        elif x <= i < x + d1:
            population[0] += sum(board[i][:y - (i - x)])
            population[4] += sum(board[i][y - (i - x):y + (i - x) + 1])
            population[1] += sum(board[i][y + (i - x) + 1:])
            # print(1, population)
        elif x + d1 <= i <= x + d2:
            population[2] += sum(board[i][:y - d1 + (i - x - d1)])
            population[4] += sum(board[i][y - d1 + (i - x - d1):y + (i - x) + 1])
            population[1] += sum(board[i][y + (i - x) + 1:])
            # print(y-d1+(i-x), y+d2-(i-x))
            # print(2, population)
        elif x + d2 < i <= x + d1 + d2:
            population[2] += sum(board[i][:y - d1 + (i - x - d1)])
            population[4] += sum(board[i][y - d1 + (i - x - d1):y + d2 - (i - x - d2) + 1])
            population[3] += sum(board[i][y + d2 - (i - x - d2) + 1:])
            # print(4, population)
        elif i > x + d1 + d2:
            population[2] += sum(board[i][:y + d2 - d1])
            population[3] += sum(board[i][y + d2 - d1:])
            # print(5, population)
        # else:
        #     print(i)
    # print(max(population) - min(population))
    return max(population) - min(population)

answer = 1e9
for x in range(0, N-2):
    for y in range(1, N-1):
        for d1 in range(1, N-1):
            for d2 in range(1, N-1):
                if 0 <= x < x+d1+d2 and x+d1+d2 < N and 0 <= y-d1 < y and y < y+d2 < N:
                    if d1 == d2:
                        population_difference = d1_e_d2(x, y, d1, d2)
                    elif d1 > d2:
                        population_difference = d1_g_than_d2(x, y, d1, d2)
                    else:
                        population_difference = d1_l_than_d2(x, y, d1, d2)
                    answer = min(population_difference, answer)
                    # print(x, y, d1, d2, population_difference)

print(answer)

# d1_e_d2(2, 2, 1, 1)
# d1_g_than_d2(2, 4, 2, 1)
