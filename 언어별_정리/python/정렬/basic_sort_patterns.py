"""
파이썬 정렬 기본 패턴 모음.
- in-place: list.sort()
- 새 리스트: sorted()
- stable 정렬이므로 다중 key를 튜플에 담아 한 번에 처리 가능.
"""

from typing import List, Tuple


def sort_numbers(nums: List[int]) -> List[int]:
    """가장 단순한 오름차순/내림차순."""

    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    return asc + desc


def sort_by_two_keys(data: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    1차: 첫 번째 값 오름차순
    2차: 두 번째 값 내림차순
    """

    return sorted(data, key=lambda x: (x[0], -x[1]))


def stable_sort_then_resort(data: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    stable 특성을 이용한 단계별 정렬 예시.
    뒤에서 앞으로 key를 쌓는 순서에 주의.
    """

    by_second = sorted(data, key=lambda x: x[1])
    by_first_then_second = sorted(by_second, key=lambda x: x[0])
    return by_first_then_second


if __name__ == "__main__":
    nums = [5, 1, 3, 3, 2]
    print(sort_numbers(nums))  # [1, 2, 3, 3, 5, 5, 3, 3, 2, 1]

    pairs = [(1, 3), (1, 5), (0, 9), (2, 0), (2, 5)]
    print(sort_by_two_keys(pairs))
    # [(0, 9), (1, 5), (1, 3), (2, 5), (2, 0)]

    print(stable_sort_then_resort(pairs))
