import sys

n = int(input())

val = 665
cnt = 0
while True:
    val += 1
    if "666" in str(val):
        cnt += 1
    if cnt == n:
        print(val)
        break
