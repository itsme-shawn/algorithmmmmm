import sys

read = sys.stdin.readline

n = int(read())

# 리스트 크기를 가변적으로 잡으면 안 됨. 예를 들어 n=1 일 때 start[2]가 없기 때문에 인덱스에러발생
# stair = []
# for _ in range(n):
#     stair.append(int(read()))
# stair.insert(0, 0)

# 문제 조건보다 1 크게 리스트 고정크기 생성
stair = [0] * 301
for i in range(1, n + 1):
    stair[i] = int(read())

dp = [0] * 301
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[n])
