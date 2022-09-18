# 14888. 연산자 끼워넣기
* 입력 : 수의 개수 `N`, 수 `A`, 연산자의 개수 `K`
* 출력 : 만들 수 있는 식의 결과의 최댓값과 최솟값


* 수와 수 사이에 연산자를 하나씩 넣어 수식을 만든다.
* 주어진 수의 순서를 바꾸면 안된다.
* 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행한다.
* 나눗셈은 정수 나눗셈으로 몫만 취하며, 음수를 양수로 나눌 때 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼 것과 같다.
* Ex. `A : [1,2,3,4,5,6]`, 덧셈 2개, 곱셈 1개, 나눗셈 1개인 경우
  - 총 60가지의 식을 만들 수 있는데,
  - 그 중 일부는 `1+2+3-4*5//6`, `1//2+3+4-5*6`이다.


## 나의 코드
+ 순열을 이용해서 가능한 연산자 조합을 구하면서 DFS
+ `ops[depth], ops[i] = ops[i], ops[depth]` :
  - swap으로 순서와 상관있는 조합들을 구한다.
  - recursion 후 `ops[depth], ops[i] = ops[i], ops[depth]`으로 다시 돌려놓는다.
+ 초기 최솟값을 `1e9`, 초기 최댓값을 `-1e9`로 설정한다.
  - recursion 중 업데이트가 될 수 있도록 한다.
  - 연산 결과는 항상 -10억보다 크고 10억 이하이다.
* 백준 기준 `7264ms`가 소요됐다.


## 멋진 코드 #1
* 순열을 이용하지 않는다.
* DFS를 이용한다.
* 최댓값, 최솟값을 정한 후 업데이트하는 방식은 동일하다.
* 다른 점은, 순열의 조합을 swap으로 구해가며 하지 않는다는 점이다.
  - 각 연산자 개수를 의미하는 `add, sub, mul, div` 변수를 사용한다.
  - 내 코드에서 swap - recursion - swap 구조는 동일하지만,
  - 변수값을 1 줄인 후 다시 복원한다.
* `add, sub, mul, div, min, max`을 `global`로 선언한다.
* 백준 기준 `104ms`가 소요됐다..!


## 배운 점
~~~
백트래킹이라고 해서 꼭 permutation을 구하지 않아도 된다.
~~~
~~~
아래의 흐름으로 순열을 구할 수 있다.
// SWAP
// DFS
// SWAP
~~~