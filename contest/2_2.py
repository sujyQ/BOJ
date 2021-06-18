import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

i = max(range(N), key=A.__getitem__)
A_left, A_right = A[:i], A[i:]

if all(i < j for i, j in zip(A_left, A_left[1:])) and all(i<j for i, j in zip(A_right, A_right[1:])) :
    print("YES")
else :
    print("NO")