"""
최대/최소 상수 모음.
무한대(INF) 를 큰 값으로 쓰면 조건문을 단순화할 수 있다.
"""

import math
import sys

# 파이썬 int 는 오버플로가 없지만, 코딩테스트에서 큰 값 초기화 용으로 자주 사용
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1
INF = math.inf  # 가중치 합 초기화 등에 사용
NEG_INF = -math.inf

# 문제에 따라 명시적 큰 수가 더 안전한 경우
BIG = 10**18  # long long 범위 내 큰 값


if __name__ == "__main__":
    print(INT_MAX, INT_MIN)
    print(INF, NEG_INF)
    print(BIG)
