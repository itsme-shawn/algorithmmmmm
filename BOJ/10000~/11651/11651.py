import sys

N = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sortedList = sorted(lst, key=lambda x: (x[1], x[0]))

for item in sortedList:
    print(item[0], item[1])
