📅 Date: 2021-02-01 (월)

# Dynamic Programming (동적 계획법)

## 🔎 개념

Dynamic Programming (DP) 를 한 줄로 요약하자면 `한 번 푼 문제의 결과값을 재활용해서 하나의 문제는 딱 한 번만 풀도록 하는 알고리즘 패러다임` 이다.  

---

### DP 로 문제를 해결하기 위한 조건

### 1️⃣ 최적 부분 구조 (Optimal Substructure) 
큰 문제를 작은 부분 문제로 나눠서 풀 수 있다.

<p align='center'><img src="./imgs/dp1.PNG" width='50%'/></p>

<br>

### 2️⃣ 중복되는 부분 문제 (Overlapping Subproblem)  
큰 문제를 부분 문제로 쪼갤 때, 동일한 부분 문제가 겹치는 경우가 있다.

<p align='center'><img src="./imgs/dp2.PNG" width='80%'/></p>

위 그림에서 같은 색으로 칠해진 `fib(n)` 처럼 부분 문제들이 중복된다.

<br>

**최적 부분 구조**와 **중복되는 부분 문제** 조건을 모두 충족하는 문제일 때, DP 를 이용하면 문제를 효과적으로 해결할 수 있다.

---

### DP 구현 방식

DP 의 구현 방식은 2가지가 있다.

### **1️⃣ Memoization (Top-down)** : 재귀 이용
   
DP에서 각 문제는 딱 한 번만 푼다고 했다. Memoization 은 **재귀**를 이용해서 부분문제를 푼 다음, **결과값을 저장시킨다.** 그 후 기존에 푼 부분문제가 중복해서 등장하면 풀지 않고 **저장된 Memo 값을 이용해서 단순히 리턴시킨다.**  
 아래의 피보나치 수 예시를 보자.

<br>

<p align='center'><img src="./imgs/dp3.PNG" width='80%'/></p>

Tob-down 인 것을 확인할 수 있고, 위의 그림에서 블러처리 된 fib(2), fib(3), fib(4) 는 이미 푼 부분문제들이기 때문에 cache(Memo) 에서 해당 값을 꺼내쓰기만 하면 된다.

<br>

### **2️⃣ Tabulation (Bottom-up)** : 반복문 이용

Tabulation 은 표(table)을 뜻한다. 말 그대로 표를 그린다고 생각하면 된다. **Memoization 과 다르게 반복문을 사용한다.** 작은 부분문제들 순서대로(Bottom-up) 결과값을 표에다가 채워나가면 된다.  

<br>

<p align='center'><img src="./imgs/dp4.PNG" width='80%'/></p>

> Tabulation 방식은 Memoization 과 다르게 공간(메모리)을 최적화시킬 수 있다. 구체적 예시는 맨 아래 예제 코드에 있다.

<br>

---

## 📝 예제

피보나치 수를 구하는 알고리즘을 **Memoization** 과 **Tabulation** 두 가지 방식으로 살펴보자.



## 👌 Memoization (Tob-down) 방식

재귀를 이용한다.  
재귀를 이용하기 때문에 base case 설정이 중요하다.

### 💻 Code

``` python
# DP 의 memoization 방식(top-down) 이용 -> 재귀 기반

def fib_memo(n, cache):
    # base case
    if (n == 1 or n == 2):
        cache[n] = 1
    
    # 아직 n번째 피보나치 수를 계산 안했으면 -> 재귀로 계산 후 cache 에 저장
    if (n not in cache):
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)

    # 이미 n번째 피보나치 수를 계산한 경우 -> cache 에 있는 값을 리턴
    # if ( n in cache ):
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 캐시
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
```
  
<br>

## 👌 Tabulation (Bottom-up) 방식

Memoization 과는 다르게 Tabulation 은 반복문을 사용한다.

### 💻 Code

``` python
# DP 의 tabulation 방식(bottom-up) 이용 -> 반복문 기반

def fib_tab(n):
    table = {}

    for i in range(1, n+1):
        if( i == 1 or i == 2):
            table[i] = 1
        else:
            table[i] = table[i-1] + table[i-2]
    
    return table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

```


### 💬 Commentary
- 위에서는 딕셔너리를 썼지만, 사실 딕셔너리보다 리스트를 사용하는 것이 메모리적으로 더 나음.  
딕셔너리는 key, value 를 저장해야하기 때문임.

- 리스트와 딕셔너리 비교

  - 리스트 - 리스트 끝에 데이터를 append하는것이 빠르고 인덱스로 데이터 접근도 빠르다.
딕셔너리에 비해 메모리를 덜 차지한다.

  - 딕셔너리 - 탐색 (lookup)이 빠르다. (ex. 리스트에서 'Alice'가 있는지 확인하는것은 O(n) 이지만 딕셔너리에서 'Alice'가 있는지 확인하는것은 O(1)이다.)

<br>

## 👌 Tabulation (Bottom-up) 방식에서의 공간최적화

Tabulation 방식은 공간(메모리)를 최적화할 수 있다.  
기존의 방식에서 `fib(n)` 을 구할 때, 리스트(table)의 크기는 n이 되므로 공간복잡도는 O(n) 이다.  
하지만, `fib(n)` 을 구할 때 다른 table 의 값은 필요없고, `fib(n-1)` 과 `fib(n-2)` 만 있으면 된다.  
즉,  `current` 와 `previous` 변수만을 사용하게 되면 공간복잡도가 O(1) 로 줄어들게 된다.


### 💻 Code

``` python
# 기존 tabulation 방식에서 공간(메모리)을 최적화한 방식

def fib_optimized(n):
    cur = 1
    prev = 0

    for i in range(1, n):
        cur, prev = cur + prev, cur
        
    return cur

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
```

### 💬 Commentary
- python 에서의 변수 swap 시 내부과정 : 

  `a, b = b, a` 의 내부로직은 다음과 같다.

  ```python
  # a, b = b, a

  tmp = (b, a)
  a, b = tmp
  ```

  `tmp` 에 `(b, a)` 튜플을 생성하고 `(a, b)` 튜플에 `tmp` 값을 넣으면 swap 이 이뤄지게 된다.

---