# DP 의 memoization 방식(top-down) 이용 -> 재귀 기반

def fib_memo(n, cache):
    # base case
    if (n == 1 or n == 2):
        cache[n] = 1
    
    # 아직 n번째 피보나치 수를 계산 안했으면 -> 재귀로 계산 후 caceh 에 저장
    if (n not in cache):
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)

    # 이미 n번째 피보나치 수를 계산한 경우 -> caceh 에 있는 값을 리턴
    # if ( n in cache ):
    return cache[n]



def fib(n):
    # n번째 피보나치 수를 담는 캐시
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))