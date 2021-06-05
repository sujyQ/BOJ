import sys

N = int(sys.stdin.readline())

for i in range(N) :
    result = [char for char in sys.stdin.readline().strip()]
    _s = 0
    for j in range(len(result)) :
        k = 0
        while(j-k >= 0) :
            if result[j-k] == 'O' :
                _s = _s + 1
                k = k+1
            else : break
    print(_s)