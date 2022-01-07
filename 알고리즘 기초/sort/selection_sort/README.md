- 📅 Date: 2020-11-28 (토)

# 선택 정렬 (Selection Sort)

## 📝 개념

우리가 실생활에서 직관적으로 생각하는 정렬하는 방식과 같다.

1. 주어진 배열 중에서 최솟값을 찾는다.  
2. 그 값을 맨 앞에 위치한 값과 교체한다(패스(pass)).  
3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.  
4. 하나의 원소만 남을 때까지 위의 1~3 과정을 반복한다. 

<br>

 ![선택정렬](./selection_sort.png "selection-sort")  

<br>

## 📝 예제


* 문제  
배열에 7, 4, 5, 1, 3이 저장되어 있다고 가정하고 자료를 오름차순으로 정렬해 보자.


* 입력  
[7,4,5,3,1]


* 출력  
[1,3,4,5,7]

<br>

## 💡 풀이
### Solved code
(Important part only)
``` python
def selection_sort(list) :
  for i in range(0, len(list)-1) : # 외부 루프 : n-1 번
    min_idx = i
    for j in range(i+1, len(list)) : # 내부 루프 : 최솟값 탐색
      if( list[j] < list[min_idx] ) :
        min_idx = j
    list[i], list[min_idx] = list[min_idx], list[i] # SWAP
  return list

print(selection_sort([7,4,5,3,1]))

```

### Solution
- 외부 루프를 한 번 돌때마다 왼쪽부터 하나씩 정렬이 된다.  
  내부 루프에서는 최솟값 탐색을 하고, 안쪽 루프가 끝나면 (= 최솟값 탐색 완료) SWAP 을 진행한다.

### Commentary
- 크게 어렵지 않지만 포인트가 좀 있다.
1. min 변수에 최솟값을 직접 담는 것이 아니라 **인덱스**로 이용해야 쉽게 풀린다.  

2. 원소 개수가 n개라면 **n-1** 번만 외부 루프를 돌리면 정렬이 완료된다. ( 만약 n번 돌리게 되면 그 자리에서 한 번 더 SWAP이 돼서 다른 결과가 나온다. )  
3. 안쪽 루프의 반복문  `for j in range(i+1, len(list))` 에서 
 j 가 i 부터가 아닌 i+1 로 하면 더 효율적이다.

### ⏳ 시간복잡도

<h4>최선의 경우(Best case) : 자료가 이미 정렬되있는 경우</h4> 

- 외부 루프 : (n-1)번
- 내부 루프(최솟값 찾기) : 처음 외부 루프에서 (n-1)회 , 두 번째 외부 루프에서 (n-2)회, ... n-1 번째 외부 루프에서 1회 = n(n-1) / 2
- 자리 교환 : 발생 안 함  

  **총 소요 시간 : n(n-1) / 2**

<h4>최악의 경우(Worst case) : 최솟값만 맨 뒤에 있는 경우</h4> 

- 외부 루프 : (n-1)번
- 내부 루프(최솟값 찾기) : 처음 외부 루프에서 (n-1)회 , 두 번째 외부 루프에서 (n-2)회, ... n-1 번째 외부 루프에서 1회 = n(n-1) / 2
- 자리 교환 : 모든 외부 루프 당 1번씩 실행되므로 n-1 회 실행

  **총 소요 시간 : n(n-1) / 2 + (n-1)**

따라서 최선이든 최악이든 시간복잡도는 
 **O(n^2)** 이다.

### References
- [[알고리즘] 선택 정렬(selection sort)이란](https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html)
- [선택정렬](https://mong9data.tistory.com/42)
- [[알고리즘] 선택 정렬 - Slection Sort (Python, Java)](https://www.daleseo.com/sort-selection/)
