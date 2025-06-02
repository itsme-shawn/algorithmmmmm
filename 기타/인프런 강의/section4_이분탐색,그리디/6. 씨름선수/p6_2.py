import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n = int(read())
    person = [list(map(int, read().split())) for _ in range(n)]

    person.sort(key=lambda x: -x[0])

    cnt = 1
    max_w = person[0][1]

    for _, w in person[1:]:
        if w > max_w:
            cnt += 1
            max_w = w

    print(cnt)

    # 로직 끝
