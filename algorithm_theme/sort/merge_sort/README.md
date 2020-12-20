📅 Date: 2020-12-20 (일)

#  병합정렬 (Merge Sort)

## 🔎 개념




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


## 👌 풀이 1 : C 스타일 코드

### 💡 Idea


### 💻 Code
(Important part only)

``` python
# merge_sort : 병합정렬의 주 함수
def merge_sort(arr, start=None, end=None):
  if (start == None and end == None):
    start = 0
    end = len(arr) - 1
  
  if (start < end):
    mid = start + (end - start) // 2  # mid = (start + end) // 2 와 동일 (오버플로우 방지 스킬)
    merge_sort(arr, start, mid) # 분할(Divide) : 왼쪽 리스트
    merge_sort(arr, mid+1, end) # 분할(Divide) : 오른쪽 리스트
    merge(arr, start, mid, end) # 정복(Conquer)

def merge(arr, start, mid, end):
  for i in range(start, end+1):
    temp[i] = arr[i]     # temp 배열에 원본배열을 그대로 복사함
    
  part1 = start         # part1 : 왼쪽 리스트의 인덱스 역할
  part2 = mid + 1       # part2 : 오른쪽 리스트의 인덱스 역할
  index = start         # index : 원본 리스트(arr)의 인덱스 역할

  # 왼쪽 리스트와 오른쪽 리스트를 비교하면 실제로 merge 하는 작업
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
-

### 💬 Commentary
- 

## 👌 풀이 2 : 파이썬 스타일 코드

### 💡 Idea


### 💻 Code
(Important part only)

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
  
  if(i == len(left)):
    temp += right[j : len(right)]
  if(j == len(right)):
    temp += left[i : len(left)]
  return temp

def merge_sort(arr):
  if(len(arr) <= 1):
    return arr
  
  mid_idx = len(arr) // 2

  left = merge_sort(arr[0:mid_idx])         # 왼쪽 부분 리스트 분할
  right = merge_sort(arr[mid_idx:len(arr)]) # 오른쪽 부분 리스트 분할
  return merge(left, right)

print(merge_sort([30, 50, 80, 90, 10, 0, 20]))
```

### ✍ Solution
- 

### 💬 Commentary
- `merge()` 함수 내에서 임시 배열인 `temp` 를 계속해서 생성하고 `return` 하기 있고, 리스트 slice( `arr[start:end]` )를 사용하면 리스트가 복제되기 때문에 풀이 1 보다는 메모리적으로 좋지않다. 하지만 훨씬 코드가 직관적이고 짧아서 나는 이 코드를 선호한다.



## References
- [[자료구조 알고리즘] 병합정렬(Merge Sort) 구현하기](https://www.youtube.com/watch?v=QAyl79dCO_k)
- [머지소트 병합정렬 5분만에 이해하기- Gunny](https://www.youtube.com/watch?v=FCAtxryNgq4)
- [파이썬으로 병합 정렬 구현하기](https://leedakyeong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-merge-sort-in-python-bottom-up-%EB%B0%A9%EC%8B%9D)
- [[알고리즘] 합병 정렬(merge sort)이란](https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html)