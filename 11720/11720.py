import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline()[:-1]
sum = 0
for i in range(N) :
    sum += int(string[i])
print(sum)