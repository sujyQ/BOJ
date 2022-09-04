# https://www.acmicpc.net/problem/6603

target_list = []
while True:
    target = list(map(int, input().split()))
    if target[0] == 0:
        break
    else:
        target_list.append(target)

for _i, target in enumerate(target_list):
    K, S = target[0], target[1:]
    visited = [False] * K


    def DFS(depth, idx, res):
        # print(depth, visited, idx, res)
        if depth >= 6:
            print(res[:-1])

        else:
            for i in range(idx, K):
                if not visited[i]:
                    visited[i] = True
                    DFS(depth+1, i+1, res+str(S[i])+" ")
                    visited[i] = False

    DFS(0, 0, "")

    if _i != len(target_list)-1 :
        print()
