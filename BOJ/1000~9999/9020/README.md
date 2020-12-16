📅 Date: 2020-12-15 (화)

# 9020. 골드바흐의 추측
출처: https://www.acmicpc.net/problem/9020

## 📝 Problem

### 문제
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

### 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다. (4 ≤ n ≤ 10,000)

### 출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

## Input/Output example
### Input

```
3
8
10
16
```

### Output
```
3 5
5 5
5 11
```

# ✅ Submit
## 👌 Solved Code 1

### 💡 Idea

테스트케이스를 2로 나눈 다음, 해당 값와 나머지 값(=전체 - 해당 값) 에 대해 모두 그때그때마다 소수검사(`isPrime()`)를 한다.  
둘 중에 하나라도 소수가 아니면 해당 값을 1씩 줄여가며 반복한다.

### 💻 Code
(Important part only)
``` python
import sys
import math

T = int(input())
arr = list()
for _ in range(T):
  arr.append(int(input()))

# return 값 False : 소수가 아님 / True : 소수
def isPrime(num):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0 : return False 
  return True 

for i in range(T):
  check = int(arr[i] / 2)
  while check >= 2 :
    if isPrime(check) and isPrime(arr[i]-check):
      print(check,arr[i]-check)
      break
    else: 
      check -= 1

```

### ✍ Solution
Idea 에 적은 설명으로 충분

### 💬 Commentary
- 특정 수가 소수인지 검사할 때 특정 수의 제곱근(sqrt)까지만 검사해보면 된다. (제곱근 함수(`math.sqrt()`) math 모듈 사용)
- int 로 형 변환 안시켜줘서 처음에 에러났음.
- 특정 수가 소수인지 그때그때마다 함수를 호출해서 검사하기 때문에 시간복잡도가 다소 높음. => Solved Code 2 방식 (에라토스테네스의 체 아이디어) 로 개선

<br>

## 👌 Solved Code 2

### 💡 Idea
전체적인 로직은 Solved Code 1 과 동일한데, 소수 판정 방식만 에라토스테네스의 체로 전체 소수 리스트를 만든 다음에 리스트에서 소수 여부 확인하는 방식으로 변경

### 💻 Code
(Important part only)

``` python
# 에라토스테네스의 체 방법 사용

import sys
import math

T = int(input())
arr = list()
for _ in range(T):
  arr.append(int(input()))

MAX = int(max(arr))

# 소수 리스트 초기화
primeList = [False, False] + [True] * (MAX- 1)

for i in range(2, int(math.sqrt(len(primeList)))+1 ):
  if (primeList[i] == True):
    for j in range(i*2, len(primeList) , i):
      primeList[j] = False

for i in range(T):
  check = int(arr[i] / 2)
  while check >= 2 :
    if primeList[check] and primeList[arr[i]-check]:
      print(check,arr[i]-check)
      break
    else: 
      check -= 1
```

### ✍ Solution
- 테스트케이스 input 값을 배열로 받은 다음에, 그 중에 가장 큰 값을 MAX 에 할당함 -> primeList 를 최대한 효율적으로 만들기 위함.
- 에라토스테네스의 체 아이디어를 사용하여 소수 리스트(primeList)를 생성함.

### 💬 Commentary
- Solve Code 1 방식보단 시간복잡도가 확실히 줄어들었다.

## References
- [소수찾기 - 에라토스테네스의 체](https://leedakyeong.tistory.com/entry/python-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4)
- [2. 소수 구하기 - 에라토스테네스의 체](https://wikidocs.net/21638)
- [소수판정](http://www.ktword.co.kr/abbr_view.php?m_temp1=6177)