import sys
from collections import deque

read = sys.stdin.readline
 
wheels = [deque(map(int,read().rstrip())) for _ in range(4)]
k = int(read())
cmd = [list(map(int, read().split())) for _ in range(k)]


def turn(wheel:deque, d):
    if d == -1: # 반시계
        wheel.append(wheel.popleft())
    if d == 1: # 시계
        wheel.appendleft(wheel.pop())

for num, d in cmd:
    turn_dirctions = [0] * len(wheels)
    turn_dirctions[num-1] = d
    # 맞닿아있는 인덱스 : -2, 2
    
    # 맞닿은 극이 다르면 서로 반대방향으로 회전
    # 맞닿은 극이 같으면 회전 X
    
    # 기준바퀴의 인덱스 : num-1
    # 기준바퀴로부터 왼쪽으로 진행
    for i in range(num-1,0,-1):
        # 맞닿은 극 확인
        left = wheels[i][-2]
        right = wheels[i-1][2]
        # print("left,right", left, right)
        if (left != right):
            turn_dirctions[i-1] = -turn_dirctions[i]
        
        
    # 기준바퀴로부터 오른쪽으로 진행
    for i in range(num-1,len(wheels)-1):
        # 맞닿은 극 확인
        right = wheels[i][2]
        left = wheels[i+1][-2]
        # print("left,right", left, right)
        if (left != right):
            turn_dirctions[i+1] = -turn_dirctions[i]
    
    for i,td in enumerate(turn_dirctions):
        turn(wheels[i], td)
        
ans = 0
if wheels[0][0] == 1:
    ans += 1
if wheels[1][0] == 1:
    ans += 2
if wheels[2][0] == 1:
    ans += 4
if wheels[3][0] == 1:
    ans += 8
    
print(ans)

    
    





'''
10101111
01111101
11001110
00000010
2
3 -1
1 1
'''