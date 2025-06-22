import sys

read = sys.stdin.readline

x = int(read())
i = 1
while True:
    if (i * i - i + 2) // 2 <= x <= (i * (i + 1)) // 2:
        break
    else:
        i += 1

# group : 그룹번호, cnt : 그룹내에서 몇번째수
group, cnt = i, x - (i * i - i + 2) // 2 + 1

if group % 2 == 0:
    print(f"{cnt}/{group - cnt + 1}")
else:
    print(f"{group - cnt + 1}/{cnt}")
