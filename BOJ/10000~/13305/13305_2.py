import sys

read = sys.stdin.readline

n = int(read())
dist = list(map(int, read().split()))
price = list(map(int, read().split()))

total = price[0] * dist[0]
cur_price = price[0]
for i in range(1, len(dist)):
    cur_price = min(cur_price, price[i])
    total += cur_price * dist[i]

print(total)
