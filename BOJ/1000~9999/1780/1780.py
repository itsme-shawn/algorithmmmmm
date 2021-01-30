import sys

N = int(sys.stdin.readline())

# paper = [ [0] *N ] * N 

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
countA, countB, conutC = 0, 0, 0    # 순서대로 -1, 0, 1 종이의 갯수

def check(y, x, sideLen):
    global countA, countB, conutC

    number = paper[y][x]
    divide = sideLen // 3

    for i in range(y, y+sideLen):
        for j in range(x, x+sideLen):
            if( paper[i][j] != number ):
                check(y, x, divide)
                check(y, x+divide, divide)
                check(y, x+divide*2, divide)
                check(y+divide, x, divide)
                check(y+divide, x+divide, divide)
                check(y+divide, x+divide*2, divide)
                check(y+divide*2, x, divide)
                check(y+divide*2, x+divide, divide)
                check(y+divide*2, x+divide*2, divide)
                return
    
    if( number == -1 ):
        countA += 1
    elif( number == 0):
        countB += 1
    else:
        conutC += 1

check(0, 0, N)

print(countA)
print(countB)
print(conutC)