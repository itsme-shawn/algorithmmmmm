- 📅 Date: 2020-12-14 (토)

# 1920. 수 찾기
출처: https://www.acmicpc.net/problem/1920

## 📝 Problem

**문제**

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

**입력**

첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

**출력**

M개의 줄에 답을 출력한다. 
존재하면 1을, 존재하지 않으면 0을 출력한다.


## Input/Output example

### Input
```
5  
4 1 5 2 3  
5  
1 3 7 9 5
```

### Output
```
1  
1  
0  
0  
1
```

## 💡 Submit
### Solved code
(Important part only)
``` python
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target) :
  start = 0
  end = len(arr)-1

  while start <= end :
    mid = int(( start + end ) / 2)
    if arr[mid] < target :
      start = mid + 1
    elif arr[mid] > target :
      end = mid - 1
    else : 
      return 1
  return 0

A.sort()

for i in range(0,M):
  print(binary_search(A, check[i]))

# 삽입정렬 쓰면 매우느려짐, sort() 내장함수사용

```

### Solution
- 이진탐색을 사용하기 위해, sort() 로 정렬시킨 다음 `binary_search` 함수를 실행한다.

### Commentary
- 맨 처음에 삽입정렬을 직접 구현해서 제출했는데 시간초과가 떴다. 당연히 시간복잡도가 O(n^2) 이기 때문에 시간초과가 뜬다. 정렬이 필요할때는 merge sort 를 사용하거나 `sort()` 내장함수를 사용하자. sort() 함수의 시간복잡도는 O(n*log n) 이라고 한다.  

- 입력을 받을 때, `input()` 대신 sys 모듈의 `sys.stdin.readline()` 을 사용하자. (시간복잡도 감소)

### References
- [파이썬 내장함수 시간복잡도 정리](https://m.blog.naver.com/PostView.nhn?blogId=complusblog&logNo=221204308911&proxyReferer=https:%2F%2Fwww.google.com%2F)
- [1920 수찾기 파이썬 풀이](https://alpyrithm.tistory.com/2)