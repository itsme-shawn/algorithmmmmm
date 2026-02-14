"""
여러 숫자/리스트 입력 패턴 모음.
sys.stdin.readline() + split() + map() 조합이 가장 빠르고 흔하다.
"""

import sys
from io import StringIO
from typing import List


def read_int_list(fake: StringIO) -> List[int]:
    """한 줄에 공백 구분된 정수들"""
    return list(map(int, fake.readline().split()))


def demo_unpack_two() -> None:
    fake = StringIO("10 20\n")
    a, b = map(int, fake.readline().split())
    print(a, b)  # 10 20


def demo_list_and_matrix() -> None:
    fake = StringIO("5\n1 2 3 4 5\n")
    n = int(fake.readline())
    nums = read_int_list(fake)
    print(n, nums)  # 5 [1, 2, 3, 4, 5]


def demo_unknown_count(fake: StringIO) -> None:
    """
    줄 수를 모를 때: for line in sys.stdin 사용.
    여기서는 StringIO 로 시뮬레이션.
    """

    data = []
    for line in fake:
        if not line.strip():
            continue
        data.append(list(map(int, line.split())))
    print(data)  # [[1, 2], [3, 4, 5]]


if __name__ == "__main__":
    demo_unpack_two()
    demo_list_and_matrix()
    demo_unknown_count(StringIO("1 2\n3 4 5\n"))
