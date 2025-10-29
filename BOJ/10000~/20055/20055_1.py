from collections import deque

import sys
read = sys.stdin.readline

n, k = map(int, read().split())
hp = deque(map(int, read().split()))
robot = deque([0]*2*n)

step = 1
res = 0
zero_cnt = 0

while True:
    # 1. 벨트+로봇 회전
    hp.appendleft(hp.pop())
    robot.appendleft(robot.pop())
    if robot[n-1]:
        robot[n-1] = 0
        
    # print(f"1 : {hp=}, {robot=}, {step=}")
    
    # 2. 로봇 이동
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and hp[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            hp[i+1] -= 1
            if hp[i+1] == 0:
                zero_cnt += 1
        
    if robot[n-1]:
        robot[n-1] = 0
    
    # print(f"2 : {hp=}, {robot=}, {step=}")
    
    # 3. 0번위치에 로봇 올림
    if hp[0]:
        robot[0] = 1
        hp[0] -= 1
        if hp[0] == 0:
            zero_cnt += 1
         
    # print(f"3 : {hp=}, {robot=}, {step=}")
    
    if zero_cnt >= k:
        res = step
        break
    else:
        step += 1

print(res)