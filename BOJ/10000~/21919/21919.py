import sys

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

maxx = max(nums)

primes = [False, False] + [True] * (maxx - 1)

for i in range(2, maxx + 1):
    if primes[i]:
        for j in range(2 * i, maxx + 1, i):
            primes[j] = False

result = 1

for num in nums:
    if primes[num]:
        primes[num] = (
            False  # 한 번 들어온 소수 중복체크를 위해 primes 배열에서 num 제거
        )
        result *= num

if result == 1:
    print(-1)
else:
    print(result)
