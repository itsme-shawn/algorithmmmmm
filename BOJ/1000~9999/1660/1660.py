import sys

read = sys.stdin.readline

N = int(read())

cur = 1
last = 1
tri = [cur] # [1,3,6,10,15...]

BULLET_MAX = 300_000

while cur <= BULLET_MAX:
    last += 1
    cur += last
    tri.append(cur)
    
dp = [0] * BULLET_MAX
# dp[i] : i개의 대포알로 만들 수 있는 사면체의 최소 개수

idx = 0

# 사면체 수 생성
tetra = []
current_tetra = 0
for t_num in tri:
    current_tetra += t_num
    if current_tetra > BULLET_MAX:
        break
    tetra.append(current_tetra)
    
# dp[i] : i개의 대포알로 만들 수 있는 사면체의 최소 개수
dp = [float('inf')] * (N + 1)

# 사면체 수 자체는 1개의 사면체로 만들 수 있으므로 1로 초기화
for t_val in tetra:
    if t_val <= N:
        dp[t_val] = 1 # dp[1], dp[4], dp[10], dp[20].. 등이 1
        
# DP를 사용하여 최소 개수 계산
for i in range(1, N + 1):
    # i개의 대포알로 사면체를 만드는 경우를 탐색
    # 현재 i개의 대포알에서 이전에 계산된 사면체 값을 빼고 남은 대포알로 만들 수 있는
    # 사면체의 개수 + 1 (현재 만든 사면체) 중 최솟값을 찾는다.
    for t_val in tetra:
        if i - t_val >= 0: # 현재 대포알 개수에서 사면체 하나를 만들 수 있는 경우
            # dp[i]는 기존 값과, (i - t_val)개의 대포알로 만든 사면체 개수 + 1 중 최솟값
            dp[i] = min(dp[i], dp[i - t_val] + 1)
        else:
            break

print(dp[N])