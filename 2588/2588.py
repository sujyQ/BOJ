import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

print(a*(b%10))
print(int((a*(b%100-b%10))/10))
print(a*int(b/100))
print(a*b)