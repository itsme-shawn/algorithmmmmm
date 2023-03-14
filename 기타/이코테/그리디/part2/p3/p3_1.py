# 1이 될 때까지
import sys
import time

start_time = time.time()
sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, k = map(int, read().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1
print(cnt)

# 로직 끝
print(f"실행시간 : {time.time() - start_time}\n")
