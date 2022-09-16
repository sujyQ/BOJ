N = int(input())
A = list(map(int, input().split()))

visited = [False] * N

answer = -1e9


def DFS(depth, arr):
    global answer
    if False not in visited:
        s = 0
        for i in range(1, N):
            s += abs(arr[i]-arr[i-1])
        answer = max(s, answer)

    else:
        for i in range(0, N):
            if not visited[i]:
                visited[i] = True
                DFS(depth+1, arr+[A[i]])
                visited[i] = False


DFS(0, [])
print(answer)
