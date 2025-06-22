import sys

n = int(input())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:  # 현재 문자와 다음 문자가 다를 때
            if word[i] in word[i + 1 :]:  # 현재 문자가 뒷 문자열에 있으면 그룹단어가 아님
                break
    else:  # break 안걸렸다면 그룹단어임
        cnt += 1
print(cnt)
