📅 Date: 2021-06-03 (목)

# Greedy Algorithm (탐욕 알고리즘)

## 🔎 개념

그리디 알고리즘은 먼 미래를 생각하지 않고, 각 단계에서의 최선의 방법만을 선택하는 알고리즘이다. 빠르게 해답을 얻어낼 수는 있지만 항상 최적의 해가 보장되지는 않는다.  
그리디 알고리즘으로 최적의 해를 얻어내려면 매 순간의 선택이 최적의 선택이라는 보장이 있어야 한다. 이를 위해서는 두 가지 조건이 성립해야한다.

1. 최적 부분 구조(Optimal Substructure)
2. 탐욕 선택 속성(Greedy Choice Property)

### 1️⃣ 최적 부분 구조(Optimal Substructure)

DP 와 마찬가지로 그리디도 최적 부분 구조를 만족해야한다.
최적 부분 구조는 부분 문제(작은 문제)들의 최적의 답을 이용해서 큰 문제의 최적의 답을 구할 수 있다는 것이다.  
대표적인 예제로 피보나치 수열이 있다.
fib(5)의 값은 fib(4)+fib(3) 으로 표현할 수 있고, 다시 fib(4) 는 fib(3)+fib(2) 로 나타낼 수 있다.

### 2️⃣ 탐욕 선택 속성(Greedy Choice Property)

각 단계에서의 탐욕스러운 선택이 최종 답을 구하기 위한 최적의 선택이여야 한다.  
즉, 탐욕적 선택을 하더라도 최종 결과에 손해가 없어야 한다.

## 📝 예제

### 문제

돈을 거슬러줄 때 필요한 최소한의 동전 개수를 리턴하는 함수 min_coin_count 를 구현해보자.
예를 들어, 1440원을 거슬러 주기 위해서는 500원 2개, 100원 4개, 10원 4개, 총 10을 리턴하면 된다.

## 👌 풀이

### 💡 Idea

우선, 그리디알고리즘으로 풀 때 최적의 해가 보장되는지부터 확인해야한다.

**1️⃣ 최적 부분 구조(Optimal Substructure)**  
1440원을 거슬러 줄때, 500원을 먼저 거슬러 줬다고 치면 940원이 남는다.
이제 동전을 최대한 적게 사용해서 940원을 거슬러주는 부분문제를 풀면 된다.
만약 100원을 먼저 거슬러 줬다고 치면, 1340원을 거슬러주는 부분문제를 풀면 되는 것이다. 이러한 부분 문제들에 대한 최적의 답을 구하고 합쳐서 최종답을 비교하면 최적의 답을 구할 수 있다.  
이 문제에는 최적 부분 구조가 존재한다.

**2️⃣ 탐욕 선택 속성(Greedy Choice Property)**
500원 1개는 100원 5개와 같다. 즉, 개수를 최대한으로 줄일려면 큰 단위 동전을 주는게 유리하다. 때문에 매 순간마다 가능한 큰 동전을 선택하는 것이 가장 좋은 선택이다. (탐욕적 선택 속성 만족)

### 💻 Code

(Important part only)

```python
# 거스름돈을 최소한의 동전 갯수로 거슬러주기
# min_coin_count(value, coin_list) : 거슬러 주기 위해 필요한 최소 동전 개수 리턴
# default_coin_list : 동전 종류


def min_coin_count(value, coin_list):
    coin_list.sort(reverse=True)  # [500, 100, 50, 10]
    count = 0
    for coin in coin_list:
        count += value // coin
        value = value % coin
    return count


default_coin_list = [100, 500, 10, 50]

print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
```

### 💬 Commentary

- 만약 거슬러줄 수 있는 동전의 종류가 100원, 70원, 30원, 10원 이라고 치면 최적 부분 구조는 여전히 만족하겠지만, 탐욕적 선택 속성을 충족하지 않게 된다.  
  140원을 거슬러 줄때, 100+30+10 보다 70+70 조합이 더 최적의 해가 된다.
