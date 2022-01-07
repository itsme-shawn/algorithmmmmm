# DP 의 tabulation 방식에서 공간(메모리)을 최적화한 방식

def fib_optimized(n):
    cur = 1
    prev = 0

    for i in range(1, n):
        cur, prev = cur + prev, cur
        
    return cur

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

'''
python 에서의 변수 swap 시 내부과정 : 

a, b = b, a

내부로직
tmp = (b, a)
a, b = tmp
'''
