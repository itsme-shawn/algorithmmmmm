"""
2차원/3차원 리스트 입력 예시.
리스트 컴프리헨션으로 빠르게 초기화하고, 입력 크기만큼 곱셈을 쓰지 않는다.
"""

from io import StringIO


def read_grid(fake: StringIO) -> None:
    """
    N*M 격자 입력.
    예: 2 3\n1 2 3\n4 5 6\n
    """

    n, m = map(int, fake.readline().split())
    grid = [list(map(int, fake.readline().split())) for _ in range(n)]
    print(n, m, grid)  # 2 3 [[1,2,3],[4,5,6]]


def read_3d(fake: StringIO) -> None:
    """
    H개의 층, 각 층은 N*M 격자.
    예: 2 2 2\n1 2\n3 4\n5 6\n7 8\n
    """

    h, n, m = map(int, fake.readline().split())
    box = [
        [list(map(int, fake.readline().split())) for _ in range(n)] for _ in range(h)
    ]
    print(box)  # [[[1,2],[3,4]], [[5,6],[7,8]]]


if __name__ == "__main__":
    read_grid(StringIO("2 3\n1 2 3\n4 5 6\n"))
    read_3d(StringIO("2 2 2\n1 2\n3 4\n5 6\n7 8\n"))
