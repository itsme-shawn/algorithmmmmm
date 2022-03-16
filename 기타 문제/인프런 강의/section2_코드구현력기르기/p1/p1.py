import sys

sys.stdin = open("in1.txt", "rt")
a, b = map(int, input().split())

cnt = 0
result = -1

for i in range(1, a + 1):
    if a % i == 0:
        cnt += 1
        if cnt == b:
            result = i

print(result)
