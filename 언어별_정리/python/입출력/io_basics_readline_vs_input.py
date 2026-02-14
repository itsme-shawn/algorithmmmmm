"""
입력 기본기 정리.
- input() 은 내부에서 strip 을 해주지만 느림.
- sys.stdin.readline() 은 빠르지만 개행 문자가 붙으므로 rstrip() 으로 제거.
아래 예시는 StringIO 로 입력을 흉내 내어 즉시 실행해도 멈추지 않는다.
"""

import sys
from io import StringIO


def input_vs_readline() -> None:
    fake = StringIO("hello\n42\n")
    original = sys.stdin
    try:
        sys.stdin = fake
        s = input()  # 개행 제거됨
        n = int(sys.stdin.readline())  # 개행 포함 -> int 로 캐스팅하여 제거
    finally:
        sys.stdin = original
    print(f"input() length={len(s)}, readline int={n}")


def strip_newline() -> None:
    fake = StringIO("abc\n")
    line_with_newline = fake.readline()
    fake.seek(0)
    line_stripped = fake.readline().rstrip()
    print(len(line_with_newline), len(line_stripped))  # 4, 3


if __name__ == "__main__":
    input_vs_readline()
    strip_newline()
