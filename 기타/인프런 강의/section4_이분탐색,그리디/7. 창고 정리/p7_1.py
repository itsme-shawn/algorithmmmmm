import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    L = int(read())
    boxes = list(map(int, read().split()))
    M = int(read())
    dic = dict()

    for idx, height in enumerate(boxes):
        dic[idx] = height

    for _ in range(M):
        maxx = max(dic.items(), key=lambda x: x[1])
        minn = min(dic.items(), key=lambda x: x[1])

        dic[maxx[0]] -= 1
        dic[minn[0]] += 1

    max_height = max(dic.values())
    min_height = min(dic.values())

    print(max_height - min_height)

    # 로직 끝

    print()
