import sys
read = sys.stdin.readline

def solution():
    N = int(read())
    nums = [0] + list(map(int, read().split()))
    M = int(read())
    queries = [list(map(int, read().split())) for _ in range(M)]

    dp = [[False]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][i] = True
    
    for j in range(1, N):
        if nums[j] == nums[j+1]:
            dp[j][j+1] = True

    length = 0

    for length in range(3, len(nums)+1): # 길이
        for start in range(1, N-length+2): # N = 5, length = 3
            end = start + length - 1
            if nums[start] == nums[end] and dp[start+1][end-1]:
                dp[start][end] = True

    # for row in dp:
    #     print(row)

    for query in queries:
        if dp[query[0]][query[1]]:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()