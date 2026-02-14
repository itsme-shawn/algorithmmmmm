📅 Date: 2020-12-20 (일)

#  병합정렬 (Merge Sort)

## 🔎 개념

분할 정복(divide and conquer) 알고리즘을 이용한 정렬 알고리즘

### 분할 정복이란? 

한 문제를 유형이 비슷한 작은 여러 개의 하위 문제로 분리(=분할)하고 각각 해결(=정복)한 다음, 결과를 모아서(=결합) 원래의 문제를 해결하는 방법이며 대개 순환 호출(재귀 호출)을 이용하여 구현한다. 따라서 하위 문제를 재귀적으로 해결하기 위해서는 원래 문제보다 범위가 작아야 하며 하위 문제는 탈출 조건이 존재해야 한다.

분할 정복 알고리즘은 세 부분으로 나눠진다.  

1. **분할** : 원래 문제를 분할하여 비슷한 유형의 더 작은 하위 문제들로 나눔.
2. **정복** : 하위 문제들을 재귀적으로 **해결**하고, 하위 문제의 규모가 충분히 작으면 탈출 조건으로 문제를 해결함.
3. **결합** : 하위 문제들의 답을 합쳐서 상위 문제를 해결함.

![분할정복도식화1](https://cdn.kastatic.org/ka-perseus-images/98c02634ee7f970a6bfb0812cc1495bacb462282.png)

![분할정복도식화2](https://cdn.kastatic.org/ka-perseus-images/db9d172fc33b90e905c1213b8cce660c228bb99c.png)




### 과정 설명

1. 분할 : p 와 r 의 중간인 q 를 찾는다.
2. 정복 : 분할 단계에서 만들어진 두 개의 배열(=문제라고 표현할 수 있음) 각각에 있는 하위 배열들을 또 다시 재귀적으로 정렬함.
3. 결합 : 정렬된 두 하위 배열을 하나의 배열로 결합한다.

이 때, 정복 과정에서 탈출 조건이 필요한데, 탈출 조건은 배열의 요소가 1개 이거나 0개 인 경우다. 즉 탈출조건은 `p >= r` 이다.

 ![병합정렬](./merge_sort.jpg "merge_sort")

 위 그림 예제를 통해 병합정렬 흐름을 살펴보자.  

재귀적으로 푸는 문제를 이해할 때는, 나무를 보지 말고 숲을 보는 것이 쉽다. 즉, 큰 문제만 우선 생각해보는 것이다.  

`[14, 7, 3, 12, 9, 11, 6, 2]` 가 있는 배열에서 시작해보자.

1. 분할 : q = 3 이므로 전체 배열을 `[14, 7, 3, 12]` 와 `[9, 11, 6, 2]` 의 하위 배열로 분할함.
2. 정복 : 2개의 하위배열( `[14, 7, 3, 12]` , `[9, 11, 6, 2]` ) 를 각각 정렬한다. 정복과정이 끝나면 하위배열은 `[3, 7, 12, 14]` 와 `[2, 6, 9, 11]` 로 정렬된다.
3. 결합 : 2개의 하위배열을 결합한다. `[2, 3, 6, 7, 9, 11, 12, 14]` 를 얻게 된다.

보다시피 정복 과정에서 하위배열을 정렬시키는 것이 결국 문제의 스케일만 달라졌을뿐, 같은 문제나 다름없다. 따라서 정복 과정에서 하위배열들을 정렬시키는 것을 재귀를 이용해서 풀면 되는것이다.

## 📝 예제

## Input/Output example
### Input

```
[30, 50, 80, 90, 10, 0, 20]
```

### Output
```
[0, 10, 20, 30, 50, 80, 90]
```


## 👌 Code 1 : C 스타일 코드

### 💻 Code

``` python
# merge_sort : 병합정렬의 주 함수
def merge_sort(arr, start=None, end=None):
  if (start == None and end == None):
    start = 0
    end = len(arr) - 1
  
  if (start < end):
    mid = start + (end - start) // 2  # 분할(Divide)
    # mid = (start + end) // 2 와 동일 (오버플로우 방지 스킬)
    merge_sort(arr, start, mid) # 정복(Conquer) : 왼쪽 리스트 정렬
    merge_sort(arr, mid+1, end) # 정복(Conquer) : 오른쪽 리스트 정렬
    merge(arr, start, mid, end) # 결합(Combine)

def merge(arr, start, mid, end):
  for i in range(start, end+1):
    temp[i] = arr[i]     # temp 배열에 원본배열을 그대로 복사함 
    
  part1 = start         # part1 : 왼쪽 리스트의 인덱스 역할
  part2 = mid + 1       # part2 : 오른쪽 리스트의 인덱스 역할
  index = start         # index : 원본 리스트(arr)의 인덱스 역할

  # 왼쪽 리스트와 오른쪽 리스트를 비교하면서 결합하는 과정
  while (part1 <= mid and part2 <= end):
    if (temp[part1] <= temp[part2]):
      arr[index] = temp[part1]
      part1 += 1
    else:
      arr[index] = temp[part2]
      part2 += 1
    index += 1
  
  # while 이 끝나고 왼쪽 리스트(part1)가 남아있으면 원본 리스트에 담아준다.
  # 오른쪽 리스트(part2)는 검사를 안하는 이유는 
  # 왼쪽 리스트(part1)가 다 원본으로 담아졌다면,
  # 이미 오른쪽 리스트는 원본리스트에 정렬된 채로 존재할 것이다.
  if (part1 <= mid and part2 > end): # 사실 if 문은 없어도됨 (코드이해를 위해 남겨둠)
    for i in range(0, (mid - part1) + 1):
      arr[index + i] = temp[part1 + i]

arr = [30, 50, 80, 90, 10, 0, 20]
temp = list()  # 임시배열은 전역변수로 사용하는게 메모리 효율적

for _ in range(0, len(arr)):
  temp.append(0)

print('Before sorted : ', arr)

merge_sort(arr)

print('After sorted : ', arr)
```

### ✍ Solution
- 병합 정렬 개념 설명과 주석으로 대체

### 💬 Commentary
- 함수의 파라미터로 리스트를 넘겨줌으로써, 직접 리스트에 참조형식으로 접근하기 때문에 리스트를 `return` 하는 방식을 사용하지 않는다. 원본 리스트 자체가 정렬된다.
- 맨 처음에 분할 과정을 되게 거창하게 생각했는데, 단순히 인덱스의 중간 값을 계산하는 식 한 줄이 분할과정이여서 좀 신기했다.
- 이 방식은 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하기 때문에 메모리 사용량을 대폭 줄일 수 있다. (제자리 정렬; In-place sort)  
물론 temp 배열을 사용하긴 하지만, temp 배열은 결합과정에서 원본과의 비교를 위한 임시배열인데다가 전역변수여서 사실상 메모리 소모가 거의 없다.


## 👌 Code 2 : 파이썬 스타일 코드

### 💻 Code

``` python
# merge 방식을 통해 정렬된 temp 리스트를 return 하는 함수
def merge(left, right):
  temp = list()
  i = 0   # left array index
  j = 0   # right array index

  while(i < len(left) and j < len(right)):
    if(left[i] <= right[j]):
      temp.append(left[i])
      i += 1
    else:
      temp.append(right[j])
      j += 1
  
  if(i == len(left)): # 오른쪽 리스트가 아직 남아있음
    temp += right[j : len(right)]
  if(j == len(right)): # 왼쪽 리스트가 아직 남아있음
    temp += left[i : len(left)]
  return temp

def merge_sort(arr):
  if(len(arr) <= 1):
    return arr
  
  mid_idx = len(arr) // 2 # 분할

  left = merge_sort(arr[0:mid_idx])         # 정복 : 왼쪽 부분배열 정렬
  right = merge_sort(arr[mid_idx:len(arr)]) # 정복 : 오른쪽 부분배열 정렬
  return merge(left, right) # 결합 : 정렬된 왼쪽,오른쪽 부분배열 결합

print(merge_sort([30, 50, 80, 90, 10, 0, 20]))

```

### ✍ Solution
- 

### 💬 Commentary
- 병합 결과를 담을 새로운 배열인 `temp` 를 매번 생성해서 리턴하고, 리스트 slice( `arr[start:end]` )를 사용하면 리스트가 복제되기 때문에 풀이 1 보다는 메모리적으로 좋지않다.
하지만 훨씬 코드가 직관적이고 짧아서 나는 이 코드를 선호한다.
- 원래 배열은 그 상태로 그대로 존재하게 된다.



## References
- [[자료구조 알고리즘] 병합정렬(Merge Sort) 구현하기](https://www.youtube.com/watch?v=QAyl79dCO_k)
- [머지소트 병합정렬 5분만에 이해하기- Gunny](https://www.youtube.com/watch?v=FCAtxryNgq4)
- [파이썬으로 병합 정렬 구현하기](https://leedakyeong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-merge-sort-in-python-bottom-up-%EB%B0%A9%EC%8B%9D)
- [[알고리즘] 합병 정렬(merge sort)이란](https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html)
- [병합 정렬이란? (개념 이해하기)](https://ko.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)