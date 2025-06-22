import sys

n = int(input())

i = 1

while True:
    tmp = 3 * i * i - 3 * i + 2
    if tmp > n:
        break
    i += 1

print(i)
