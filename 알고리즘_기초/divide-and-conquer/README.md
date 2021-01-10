📅 Date: 2021-01-10 (일)

# 분할정복 (Divide and Conquer)

## 🔎 개념

> 병합 정렬을 다룰 때 이미 분할정복은 공부했으므로 그것으로 대체함. 여기서는 예제에 좀 더 포커스를 두도록 하겠다.

한 문제를 유형이 비슷한 작은 여러 개의 하위 문제로 분리(=분할)하고 각각 해결(=정복)한 다음, 결과를 모아서(=결합) 원래의 문제를 해결하는 방법이며 대개 순환 호출(재귀 호출)을 이용하여 구현한다. 따라서 하위 문제를 재귀적으로 해결하기 위해서는 원래 문제보다 범위가 작아야 하며 하위 문제는 탈출 조건이 존재해야 한다.

분할 정복 알고리즘은 세 부분으로 나눠진다.  

1. **분할** : 원래 문제를 분할하여 비슷한 유형의 더 작은 하위 문제들로 나눔.
2. **정복** : 하위 문제들을 **재귀적으로 해결**하고, 하위 문제의 규모가 충분히 작으면 탈출 조건으로 문제를 해결함.
3. **결합** : 하위 문제들의 답을 합쳐서 상위 문제를 해결함.

![분할정복도식화1](https://cdn.kastatic.org/ka-perseus-images/98c02634ee7f970a6bfb0812cc1495bacb462282.png)

![분할정복도식화2](https://cdn.kastatic.org/ka-perseus-images/db9d172fc33b90e905c1213b8cce660c228bb99c.png)


## 📝 예제 1️⃣

start 와 end 까지 더하는 함수를 divide and conquer 를 이용해 구현

## 👌 풀이

### 💡 Idea
분할정복으로 접근할 때 핵심은 **분할**, **정복**, **결합**을 어떻게 처리할 것인가이다.  
또한 재귀의 탈출조건 (base case) 이 필요한데, 함수의 맨 위에 써주는 것이 좋은 것 같다.

### 💻 Code

``` python
def consecutive_sum(start, end):
  # base case
  if(start == end):
    return start

  mid = (start + end) // 2  # 분할

  return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)  
  # 각각의 consecutive_sum() 호출은 정복
  # 두 함수의 리턴값을 더하는 과정이 결합

# 테스트
print(consecutive_sum(1, 10))   # 55
print(consecutive_sum(1, 100))  # 5050
print(consecutive_sum(1, 253))  # 32131
print(consecutive_sum(1, 388))  # 75466
```

### ✍ Solution
- 분할정복 알고리즘은 큰 틀에서 모두 비슷비슷하다.
  1. 재귀함수의 base case 설정
  2. 분할
  3. 정복
  4. 결합
  
  이 때, 분할이나 결합 과정에서 로직이 복잡하면 외부함수로 빼서 구현할 수도 있다.  
  ( 병합정렬에서는 결합과정에서 `merge` 함수이용, 퀵정렬에서는 분할과정에서 `partiton` 함수이용 ) <br>
  
  정복과정은 보통 argument 값을 잘 처리해서 재귀호출을 하는 것이 대부분이다.

### 💬 Commentary
- 재귀의 탈출조건(base case) 를 조건문으로 안 쓰고 반복문으로 쓰는 것도 가능하다.
반복문으로 base case 를 사용할 때에는 반복문 안에 로직들이 다 들어가야 하고 반복문 바깥에 base case 에서의 return 문이 오게 된다.
  ```python
  def consecutive_sum(start, end):
    # base case
    while(start != end):

      mid = (start + end) // 2  # 분할

      return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)  
      # 각각의 consecutive_sum() 호출은 정복
      # 두 함수의 리턴값을 더하는 과정이 결합

    return start
  ```
<br>

## 📝 예제 2️⃣

**병합정렬**

## 👌 풀이

자세한 설명은 기존에 작성한 [병합정렬 (merge sort)](../sort/merge_sort) 문서 참고

### 💻 Code

``` python
# merge : 정렬된 두 리스트 list1과 list2를 받아서, 하나의 정렬된 리스트를 리턴하는 함수
def merge(list1, list2):
  newlist = []
  i = j = 0
  while(i < len(list1) and j < len(list2)):
    if(list1[i] <= list2[j]):
      newlist.append(list1[i])
      i += 1
    else:  # ( list1[i] > list2[j])
      newlist.append(list2[j])
      j += 1
  if(i == len(list1)):  # list2 가 아직 다 안들어옴
    newlist += list2[j:]
  if(j == len(list2)):
    newlist += list1[i:]
  return newlist

# merge_sort : 병합 정렬
def merge_sort(my_list):
  # base case
  if(len(my_list) <= 1):
    return my_list
  
  mid = len(my_list) // 2  # 분할
  left = merge_sort(my_list[:mid])  # 정복
  right = merge_sort(my_list[mid:]) # 정복

  return merge(left,right)  # 결합

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

```
<br>

## 📝 예제 3️⃣

**퀵 정렬**

## 👌 풀이

자세한 설명은 기존에 작성한 [퀵정렬 (quick sort)](../sort/quick_sort) 문서 참고

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
  big_idx += 1

  return pivot_idx

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
list0 = [1, 6, 5, 3, 4]
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

