"""
얕은 복사 vs 깊은 복사, 2차원 리스트 초기화 주의.
코딩테스트에서 자료구조 스냅샷을 보관할 때 발생하는 사이드이펙트를 방지한다.
"""

import copy


def shallow_vs_deep() -> None:
    base = [0, [1, 2]]
    shallow = base.copy()  # 혹은 copy.copy(base)
    deep = copy.deepcopy(base)

    base[0] = "A"
    base[1][0] = "B"

    print("orig :", base)  # ['A', ['B', 2]]
    print("shallow shares inner :", shallow)  # [0, ['B', 2]]
    print("deep keeps snapshot  :", deep)  # [0, [1, 2]]


def build_grid_wrong() -> None:
    """
    리스트 곱셈은 내부 리스트를 같은 객체로 복사한다.
    한 칸을 바꾸면 같은 행이 모두 바뀌어 버림.
    """

    grid = [[0, 0, 0]] * 2
    grid[0][0] = "X"
    print(grid)  # [['X', 0, 0], ['X', 0, 0]]


def build_grid_right() -> None:
    """컴프리헨션을 쓰면 행마다 별도 객체 생성"""
    grid = [[0, 0, 0] for _ in range(2)]
    grid[0][0] = "X"
    print(grid)  # [['X', 0, 0], [0, 0, 0]]


if __name__ == "__main__":
    shallow_vs_deep()
    build_grid_wrong()
    build_grid_right()
