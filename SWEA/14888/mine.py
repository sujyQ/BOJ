N = int(input())        # number of nums
targets = list(map(int, input().split()))
num_operator = list(map(int, input().split()))

operator = []
for idx, op in enumerate(num_operator):
    operator += [idx]*op


def permutations(ops, depth, made, max, min):
    # print(ops, depth, made)
    if depth >= len(ops):
        # print(made)
        if made < min:
            min = made
        if made > max:
            max = made
        return max, min

    for i in range(depth, len(ops)):
        ops[depth], ops[i] = ops[i], ops[depth]
        if ops[depth] == 0:
            next = made + targets[depth+1]
        elif ops[depth] == 1:
            next = made - targets[depth+1]
        elif ops[depth] == 2:
            next = made * targets[depth+1]
        elif ops[depth] == 3:
            if made < 0:
                made *= -1
                next = made // targets[depth+1]
                next *= -1
                made *= -1
            else:
                next = made // targets[depth+1]
        max, min = permutations(ops, depth+1, next, max, min)
        ops[depth], ops[i] = ops[i], ops[depth]

    return max, min

res = permutations(operator, 0, targets[0], -1000000000, 1000000000)
print(res[0])
print(res[1])

