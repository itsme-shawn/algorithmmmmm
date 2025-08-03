def solution(n, q, ans):
    # 비밀코드로 가능한 정수 조합 개수 : 최대 30C5 개
    
    CODE_LEN = 5
    res = 0
    total = 0

    code = [0] * CODE_LEN
    def dfs(level, cur):
        nonlocal res
        nonlocal total
        if level == CODE_LEN:
            total += 1
            # print("code:", code)
            for i in range(len(q)):
                cnt = 0
                for num in q[i]:
                    if num in code: # 생성된 코드와 비교
                        cnt += 1
                # print(f"{code=}, {cnt=}, {ans[i]=}")
                if cnt != ans[i]:
                    break
            else:
                res += 1
            return
        for i in range(cur, n+1): # 서로 다른 정수
            code[level] = i
            dfs(level+1, i+1)
            
    
    dfs(0, 1)
    # print(f"{total=}")
    
    return res
            


# n = 10
# q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]

# ans = [2, 3, 4, 3, 3]

n = 15
q = [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]

ans = [2, 1, 3, 0, 1]

print(solution(n,q,ans))

# 정답 3