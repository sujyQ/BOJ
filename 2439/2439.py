import sys

n = int(sys.stdin.readline())

for i in range(n) :
    line = ""
    for j in range(n-i-1) :
        line += " "
    for j in range(i+1) :
        line += "*"
    print(line)