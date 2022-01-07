import sys

n = int(input())
lst = [list(sys.stdin.readline().split()) for _ in range(n)]

lst.sort(key=lambda x: int(x[0]))
for row in lst:
    age, name = int(row[0]), row[1]
    print(age, name)
