N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

visited = [False] * N

answer = 0

def DFS(depth, idx, made):
    global answer
    if sum(made) == S and depth > 0:
        # print(made)
        answer += 1

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(depth+1, i+1, made+[arr[i]])
            visited[i] = False


DFS(0, 0, [])
print(answer)
