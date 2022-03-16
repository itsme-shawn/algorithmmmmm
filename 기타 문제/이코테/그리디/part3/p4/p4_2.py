import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n = int(read())
coins = list(map(int, read().split()))
coins.sort()

target = 1  # 검증하고자 하는 금액
for coin in coins:
    # target 금액을 만들 수 있는지 검증
    if target < coin:  # 이럴 경우 target 금액을 못 만듦
        break
    # target 값 갱신
    target += coin  # 다음 루프의 target
print(target)
