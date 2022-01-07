import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    # i : 시작 포인터
    for i in range(n):
        mySum = lst[i]  # mySum 에 시작포인터가 가리키는 값 대입
        if mySum > m:  # mySum > m 이면 continue
            continue
        elif mySum == m:  # mySum == m 이면 카운트 하나 늘리고 continue
            cnt += 1
            continue
        else:
            # mySum < m 일 때만 이 for문 실행
            # j : 끝 포인터
            for j in range(i + 1, n):
                mySum += lst[j]
                # 아래는 위와 같은 로직 (다만 이번엔 break 로 이 for문을 탈출해줘야함)
                if mySum > m:
                    break
                elif mySum == m:
                    # j 의 위치를 계속 홀딩하고 있으면 됨
                    cnt += 1
                    break

    print(cnt)

    # 로직 끝

    print()
