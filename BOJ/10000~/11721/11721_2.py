import sys

word = sys.stdin.readline().rstrip()
for i in range(0, len(word), 10):  # i 는 10씩 증가함
    print(word[i : i + 10])  # 10개씩 슬라이싱해서 출력
