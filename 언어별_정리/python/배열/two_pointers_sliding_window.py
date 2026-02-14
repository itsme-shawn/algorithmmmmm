"""
투 포인터 / 슬라이딩 윈도우 예제.
- 배열이 모두 양수일 때 길이/합 조건을 빠르게 맞출 수 있다.
"""

from typing import List


def longest_subarray_leq(arr: List[int], limit: int) -> int:
    """
    합이 limit 이하인 가장 긴 구간 길이.
    양수 배열 기준 O(N) 슬라이딩 윈도우.
    """

    left = 0
    cur = 0
    best = 0
    for right, val in enumerate(arr):
        cur += val
        while cur > limit:
            cur -= arr[left]
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    nums = [2, 1, 3, 2, 4]
    print(longest_subarray_leq(nums, 6))  # 3 (2+1+3)
