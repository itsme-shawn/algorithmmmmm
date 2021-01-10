📅 Date: 2021-01-10 (일)

# 퀵 정렬 (quick sort)

## 🔎 개념

* 퀵 정렬은 불안정 정렬 에 속하며, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬 에 속한다.
* 분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법
합병 정렬(merge sort)과 달리 퀵 정렬은 리스트를 비균등하게 분할한다.
* 분할 정복(divide and conquer) 방법

  * 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략이다.
  * 분할 정복 방법은 대개 순환 호출을 이용하여 구현한다.

## 퀵 정렬 과정 설명

1. 리스트 안에 있는 한 요소를 선택한다. ( 리스트의 가장 오른쪽 요소, or 왼쪽 요소, or 랜덤 ) 이렇게 고른 원소를 피벗(pivot) 이라고 한다.
2. 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 옮겨지고 피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨지게끔 만든다. (피벗을 중심으로 왼쪽: 피벗보다 작은 요소들, 오른쪽: 피벗보다 큰 요소들)
-> 이 부분은 지금 이해가 안될 수도 있는데 partiton 함수를 설명하는 부분에서 더 자세히 설명한다.
3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
   * 분할된 부분 리스트에 대하여 순환 호출 을 이용하여 정렬을 반복한다.
   * 부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개의 부분 리스트로 나누는 과정을 반복한다.
4. 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.
   * 리스트의 크기가 0이나 1이 될 때까지 반복한다.
  
<p align='center'><img src="./imgs/qsort.JPG" width='50%'/></p>

> 💡 피벗(pivot)을 어떤 것으로 선택하냐에 따라서 퀵 정렬 안에서도 시간복잡도가 달라진다. 일단 나는 리스트의 가장 오른쪽 요소를 피벗으로 선택하는 로직으로 구현했다. 이 외에도 가장 왼쪽을 선택하는 방법, 아예 랜덤으로 피벗을 선택하는 방법도 있다.

<br>

## 퀵 정렬의 분할(Divide) 과정 : partiton 함수

퀵 정렬은 **분할 과정**에서 거의 모든 것이 이뤄진다고 해도 과언이 아니다. ( 한편 병합정렬은 결합과정이 핵심이다. )  

퀵 정렬의 분할 로직이 구현되는 partition 함수는 피벗을 기준으로 작은 값은 피벗 왼쪽에, 큰 값은 피벗 오른쪽에 배치되게끔 한다. 

<p align='center'><img src="./imgs/partition1.JPG" width='50%'/></p>

주의할 점은 배치만 될 뿐, 정렬은 되지 않는다.
그렇다면 정렬은 언제하는가? 파티션된 리스트에서 재귀적으로 또 다시 퀵 정렬을 돌리면 마지막에 알아서 정렬이 된다.

### 파티션 그룹

<p align='center'><img src="./imgs/partition2.JPG" width='50%'/></p>

파티션은 4개 (실제로 존재하는 것은 2개)로 나눌 수 있는데, small 그룹, big 그룹, unknown 그룹, pivot 이다.  
사실 unknown 그룹은 중간과정에서 아직 탐색하지 않은 그룹을 이름지어 놓은 것이라서 partiton 함수가 최종적으로 끝나면 small group, big 그룹, pivot 만 존재하게 된다.

### partiton 함수 진행 과정

1. **시작**
    <p align='center'><img src="./imgs/partition3.JPG" width='50%'/></p>
    Pivot 은 리스트의 맨 오른쪽 요소로 설정하고, i,b,start 는 시작 인덱스를 할당, p 값에는 끝 인덱스를 할당한다.

<br>

2. 16 이 7(피벗) 보다 크므로, b 값은 가만히 있고 i(current index)만 증가시킨다.
    <p align='center'><img src="./imgs/partition4.JPG" width='50%'/></p>

<br>

3. 6 은 7(피벗) 보다 작다. 이 부분은 조금 복잡하다.
    <p align='center'><img src="./imgs/partition4_1.JPG" width='50%'/></p>

    <p align='center'><img src="./imgs/partition5.JPG" width='50%'/></p>
      b 가 가리키는 요소와 swap 한 후, b 와 i 를 1씩 증가시킨다.  
      이제 나머지 unknown 그룹을 똑같은 로직으로 처리해나가면 된다.

<br>

4. unknown 그룹까지 모두 Pivot 과 비교가 끝나면, small 그룹과 big 그룹이 아래처럼 나뉘게 된다.
    <p align='center'><img src="./imgs/partition6.JPG" width='50%'/></p>

<br>

5. Pivot 이 small 그룹과 big 그룹의 중간에 들어가야 하기 때문에, b 가 가리키는 요소와 Pivot 을 swap 한다. 이제 Pivot index 값이 b 가 가리키는 값이 된다.
    <p align='center'><img src="./imgs/partition7.JPG" width='50%'/></p>


## 👌 풀이

### 💻 Code

