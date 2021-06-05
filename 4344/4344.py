import sys

C = int(sys.stdin.readline())

for i in range(C) :
    line = list(map(int, sys.stdin.readline().split()))
    _C = line.pop(0)
    mean = sum(line)/_C
    count = [1 for score in line if score > mean ]
    print('{:.3f}%'.format(sum(count)/_C*100))