- 📅 Date: 2020-11-22 (일)

# 선형 탐색(Linear Search)

## 📝 개념

리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘이다.

가장 간단하고 기본적인 탐색법이지만 효율이 굉장히 안 좋다.

**⏳ 시간복잡도 : O(n)**

<br>

## 📝 예제


* 문제
```
파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 linear_search를 작성하세요.  
0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴해 주면 됩니다.

element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.
```

* 입력
```python
def linear_search(element, some_list):
    # 코드를 작성하세요.

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
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
### Solved code
(Important part only)
``` python
def linear_search(element, some_list):
    for idx in range(0,len(some_list)) :
        if element == some_list[idx] :
            return idx
    return None
    

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
```

### Solution
- x

### Commentary
- x

### References
- (If there is any reference)