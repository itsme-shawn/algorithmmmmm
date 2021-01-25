import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def cut(y, x, sideLen): # sideLen : 한 변의 길이
    color = paper[y][x] # paper 의 시작점의 색을 기준색으로 뽑는다.

    half = sideLen // 2 

    for i in range(y, y+sideLen):
        for j in range(x, x+sideLen):
            if (color != paper[i][j]):      # paper 의 모든 색을 살피면서 기준색과 다르면 4등분으로 cut 해야함
                cut(y, x, half)             # 왼쪽 위       (분할&정복)
                cut(y, x+half, half)        # 왼쪽 아래     (분할&정복)
                cut(y+half, x, half)        # 오른쪽 위     (분할&정복)
                cut(y+half, x+half, half)   # 오른쪽 아래   (분할&정복)
                return  # return 문 없으면 재귀 한 사이클을 돌고나서도 이전 콜스택으로 못 빠져나옴
    
    # 결합
    if (color == 1):
        result.append(1)
    else:
        result.append(0)

cut(0, 0, N)
print(result.count(0))
print(result.count(1))