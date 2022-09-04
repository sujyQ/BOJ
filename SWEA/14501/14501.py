N = int(input())
table = []
for _ in range(N):
    t, p = map(int, input().split())
    table.append([t, p])

visited = [False for _ in range(N)]
# for i in range(N):
#     if table[i][0] + i >= N:
#         visited[i] = True
# print(visited)
answer = -1

def dfs(index, pay):
    global answer
    if index >= N:
        answer = max(answer, pay)

    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            if table[i][0] + i > N:
                dfs(i+table[i][0], pay)
            else:
                dfs(i + table[i][0], pay + table[i][1])
            visited[i] = False


dfs(0, 0)
print(answer)
