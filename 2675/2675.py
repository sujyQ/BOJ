import sys

N = int(sys.stdin.readline())

for i in range(N) :
    answer = ""
    repeat, input = sys.stdin.readline().split()
    repeat = int(repeat)

    for _, ch in enumerate(input) :
        answer += ch*repeat
    print(answer)