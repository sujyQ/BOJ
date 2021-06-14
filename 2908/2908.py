import sys

A, B = map(int, sys.stdin.readline()[::-1].split())

print(A if A > B else B)