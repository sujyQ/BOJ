import sys

n, x = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()

answer = ""
for i in range(n) :
    if int(a[i]) < x :
        answer += a[i]
        if i != n-1 :
            answer += " "

print(answer)