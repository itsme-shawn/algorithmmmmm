📅 Date: 2021-01-25 (월)

# 2630. 색종이 만들기
출처: https://www.acmicpc.net/problem/2630

## 📝 Problem

### 문제

아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.

<p align='center'><img src="https://www.acmicpc.net/upload/images/bwxBxc7ghGOedQfiT3p94KYj1y9aLR.png" /></p>

전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.

<p align='center'><img src="https://www.acmicpc.net/upload/images/VHJpKWQDv.png" /></p>

입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.


### 출력

첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

## Input/Output example
### Input

```
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
```

### Output
```
9
7
```

# ✅ Submit
## 👌 Solved Code 1

### 💡 Idea
분할정복 문제이다. 배열을 4개의 사각형으로 분리해야하는데, x축 y축 인덱스 조작을 통해 분할한다.


### 💻 Code
(Important part only)

``` python
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def cut(y, x, sideLen): # sideLen : 한 변의 길이
    color = paper[y][x] # paper 의 시작점의 색을 기준색으로 뽑는다.

    half = sideLen // 2 

    for i in range(y, y+sideLen):
        for j in range(x, x+sideLen):
            if (color != paper[i][j]):      # paper 의 모든 색을 살피면서 기준색과 다르면 4등분으로 cut 해야함
                cut(y, x, half)             # 왼쪽 위       (분할&정복)
                cut(y, x+half, half)        # 왼쪽 아래     (분할&정복)
                cut(y+half, x, half)        # 오른쪽 위     (분할&정복)
                cut(y+half, x+half, half)   # 오른쪽 아래   (분할&정복)
                return  # return 문 없으면 재귀 한 사이클을 돌고나서도 이전 콜스택으로 못 빠져나옴
    
    # 결합
    if (color == 1):
        result.append(1)
    else:
        result.append(0)

cut(0, 0, N)
print(result.count(0))
print(result.count(1))
```

### 💬 Commentary  

- 삽질하고 고민했던 내용
  - 배열을 분할해야한다는 것에 너무 휩싸여서 배열 인덱스 조작을 통해 분할효과를 내면 될 것을, 실제로 배열을 쪼개려고 하다가 애먹음
  - 그 동안 분할정복 문제를 풀던 패턴( base case 먼저 if문으로 처리하고 값 return) 하고 좀 달랐음 -> 패턴을 외우려고 하지말고 유연하게 사고 
  - 참조형 자료형(리스트)를 사용하면 global 키워드를 쓰지않고도 전역변수처럼 사용할 수 있다.
  - 하얀색과 파란색 색종이의 값을 누적으로 기억하고 더해주기 위한 방법을 고안하기 위해 고민을 많이 했는데, 어렵게 생각하기보다 그냥 전역변수 쓰자.

- 눈여겨볼만한 내용
  - 2차원배열에서 x축,y축 순서를 거꾸로해야 직관적이다.  
  ( `arr[x][y]` 가 아니라 `arr[y][x]`)

<br>

## 👌 Solved Code 2

### 💡 Idea
Solved Code 1 과 큰 틀에서 로직은 동일한데, 세부적으로 잡기술(?)만 조금 다르다.  
* flag 사용
* 재귀함수 콜스택 알맞게 탈출하기 위해서 return 대신 break 사용 -> 이중 for 문을 탈출해야해서 좀 까다로움
* 전역변수 사용 ( 함수내에서 global 키워드 사용)

### 💻 Code
(Important part only)

``` python
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt_white, cnt_blue = 0, 0

def cut(y, x, sideLen):
    global cnt_white, cnt_blue

    color = paper[y][x]
    flag = True
    half = sideLen // 2
    
    for i in range(y, y+sideLen):
        if not flag:    # 이중for문 탈출용
            break
        for j in range(x, x+sideLen):
            if (color != paper[i][j]):
                flag = False
                cut(y, x, half)             # 왼쪽 위       (분할&정복)
                cut(y, x+half, half)        # 왼쪽 아래     (분할&정복)
                cut(y+half, x, half)        # 오른쪽 위     (분할&정복)
                cut(y+half, x+half, half)   # 오른쪽 아래   (분할&정복)
                break   # return 문을 안쓰고 break

    if flag:    # 콜스택이 다 끝나고 flag 가 False 인 상태로 여기에 들어오는 것 방지 -> 이것때문에 return 보다 break 가 좀 까다로움
        if (color == 1):
            cnt_blue += 1
        else:
            cnt_white += 1

cut(0, 0, N)
print(cnt_white)
print(cnt_blue)
```

### 💬 Commentary
- 파이썬은 함수 밖 영역에서 변수를 선언한 전역변수는 read 만 되고, write 가 안된다. write 까지 할려면 함수 내에서 global 키워드를 선언해줘야한다.

## References
- [풀이 1 참고](https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python)
- [풀이 2 참고](https://suri78.tistory.com/66)