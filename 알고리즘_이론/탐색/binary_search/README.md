- 📅 Date: 2020-11-22 (일)

# 이진 탐색(Binary Search)

## 📝 개념

**❗ 이진탐색은 정렬된 리스트(오름차순/내림차순)를 전제로 한다**

이진탐색은 리스트의 인덱스 상 중간값과 내가 찾고자 하는 값을 비교하면서 수를 탐색 범위를 절반씩 줄여나간다.

**⏳ 시간복잡도 : O(log N)**

<br>

## 📝 예제


* 문제
```
이진탐색 알고리즘을 이용하여 파라미터로 탐색할 값 element와  
리스트 some_list를 받는 함수 binary_search를 작성하세요.  

element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.
```

* 입력
```python
def binary_search(element, some_list):
    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

* 출력
```
0
None
2
1
4
```

<br>

## 💡 풀이

### 재귀방식

``` python
# 재귀
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index==None :
        end_index = len(some_list) - 1
    
    if start_index > end_index :
        return None
        
    mid = (start_index + end_index) // 2
    
    if some_list[mid] == element :
        return mid
    elif some_list[mid] > element :
        end_index = mid - 1
    else :
        start_index = mid + 1
    
    return binary_search(element,some_list,start_index,end_index)
           
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

### 반복문 방식

```python
# 반복문
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if some_list[mid_index] == element :
            return mid_index
        elif some_list[mid_index] < element :
            start_index = mid_index + 1
        else :      # some_list[mid_index] > element 
            end_index = mid_index - 1
    return None
    
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

### Commentary
- 재귀 방식에서는 함수의 파라미터로 `start_index` 와 `end_index` 로 설정해주고,  함수의 파라미터 값을 defulat 값으로 설정하는 idea 중요
- `start_index > end_index` 일 때 탐색실패

### References
- https://velog.io/@jinstonlee/%EC%84%A0%ED%98%95-%ED%83%90%EC%83%89%EA%B3%BC-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89