import sys

N = int(sys.stdin.readline())
cnt = 0


def is_sequence(n) :
    d = int((n%100)/10) - n%10
    while True :
        if int(n/100) > 0 :
            n = int(n/10)
            _d = int((n%100)/10) - n%10
            if d != _d :
                return False
        else : 
            break
    return True

for i in range(N) :
    if is_sequence(i+1) :
        cnt +=1

print(cnt)