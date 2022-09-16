N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for n in range(N):
    if A[n] >= B:
        answer += (A[n] - B) // C + 1
        if (A[n] - B) % C != 0:
            answer += 1
    else:
        answer += 1

print(answer)
