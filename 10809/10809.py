import sys
input = sys.stdin.readline()[:-1]

answer = ""

for i in range(ord('a'), ord('z')+1) :
    flag = -1
    for j in range(len(input)) :
        if chr(i) == input[j] :
            flag = j
            break
    answer += str(flag) + " "

print(answer)

        
