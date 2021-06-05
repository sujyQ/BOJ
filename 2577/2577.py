import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul = A*B*C
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while mul/10 != 0 :
    reminder = mul%10
    arr[reminder] = arr[reminder] + 1
    mul = int(mul/10)

for i in range(10) :
    print(arr[i])