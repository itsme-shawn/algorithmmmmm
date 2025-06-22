price = int(input())
change = 1000 - price
lst = [500, 100, 50, 10, 5, 1]
cnt = 0
for x in lst:
    cnt += change // x
    change %= x

print(cnt)
