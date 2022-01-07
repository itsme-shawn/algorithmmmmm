import sys

r, c = map(int, input().split())

puzzle = [list(sys.stdin.readline().split()[0]) for _ in range(r)]

# 낱말 기준은 연속 2개

# 가로 낱말
garo = []
for i in range(r):
    s = 0
    e = 0
    while e < c:
        if puzzle[i][e] != "#":
            if e == c:
                garo.append(puzzle[i][s:e])
            e += 1
            flag = 1  # 방금 전 # 이 아닌 문자를 지나왔다는 뜻
        else:
            if flag == 1:
                garo.append(puzzle[i][s:e])
            flag = 0
            s = e
        e += 1

print(garo)
