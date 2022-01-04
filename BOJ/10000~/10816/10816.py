import bisect
import sys

N = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
findList = list(map(int, sys.stdin.readline().split()))


# 각 카드별 개수 조사
count = {}
for card in cardList:
    try:
        count[card] += 1
    except:
        count[card] = 1

for num in findList:
    try:
        print(count[num], end=" ")
    except:
        print(0, end=" ")
