import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
coin.sort(reverse=True)
cnt = 0

for idx in range(len(coin)):
    if K // coin[idx] >= 1:
        cnt += K // coin[idx]
        K %= coin[idx]
        if K == 0:
            break

print(cnt)
