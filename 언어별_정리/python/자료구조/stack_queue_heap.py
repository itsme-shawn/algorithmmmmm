"""
스택, 큐, 힙 핵심 사용법 정리.
리스트 스택, deque 큐, heapq 최소/최대 힙.
"""

from collections import deque
import heapq


def stack_example() -> None:
    stack = []
    for v in [1, 2, 3]:
        stack.append(v)
    while stack:
        print(stack.pop())  # LIFO: 3 2 1


def queue_example() -> None:
    q = deque()
    for v in [1, 2, 3]:
        q.append(v)
    while q:
        print(q.popleft())  # FIFO: 1 2 3


def min_max_heap_example() -> None:
    nums = [7, 2, 9, 4]

    # min-heap
    minh = nums[:]
    heapq.heapify(minh)
    print([heapq.heappop(minh) for _ in range(len(minh))])  # 2 4 7 9

    # max-heap: 값에 -1 곱해 활용
    maxh = [-x for x in nums]
    heapq.heapify(maxh)
    print([-heapq.heappop(maxh) for _ in range(len(maxh))])  # 9 7 4 2


if __name__ == "__main__":
    stack_example()
    queue_example()
    min_max_heap_example()
