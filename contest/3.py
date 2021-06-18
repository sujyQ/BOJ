import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline()[:-1]

if len(S) <= 25 :
    print(S)
else :
    if S[11:-11].__contains__('.') :
        if S[11:-11].count('.') == 1 and S[-12] == '.' :
            print(S[0:11]+"..."+S[-11:])
        else :
            print(S[0:9]+"......"+S[-10:])
    else :
        print(S[0:11]+"..."+S[-11:])