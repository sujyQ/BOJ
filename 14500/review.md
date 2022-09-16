# BOJ 14500 테트로미노
## 테트로미노 [#14500](https://www.acmicpc.net/problem/14500)
+ 폴리오미노 : 1x1 크기의 정사각형을 여러개 이어서 붙인 도형
+ 테트로미노 : 정사각형 4개를 이어 붙인 폴리오미노
+ NxM 크기의 종이 위에 테트로미노 하나를 놓아, 테트로미노가 놓인 칸에 쓰여 있는 수들의 합의 최댓값을 구한다.

+ 입력 : 크기 `N`, `M`, NxM 크기의 `board`
+ 출력 : 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값


## 나의 풀이
+ 무언가의 최댓값/최솟값은 DFS를 떠오르게 한다.
+ 그래서 DFS로 구현했다.
+ `dfs()`를 재귀로 부르면서, `depth`가 4일 때 멈추고 `score`를 비교한다.
+ 그런데 단순히 재귀로만 구현하면, ㅗ 모양의 테트로미노는 찾을 수 없다.
  + 그래서 DFS로는 ㅗ모양을 제외한 다른 테트로미노들에 대해 탐색하고
  + ㅗ 모양은 만들 수 있는 모양 (ㅗ, ㅏ, ㅓ, ㅜ)을 정의하고, 픽셀별로 갖다대면서 합을 구했다.
+ `Python3`으로는 죽어도 시간초과가 뜬다. `pypy`로 제출하면 너무 스무스하게 통과한다.

## 멋진 풀이 1
+ ㅗ 모양도 DFS로 찾을 수 있다!
+ idx가 1인 경우, 즉 첫번째 재귀 = 2번째 함수 호출인 경우
  + 다음 자리에서 이동하지 않고 현재 위치에서 다시 dfs 함수를 호줄한다면
  + ㅗ 모양도 탐색 가능하다.
+ 뿐만 아니라, 가지치기도 가능하다.
  + 현재 `score`를 보고 최댒값이 될 수 있는 조합인지 확인하는 방법이다.
  + 만약 최댓값이 될 수 없는 싹이면 도려낸다 = 멈춘다
    ~~~
    def dfs(r, c, idx, total):
        global ans
        if ans >= total + max_val * (3 - idx):
            return
    ~~~
    + dfs 함수 내에서, `total`이 내 코드의 `score`과 같은 변수다.
    + 현재 스코어에다가 앞으로 `board`에 적힌 값 중 제일 큰 값만 더해진다면
    + `answer`이 갱신될 가능성이 존재한다.
    + 만약 아니라면 남은 횟수동안 최댓값만 더한다고 하더라도 합의 최댓값이 될 수 없다.

## 배운 점
~~~
def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
~~~
~~~
for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0
~~~