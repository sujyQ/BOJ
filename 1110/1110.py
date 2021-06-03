import sys

cycle = 0
target = int(sys.stdin.readline())
if target < 10 :
        target = target * 10
_target = target

while True :
    ten = int(_target/10)
    one = int(_target%10)
    sum = ten + one
    _target = one*10 + int(sum%10)
    
    cycle += 1
    if _target == target :
        break

print(cycle)

