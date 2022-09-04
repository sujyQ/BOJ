N = int(input())
A = set(map(int, input().split(" ")))
M = int(input())
targets = list(map(int, input().split()))

# counts = [0 for _ in range(0, max(A))]

for target in targets :
    if target in A :
        print('1')
    else : print('0')