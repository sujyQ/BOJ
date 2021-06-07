N = 10000
cnt = [0 for i in range(N)]

def d(n) :
    sum = n
    while int(n/10) > 0 :
        sum += n%10
        n = int(n/10)
    sum += n
    return sum

for i in range(N) :
    _d = d(i+1)
    if _d <= N :
        cnt[_d-1] += 1

for i in range(N) :
    if cnt[i] < 1 :
        print(i+1)