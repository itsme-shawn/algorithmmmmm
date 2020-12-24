# 알고리즘 복잡도 (Algorithm Complexity)

## 1. 알고리즘의 평가

알고리즘을 평가하는데 있어서 **수행시간**과 **메모리 사용량**을 척도로 평가한다.  
  
수행시간에 해당하는 것이 시간 복잡도 (Time Complexity)  
메모리 사용량에 해당하는 것이 공간 복잡도 (Space Complexity) 이다.

둘다 중요하지만 더 중요한 것을 고르자면 시간복잡도가 더 중요하다.  
메모리는 기술 발전에 따라 늘릴 수 있지만, 시간은 돈으로도 살 수가 없다.  

최소한의 자원(시간, 공간)을 이용해 문제를 해결하는 알고리즘이 좋은 알고리즘이다.  

> 알고리즘은 일반적인 데스크탑 어플리케이션이나, 시간이 중요한 서비스( 지도 길찾기 서비스, 실시간 스트리밍 서비스 ..) 등에만 중요한 것이 아니라 Web 에도 중요하다. 브라우저가 사용할 수 있는 메모리는 일반적인 데스크탑 어플리케이션 보다 작은데, 이유는 웹 페이지에서 실행되는 자바스크립트가 시스템 메모리를 전부 사용해서 OS가 다운되는 것을 막기 위함이다. 즉, Web에서도 좋은 알고리즘을 사용해야 페이지의 성능을 올릴 수 있다.

## 시간복잡도 (Time Complexity)

시간복잡도란 알고리즘이 문제를 해결하기 위한 **시간(연산)의 횟수** 를 말한다.
시간복잡도를 측정할 때 시간을 직접 측정하기 보다는 **input 에 따른 연산의 횟수**로 측정하게 된다.  
하지만 연산의 횟수 또한 코드에 조건문과 반복분 등이 존재하면 상황에 따라 횟수가 모두 달라진다.
따라서 연산의 횟수를 카운팅 할때
1. 최선의 경우 (Best Case)
2. 최악의 경우 (Worst Case)
3. 평균의 경우 (Average Case)  

가 있는데, **최악의 경우**로 알고리즘의 시간복잡도를 평가한다.  

### 연산 횟수는 어떻게 측정할까?

Program Step 에서 기본 단위(Elementary Operation)는
1. 대입연산
2. 산술연산(+, -, *, / ..)
3. 비교구문
4. 함수호출
   
정도로 나눌 수 있겠다.
Program Step 을 따라가면서 이 모든 기본단위들이 일어나는 수를 측정하면 된다. 기본적으로 단순 대입, 비교, 산술연산을 실행할 때마다 1씩 카운팅을 해주면 된다.

예시로 선형 탐색과 이분 탐색의 시간복잡도를 계산해보자.

* 예시1) 선형탐색 시간복잡도 계산
<p align='center'><img src='./imgs/linear_search.JPG' width='90%'></p> 

* 예시2) 이분탐색 시간복잡도 계산
<p align='center'><img src='./imgs/binary_search.JPG' width='90%'></p>

* 예시3)
<p align='center'><img src='https://feel5ny.github.io/images/post_img/48/01.png' width='90%'></p>


<br>

## 점근적 표기법(Asymptotic notation)

시간복잡도를 측정하는데 있어서 두 가지 포인트가 있다.  
첫 번째는 **입력값의 크기에 대한 함수 형태**로 나타내야 한다는 것이다.  
두 번째는 **입력값의 크기에 따라 함수가 얼마나 빨리 커지는지** 알아보는 것이다. 이것을 *성장률* 또는 *성장성* 이라고 한다. 바로 이 두 번째 포인트에서 점근적 표기법의 필요성이 대두된다.  

입력값 크기 n 에 대하여 ![수식](./imgs/eq1.svg) 의 시간복잡도를 가진 알고리즘이 있다고 가정해보자. 성장률의 관점에서 볼 때, n 이 매우 커지면 ![수식](./imgs/eq2.svg) 의 성장률이 ![수식](./imgs/eq3.svg) 보다 훨씬 크다. 여기서 계수는 큰 의미가 없으므로 ![수식](./imgs/eq1.svg) 시간복잡도는, ![수식](./imgs/eq2.svg) 로 표기할 수 있다. 이처럼 상수 계수와 중요하지 않은 항목을 제거한 것을 **점근적 표기법(asymptotic notation)** 이라고 한다. **점근적 표기법(asymptotic notation)** 에는 3 가지 형태가 있다.
- **최상의 경우 : 오메가 표기법 (Big-Ω Notation)**
- **최악의 경우 : 빅오 표기법 (Big-O Notation)**
- **평균의 경우 : 세타 표기법 (Big-θ Notation)**  
  
<br>

### 오메가 표기법 (Big-Ω Notation)

<p align='left'><img src='https://feel5ny.github.io/images/post_img/48/o_notation.png' width='40%' ></p> 
 
