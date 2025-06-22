- 📅 Date: 2020-11-28 (토)

# 버블 정렬(Bubble Sort)


## 📝 개념

리스트를 정렬하는 가장 단순한 알고리즘이다.  
정렬 알고리즘 중 시간복잡도가 최악이다.  

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
def bubble_sort(list) :
  for cnt in range(0, len(list)-1) : # 바깥 루프
    for idx in range(0, len(list)-1-cnt) : # 안쪽 루프
      if( list[idx] > list[idx+1]) :
        list[idx], list[idx+1] = list[idx+1], list[idx]
        
        '''
          temp = list[idx]
          list[idx] = list[idx+1]
          list[idx+1] = temp
        '''
  return list

print(bubble_sort([7,4,5,3,1]))
```

### Solution  

 ![버블정렬](./bubble-sort.png "bubble-sort")  
 
 바깥루프 : 리스트의 개수보다 1개 적은 횟수만큼 반복한다.  
 안쪽루프 : 0번인덱스부터 (마지막-바깥루프횟수)인덱스까지 반복한다.  

 1회전을 수행하고 나면 가장 큰 자료가 맨 뒤로 이동하므로 2회전에서는 맨 끝에 있는 자료는 정렬에서 제외되고, 2회전을 수행하고 나면 끝에서 두 번째 자료까지는 정렬에서 제외된다. 이렇게 정렬을 1회전 수행할 때마다 정렬에서 제외되는 데이터가 하나씩 늘어난다.



### Commentary
- `list[idx], list[idx+1] = list[idx+1], list[idx]`  
파이썬에서는 위와 같이 여러 개의 변수를 교환할 수 있다.

- `for i in range(a, b)` 문에서 i 의 범위는 a <= i < b 이다.

- **⏳ 시간복잡도 : O(n^2)**  


### References
- (If there is any reference)  
[[알고리즘] 버블 정렬(bubble sort)이란](https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html)