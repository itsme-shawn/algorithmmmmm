📅 Date: 2020-12-25 (금)

# 재귀 (Recursive)

## 🔎 개념

간단히 정의하면 함수에서 자기 자신을 다시 호출하여 작업을 수행하는 방식이다.  

실제 알고리즘에서 재귀를 활용하는 방식으로는  **어떤 문제를 해결하기 위해 동일한 문제의 조금 더 작은 경우를 해결**함으로써 그 문제를 해결하는 방식이다.

<p align='center'><img src="https://miro.medium.com/max/458/1*-Y1eGambklKEHDVrPiLHPQ.jpeg" width='50%'/></p>

이해를 돕기위해, 위에 보이는 사진 속 직사각형의 문 하나를 함수, 문을 여는 것을 함수 실행, 문을 닫는 것을 함수 종료라고 가정해보자. 재귀를 사용하면 하나의 문 속에 또 다른 문을 계속해서 여는 것이다.  
 **이때 이전 함수는 종료되지 않고 계속 실행중이다.**  
 그렇게 계속 문을 열다보면 마지막 문이라는 신호(원하는 값을 찾게 됨)를 받게 되고, 그때부터는 이제 가장 마지막에 연 문부터 차레대로 닫고 나오면 된다.  

 방금 비유한 설명을 팩토리얼 재귀구현의 실제 콜스택으로 보면 아래와 같다.
 <p align='center'><img src="https://i.stack.imgur.com/PK6Ht.png" width='60%'/></p>

<br>

 ## 재귀 구현 시 주의사항

1. **탈출 조건(base case)을 걸어서 재귀호출을 끝내야 한다는 것**
2. **재귀 함수에 들어가는 파라미터 값이 계속해서 변해야 한다는 것**

1번의 탈출 조건이 없으면 함수가 무한 루프를 돌게 되고, 마찬가지로 2번에서 파라미터 값이 계속 동일하다면 이 역시 함수가 무한 루프를 돌게 될 것이다.  

재귀함수를 구현 할 때, 이 2가지 조건은 항상 충족되어야 한다.

<br>

## 재귀 vs 반복문


<br>

## 📝 재귀호출을 이용한 팩토리얼 예제

### Code

```python
def factorial(n):
  if(n == 0):   # base case ( n == 0 )
    return 1
  else:         # recursive case ( n > 0 )
    return n * factorial(n-1) 

print(factorial(4))
```

> factorial 함수에서 이전 스택의 리턴 값을 계속 사용하기 때문에 이런 경우는 return 문을 반드시 사용해줘야 한다. return 없으면 에러

 <p align='center'><img src="./imgs/fact.JPG" width='70%'/></p>



## References
- [[개념 이해] 재귀 함수 recursion](https://medium.com/@yejinh/%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4-%EC%9E%AC%EA%B7%80-%ED%95%A8%EC%88%98-recursion-7676d1ed4d6f)