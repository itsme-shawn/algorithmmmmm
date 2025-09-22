# 미완성

import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
durable = list(map(int, read().split()))
belt = deque([[0] * 2 for _ in range(2 * n)])
for i in range(2 * n):
    belt[i][0] = durable[i]

# print(belt) [[1, 0], [2, 0], [1, 0], [2, 0], [1, 0], [2, 0]]
# 0번째 : 내구도 , 1번째 : 로봇 여부

zero_cnt = 0
stage = 1

# 올리는 칸에 로봇 올리기
# if belt[0][0] > 0:
#     belt[0][0] -= 1
#     belt[0][1] = 1  # 로봇 올리기
#     if belt[0][0] == 0:
#         zero_cnt += 1

while True:
    # 벨트 회전
    belt.rotate(1)

    # 회전 시에 내리는 위치에 로봇이 있다면? => 로봇 떨굼
    if belt[n - 1][1] == 1:
        belt[n - 1][1] = 0  # 로봇 떨굼

    # 가장 먼저 벨트에 올라간 로봇 부터 이동
    for i in range(n - 2, -1, -1):  # 내리는 위치 제외
        if (
            belt[i][1] == 1 and belt[i + 1][0] > 0 and belt[i + 1][1] == 0
        ):  # 로봇 존재 and 다음 위치 내구도 > 0 and 다음 위치 로봇없음
            # 로봇 이동
            belt[i + 1][0] -= 1  # 내구도 감소
            belt[i + 1][1] = 1  # 로봇 할당
            if belt[i + 1][0] == 0:
                zero_cnt += 1

    if belt[0][0] > 0:
        belt[0][0] -= 1
        belt[0][1] = 1  # 로봇 올리기
        if belt[0][0] == 0:
            zero_cnt += 1

    if zero_cnt >= k:
        break

    stage += 1

print(stage)
