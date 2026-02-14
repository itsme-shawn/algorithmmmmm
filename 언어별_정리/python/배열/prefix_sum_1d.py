"""
1차원 누적합(prefix sum) 기본 패턴.
구간합 질의가 많을 때 O(1) 로 계산 가능.
"""

from typing import List


def build_prefix(arr: List[int]) -> List[int]:
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps


def range_sum(ps: List[int], l: int, r: int) -> int:
    """0-indexed, 구간 [l, r] 합"""
    return ps[r + 1] - ps[l]


if __name__ == "__main__":
    arr = [2, -1, 3, 5]
    ps = build_prefix(arr)
    print(ps)  # [0, 2, 1, 4, 9]
    print(range_sum(ps, 1, 3))  # 7