참고 : 그래프 상에서 y값이 클수록 안 좋은 알고리즘(시간이 많이 걸림)
* 최상의 경우를 표현
* 점근적 하한선
* 알고리즘의 시간복잡도( `f(n)` )가 아무리 최상이여도, `Ω(g(n))` 보단 나쁘다(느리다).
* 정의 : `Ω(g(n)) = {f(n) : there exist positive constants c and n0 such that 0≤cg(n)≤f(n) for all n≥n0}`
* 예시 : 주머니에 1000만원(`f(n)`)이 있을 때, 적어도 10만원(`Ω(g(n))`) 이상은 있다고 말하는 것

n 값이 작을 때는 고려하지않고, n 값이 충분히 클 때(>=n0) 만을 고려한다. 이는 나머지 표기법들도 마찬가지이다.  
또한 시간복잡도 표기를 할 때는 `c*g(n)` 에서 계수인 `c` 를 제거한 `g(n)` 만을 사용한다.

<br>

### 빅오 표기법 (Big-O Notation)

<p align='left'><img src='https://feel5ny.github.io/images/post_img/48/o_notation.png' width='40%' ></p>  

* 최악의 경우를 표현
* 점근적 상한선
* 알고리즘의 시간복잡도( `f(n)` )가 아무리 최악이여도, `O(g(n))` 보단 낫다(빠르다).
* 정의 : `O(g(n)) = {f(n) : there exist positive constants c and n0 such that 0≤f(n)≤cg(n) for all n≥n0}`
* 예시 : "10만원을 가지고 있는데, 확실히 1000만원보다는 적게 가지고 있어" 라고 말하는 것

Big-O 로 시간복잡도를 표현하게 되면 최악의 경우까지 커버를 치는 것이기 때문에 가장 보수적이면서 시간복잡도를 측정할 때 많이 쓰인다.  

아래는 자주 등장하는 Big-O 함수와 그 순서이다.
<p align='center'><img src='https://feel5ny.github.io/images/post_img/48/03.png' width='80%' ></p>  

<p align='center'><img src='https://feel5ny.github.io/images/post_img/48/05.png' width='80%' ></p>  

<br>

### 세타 표기법 (Big-θ Notation)

<p align='left'><img src='https://feel5ny.github.io/images/post_img/48/theta_notation.png' width='40%' ></p>  

* 평균의 경우를 표현
* 점근적 상한선과 점근적 하한선의 교집합
* 알고리즘의 시간복잡도( `f(n)` )가 아무리 좋아지거나 나빠지더라도 , 점근적 상한선과 점근적 하한선 함수의 범위 안에 있다.
* 정의 : `Θ(g(n)) = {f(n) : there exist positive constants c1, c2 and n0 such that 0≤c1g(n)≤f(n)≤c2g(n) for all n≥n0}`
* 예시 : "10만원을 가지고 있는데, 만원보다는 많이 가지고 있고, 1000만원보다는 적게 가지고 있어" 라고 말하는 것

* 세타 표기법 -> 빅오 표기법 항상 참  
ex)  이진 탐색의 최악의 실행 시간은 Θ(![수식](./imgs/eq4.svg)) 이기 때문에 O(![수식](./imgs/eq4.svg)) 이라고도 할 수 있다.
* 빅오 표기법 -> 세타 표기법은 항상 참인 것은 아님  
ex) 이진 탐색이 항상 O(![수식](./imgs/eq4.svg)) 안에 실행되는 것은 맞지만, 항상 Θ(![수식](./imgs/eq4.svg)) 시간에 실행되는 것은 아님 ( 최상의 경우 상수시간에도 실행됨) 

<br>

## Tip

PS 문제를 풀 때, 시간복잡도를 대략적으로 맞추는 방법이다.  
보통 시간제한이 몇 초라고 주어질텐데 **1억번 연산 당 1초** 정도라고 생각하면 된다.

다음은 데이터 수에 따른 적합한 시간복잡도이다.  
| 데이터 수     | 시간복잡도        |  
| --------      | ----------      |  
|  10^8 (1억)   | O(n) , O(logn)  |
|  10^6 (백만)  | O(nlogn)        |
|  10^4 (1만)   | O(n^2)          |
|  500          | O(n^3)          |
|  20           | O(n!) , O(2^n)   |

-> 데이터의 크기가 10^8개일 떄, 시간복잡도가 n, log n 이어야지 1억번의 연산 내로 실행된다.

참고로 일반적으로 O(logn) 이라고하면 O(![수식](./imgs/eq4.svg)) 이라고 생각하면 된다. 

<br>

## Reference
- [알고리즘과 시간 복잡도](https://feel5ny.github.io/2017/12/09/CS_01/)
- [[Algorithm] 알고리즘을 위한 시간복잡도 계산 방법 - Big-O 표기](https://seolhun.github.io/contents/algorithm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%84%EC%82%B0-%EB%B0%A9%EB%B2%95-big-o-%ED%91%9C%EA%B8%B0)
- [<Time Complexity : 시간복잡도> 구하는 법 + 코딩 팁](https://mimimimamimimo.tistory.com/2)
- [점근적 표기법](https://ko.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation)