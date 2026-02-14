"""
피보나치 수 DP 두 가지 패턴.
- 재귀 + 메모이제이션(top-down)
- 반복문 테이블(bottom-up)

입력 크기 N이 10^6 수준까지 커질 수 있으니
반복문 풀이가 일반적으로 더 안전하다.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib_topdown(n: int) -> int:
    """O(N) / O(N) 메모이제이션. 재귀 제한에 주의."""

    if n <= 1:
        return n
    return fib_topdown(n - 1) + fib_topdown(n - 2)


def fib_bottomup(n: int) -> int:
    """O(N) / O(1) 반복문 DP. 가장 자주 쓰이는 형태."""

    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


if __name__ == "__main__":
    target = 10
    print(f"top-down fib({target}) = {fib_topdown(target)}")  # 55
    print(f"bottom-up fib({target}) = {fib_bottomup(target)}")  # 55
