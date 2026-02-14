"""
리스트(배열) 기본기.
- 초기화, 컴프리헨션, 얕은 복사 이슈를 한 번에 정리.
"""


def init_examples() -> None:
    arr = [0] * 5
    seq = list(range(1, 6))
    print(arr, seq)

    # 2차원 리스트 안전 초기화
    grid_ok = [[0] * 3 for _ in range(2)]
    grid_bad = [[0] * 3] * 2  # 같은 행 객체 공유
    grid_bad[0][0] = 9
    print(grid_ok)  # [[0, 0, 0], [0, 0, 0]]
    print(grid_bad)  # [[9, 0, 0], [9, 0, 0]]


def traverse_examples() -> None:
    nums = [5, 1, 7]
    for i, v in enumerate(nums):
        print(i, v)

    # 슬라이싱
    print(nums[::-1])  # 역순 복사
    print(nums[1:])  # 부분 배열


if __name__ == "__main__":
    init_examples()
    traverse_examples()
