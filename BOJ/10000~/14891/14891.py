import sys

read = sys.stdin.readline

wheel = [list(map(int,list(read().rstrip()))) for _ in range(4)]
K = int(read())
cmd = [list(map(int, read().split())) for _ in range(K)]