``` python
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(lst, idx1, idx2):
  lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(lst, start, end):
  pivot_idx = end 
  big_idx = cur_idx = start # small 그룹의 첫 번째 요소는 start 인덱스이므로 small_idx 변수 필요없음

  # cur_idx 가 pivot_idx 보다 작을 동안만 loop
  while( cur_idx < pivot_idx ):
    if( lst[cur_idx] >= lst[pivot_idx] ): # cur_idx 가 가리키는 요소를 big 그룹에 추가
      cur_idx += 1
    elif( lst[cur_idx] < lst[pivot_idx] ):  # cur_idx 가 가리키는 요소를 small 그룹에 추가
      swap_elements(lst, cur_idx, big_idx)  # cur_idx 의 요소를 big 그룹의 첫 요소와 swap 함
      cur_idx += 1
      big_idx += 1  # cur_idx 와 big_idx 가 한 칸씩 전진함으로써 small 그룹도 확장됨
    
  # pivot 요소와 big 요소를 swap 하고 big_idx 를 1 늘려주면 small, pivot, big 그룹으로 partiton 완료  
  swap_elements(lst, pivot_idx, big_idx)
  pivot_idx = big_idx 
  big_idx += 1  # 이건 안해도 되긴 함

  return pivot_idx # 정복과정에서 pivot 인덱스를 사용하므로 return 필수!

# 퀵 정렬
def quicksort(lst, start=None, end=None):

  # Set Optional Parameter
  if( start == None and end == None):
    start = 0
    end = len(lst) - 1  # pivot 을 항상 대상 list 의 맨 오른쪽으로 설정하는 퀵소트임

  # base case
  if( start > end ):
    return
  
  pivot = partition(lst, start, end)  # 분할
  quicksort(lst, start, pivot-1)      # 정복
  quicksort(lst, pivot+1 , end)       # 정복

  # quick sort 는 원래 list 상에서 sort 를 하기 때문에, 결합 과정이 필요없음


# 테스트 0
list0 = [2, 6, 5, 3, 4]
quicksort(list0, 0, len(list0) - 1)
print(list0)  # [1, 3, 4, 5, 6]
  
# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)  # [1, 3, 5, 7, 9, 11, 11, 13]

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)  # [1, 5, 7, 9, 13, 15, 28, 30, 48]

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)  # [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]
```

### ✍ Solution
- `partiton` 함수 구현이 중요하긴 하지만, 분할정복 알고리즘에서 메인은 **분할**, **정복**, **결합** 을 어떻게 처리할 것이냐 이다.
  
  * 분할 : partiton 함수
  * 정복 : argument 조절해서 quick_sort 재귀호출
  * 결합 : 따로 필요없음 ( quick_sort 는 원래배열에서 정렬 이루어짐 )
  

### 💬 Commentary
- 두 가지 부분에서 시간이 오래 걸렸다.

  1. pivot 을 정렬을 안해도 된다. `partiton` 함수가 끝나면 이미 small 그룹과 big 그룹 사이에 알맞게 위치하기 때문이다. 아래처럼 pivot 을 포함해서 재귀를 호출하면 무한루프가 발생한다.

      ```python
      quicksort(lst, start, pivot)      # 무한루프 발생 -> pviot-1 로 해야함
      quicksort(lst, pivot+1 , end)     # 정복
      ```

  2. base case 에서 `start == end` 라고하면 안되는가?

      맨 처음에 `start == end`  라고 했다가 무한루프가 돌았다.  
      `[2, 6, 5, 3, 4]` 예시에서 맨 처음 pivot 이 4이므로 `partiton` 함수 후 `[2, 3, 4, 6, 5]` 로 리스트가 바뀌게 될 것이다.  
      이제 `[2, 3]` 에서 재귀적으로 퀵 정렬이 한 번 더 들어가는데, 여기서 pivot(3) 인덱스는 1이다.  ( start = 0, end = 1)  
      따라서 `quicksort(lst, pivot+1 , end)` 이 재귀호출에서 `quicksort(lst, 2 , 1)` 로 호출된다.  
      즉, `start == end` 로 탈출조건을 설정하면 요소가 없는 그룹에서 무한루프가 돌게 된다.   
    
      `if( start > end ): ` 로 탈출조건을 설정하니 잘 작동한다.

* Optional Parameter 사용
  
  ```python
  def quicksort(lst, start=None, end=None):

  # Set Optional Parameter
  if( start == None and end == None):
    start = 0
    end = len(lst) - 1  # pivot 을 항상 대상 list 의 맨 오른쪽으로 설정하는 퀵소트임

  ...

  quicksort(list0, 0, len(list0) - 1) # 1️⃣

  quicksort(list1)  # 2️⃣

  ```

  1️⃣ 보단 2️⃣가 깔끔해보이므로 Optional Parameter 를 사용했다.


## References
- [[알고리즘] 퀵 정렬(quick sort)이란](https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html)
- [코드잇 강의](https://www.codeit.kr/)