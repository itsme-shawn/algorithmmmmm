📅 Date: 2020-12-16 (수)

# 10815. 숫자 카드
출처: https://www.acmicpc.net/problem/10815

## 📝 Problem

### 문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다


### 출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

## Input/Output example
### Input

```
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
```

### Output
```
1 0 0 1 1 0 0 1
```

# ✅ Submit
## 👌 Solved Code 1

### 💡 Idea
[BOJ 1920 수 찾기](/BOJ/1000~9999/1920) 랑 거의 동일한 문제로, 정렬 후 이진탐색을 하면 끝난다.  
이번에는 이진탐색을 재귀로 구현했다.


### 💻 Code
(Important part only)
``` python
import sys
# sys.setrecursionlimit(1500) 재귀횟수 설정

N = int(input())
own = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))

own.sort()

# 이진탐색 재귀
def binary_search(arr, target, start=0, end=None):
  if end==None :
    end = len(arr) - 1

  mid = (start + end ) // 2
  while (start <= end) :
    if (arr[mid] < target):
      return binary_search(arr, target, mid+1, end) 
    elif (arr[mid] > target):
      return binary_search(arr, target, start, mid-1)
    else: # find
      return 1
  return 0

for i in range(len(check)):
  print(binary_search(own, check[i]), end=' ')

```

### ✍ Solution
X

### 💬 Commentary
- 함수 선언 시, 파라미터에 값을 할당하면 함수를 호출할 때 함수 인자가 생략되더라도 기본값을 지정할 수 있다.
- `def binary_search(...,end=None)` 아이디어 괜찮았음
- 재귀함수와 함수호출스택 개념 다시 한번 이해하기
```C
int sum(int n) 
{
	// 탈출 조건
	if (1 == n) {
		return 1;
	
	// 자신보다 1만큼 작은 숫자를 분신을 만들어서 계산을 시킨다.
	// 분신이 계산을 마치면 자신의 현재 값을 거기에 더한다.
	} else {
		return sum(n-1) + n;
	}
}
```
![재귀이해](./recursive.png)

## References
[함수 호출의 원리 및 재귀호출](http://10bun.tv/beginner/episode-4/#%ED%95%B5%EC%8B%AC-%EA%B0%95%EC%9D%98)