"""
여러 줄 입력 받기 패턴.
- 줄 수 N 이 주어질 때: 반복문 + readline
- 줄 수 미정일 때: for line in sys.stdin 또는 sys.stdin.read()
"""

import sys
from io import StringIO


def read_n_lines(fake: StringIO) -> None:
    n = int(fake.readline())
    lines = [fake.readline().rstrip() for _ in range(n)]
    print(lines)  # ['alpha', 'beta', 'gamma']


def read_until_eof(fake: StringIO) -> None:
    """EOF 까지 모든 줄 -> 리스트"""
    lines = [line.rstrip() for line in fake if line.strip()]
    print(lines)  # ['1 2', '3 4 5']


def read_all_then_split(fake: StringIO) -> None:
    """
    sys.stdin.read() 로 몽땅 읽은 뒤 공백 기준 분리.
    입력 크기가 크고 줄 구분이 중요치 않을 때 빠르다.
    """

    tokens = fake.read().split()
    print(tokens)  # ['7', '8', '9']


if __name__ == "__main__":
    read_n_lines(StringIO("3\nalpha\nbeta\ngamma\n"))
    read_until_eof(StringIO("1 2\n3 4 5\n"))
    read_all_then_split(StringIO("7 8 9"))
