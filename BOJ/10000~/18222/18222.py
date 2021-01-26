import sys

k = int(sys.stdin.readline())

def recursion(x):
    if (x==1):
        return 0

    N = maxPowerOf2(x)
    
    return 1-recursion(x-N)

# n보다 작은 수 중 가장 큰 2의 거듭제곱수를 찾는 함수
def maxPowerOf2(n):
    m = 0
    while( 2 ** m < n ):
        m += 1
    
    return 2 ** (m-1)

print(recursion(k))


