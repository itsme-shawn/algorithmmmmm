import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    res = []
    
    def dfs(v):
        if v==n:
            if res:
                print(" ".join(map(str,res)))
            return
        # 추가
        res.append(v+1)
        dfs(v+1)
        res.pop()
        # 추가 안 하는 경우
        dfs(v+1)
    
    dfs(0)
    
    

    # 로직 끝
