import sys

read = sys.stdin.readline

s = list(map(int, read().rstrip()))
cnt_zero, cnt_one = 0, 0  # 0,1 그룹 개수
before = s[0]  # before 초기값 : 첫 숫자
if before == 0:
    cnt_zero += 1
elif before == 1:
    cnt_one += 1

for num in s[1:]:  # 인덱스 1부터 시작
    if (before, num) == (0, 1):
        cnt_one += 1
    elif (before, num) == (1, 0):
        cnt_zero += 1
    before = num  # before 에 num 저장
print(min(cnt_zero, cnt_one))
