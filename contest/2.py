import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

direction = 1
flag = True
chk = True
for i in range(N-1) :
    
    if A[i] == A[i+1] :
        flag = False
        break

    if A[i] < A[i+1] :
        if direction == -1 :
            flag = False
            break

    if A[i] > A[i+1] :
        if direction == 1 :
            if chk :
                direction = -1
                chk = False
            else :
                flag = False
                break
        

print("YES" if flag else "NO")