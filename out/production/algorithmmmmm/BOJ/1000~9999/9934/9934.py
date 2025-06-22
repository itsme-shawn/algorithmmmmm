import heapq as hq
import sys

read = sys.stdin.readline

# left -> root -> right

k = int(read())
visit = list(map(int, read().split()))
ans = []


# def rec(start, end):
#     mid = (start + end) // 2
#     ans.append(visit[mid])
#     print("ans :", ans)
#     if start == end:
#         return
#     rec(start, mid - 1)
#     rec(mid + 1, end)


# rec(0, 2**k - 2)


"""
k = 3
0 1 2 3 4 5 6
1 6 4 3 5 2 7

3 / 1 5 / 0 2 4 6

(2**3-2)/2


k = 4
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 

7 / 3 11 / 1 5 9 13 / 0 2 4 6 8 10 12 14

(2**4)

"""
