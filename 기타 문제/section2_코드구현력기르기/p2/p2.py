import sys

sys.stdin = open("in5.txt", "rt")
T = int(input())


for _ in range(T):
    N, s, e, k = map(int, input().split())
    lst = list(map(int, sys.stdin.readline().split()))
    lst = lst[s - 1 : e]
    lst.sort()
    print(lst[k - 1])
