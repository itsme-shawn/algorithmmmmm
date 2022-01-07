# DP 의 tabulation 방식(bottom-up) 이용 -> 반복문 기반

def fib_tab(n):
    table = {}

    for i in range(1, n+1):
        if( i == 1 or i == 2):
            table[i] = 1
        else:
            table[i] = table[i-1] + table[i-2]
    
    return table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

'''
참고 - 딕셔너리보다 리스트를 사용하는 것이 메모리적으로 더 나음
딕셔너리는 key, value 를 저장해야하기 때문임.

리스트와 딕셔너리 비교

리스트 - 리스트 끝에 데이터를 append하는것이 빠르고 인덱스로 데이터 접근도 빠르다.
딕셔너리에 비해 메모리를 덜 차지한다.

딕셔너리 - 탐색 (lookup)이 빠르다. (ex. 리스트에서 'Alice'가 있는지 확인하는것은 O(n) 이지만 딕셔너리에서 'Alice'가 있는지 확인하는것은 O(1)이다.)

```