import sys

sys.stdin = open("in5.txt", "rt")

n = int(input())
lst = list(map(int, input().split()))

score = 0
cnt = 0  # 연속정답수 카운트

for item in lst:
    if item == 1:
        cnt += 1
    else:
        cnt = 0
    score += cnt

print(score)
