# 시각
import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n = int(read())
hour, minute, sec = 0, 0, 0
cnt = 0

while hour < n + 1:
    if "3" in str(hour) or "3" in str(minute) or "3" in list(str(sec)):
        cnt += 1
    if sec == 59:
        sec = 0
        if minute == 59:
            minute = 0
            hour += 1
        else:
            minute += 1
    else:
        sec += 1


print(cnt)
