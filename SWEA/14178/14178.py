T = int(input())

quest = []
for _ in range(T):
    quest.append(list(map(int, input().split())))

for i, (N, D) in enumerate(quest):
    # print(-1 * (-N // (2 * D + 1)))
    print('#{} {}'.format(i+1,  -1 * (-N // (2 * D + 1))),)
