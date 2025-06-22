import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt_white, cnt_blue = 0, 0

def cut(y, x, sideLen):
    global cnt_white, cnt_blue

    color = paper[y][x]
    flag = True
    half = sideLen // 2
    
    for i in range(y, y+sideLen):
        if not flag:    # 이중for문 탈출용
            break
        for j in range(x, x+sideLen):
            if (color != paper[i][j]):
                flag = False
                cut(y, x, half)             # 왼쪽 위       (분할&정복)
                cut(y, x+half, half)        # 왼쪽 아래     (분할&정복)
                cut(y+half, x, half)        # 오른쪽 위     (분할&정복)
                cut(y+half, x+half, half)   # 오른쪽 아래   (분할&정복)
                break   # return 문을 안쓰고 break

    if flag:    # 콜스택이 다 끝나고 flag 가 False 인 상태로 여기에 들어오는 것 방지 -> 이것때문에 return 보다 break 가 좀 까다로움
        if (color == 1):
            cnt_blue += 1
        else:
            cnt_white += 1

cut(0, 0, N)
print(cnt_white)
print(cnt_blue)