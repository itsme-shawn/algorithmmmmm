"""
백트래킹으로 순열 생성.
itertools.permutations 대비 동작 이해용 예제.
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    used = [False] * n
    path: List[int] = []
    res: List[List[int]] = []

    def dfs() -> None:
        if len(path) == n:
            res.append(path[:])
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


if __name__ == "__main__":
    print(permute([1, 2, 3]))
