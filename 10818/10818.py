import sys

N = int(sys.stdin.readline())
datas = list(map(int, sys.stdin.readline().split()))
print(min(datas), max(datas))