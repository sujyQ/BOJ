N, M = list(map(int, input().split()))
arr = [i+1 for i in range(0, N)]
visited = [False] * N

def DFS(depth, made) :
    if depth == M:
        for el in made:
            print(el, end=' ')
        print()

    else:
        for i in range(0, N):
            if not visited[i]:
                visited[i] = True
                DFS(depth+1, made+[arr[i]])
                visited[i] = False


DFS(0, [])

