import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, c = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    # print(lst)
    lst.sort()

    def check(distance, horse, lst):
        horse -= 1  # 맨 처음 말은 무조건 첫 위치에 놓을 거므로 1 빼고 시작
        last_position = lst[0]  # 처음 말은 0번 인덱스에
        for i in range(1, len(lst)):
            if lst[i] - last_position >= distance:  # 인접한 말 사이의 거리 >= 주어진 거리 : 가능케이스
                last_position = lst[i]  # 말 위치 최신화
                horse -= 1  # 말 하나 감소
            if horse == 0:  # 중간에 말을 다 배치하면 주어진 distance 로 말들을 배치시킬 수 있다는 뜻
                return True
        if horse != 0:  # 말이 남아있으면 false
            return False

    start = 1
    end = lst[-1]

    while start <= end:
        mid = (start + end) // 2
        if check(mid, c, lst):  # 현재의 거리로도 조건을 만족한다는 것은 더 거리를 늘릴 수 있다는 뜻임
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    print(ans)

    # 로직 끝

    print()
