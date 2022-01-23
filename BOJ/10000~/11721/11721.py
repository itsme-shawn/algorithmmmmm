import sys

word = sys.stdin.readline().rstrip()
temp = ""
cnt = 0
for i in range(len(word)):
    if cnt <= 9:  # 9개까지는 입력받고 cnt 증가
        temp += word[i]
        cnt += 1
    if cnt == 10:  # 10개 되면 출력하고, temp,cnt 초기화
        print(temp)
        temp = ""
        cnt = 0
print(temp)  # 나머지 출력
