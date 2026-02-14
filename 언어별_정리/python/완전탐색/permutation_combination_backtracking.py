lst = [1,2,3,4,5]
num = 2

# 순열 (중복없음)
# 시간복잡도 개선 위해 visited 배열 사
def permutation_dfs(L, cur, visited):
    global cnt
    if L == num:
        print(" ".join(map(str, cur)))
        cnt += 1
        # return
    else:
        for i in range(len(lst)):
            if not visited[i]:
                visited[i] = True
                cur.append(lst[i])
                permutation_dfs(L+1, cur, visited)
                cur.pop()
                visited[i] = False
            
# 중복순열
def D_permutation_dfs(L,cur):
    global cnt
    if L == num:
        print(" ".join(map(str, cur)))
        cnt += 1
    else:
        for i in range(len(lst)):
            cur.append(lst[i])
            D_permutation_dfs(L+1, cur)
            cur.pop()

# 조합
def combination_dfs(L, cur):
    global cnt
    if L == num:
        print(" ".join(map(str,cur)))
        cnt += 1
    else:
        for i in range(len(lst)):
            if not cur or cur[-1]<lst[i]:
                cur.append(lst[i])
                combination_dfs(L+1, cur)
                cur.pop()
        

# 중복조합
def D_combination_dfs(L, cur):
    global cnt
    if L == num:
        print(" ".join(map(str,cur)))
        cnt += 1
    else:
        for i in range(len(lst)):
            if not cur or cur[-1]<=lst[i]:
                cur.append(lst[i])
                D_combination_dfs(L+1, cur)
                cur.pop()

####

# 순열 실행
print("순열")
cnt = 0
visited = [0] * len(lst)
permutation_dfs(0, [], visited)
print(cnt)


# 중복순열 실행
print("중복순열")
cnt = 0
D_permutation_dfs(0, [])
print(cnt)

# 조합 실행
print("조합")
cnt = 0
combination_dfs(0, [])
print(cnt)


# 중복조합 실행
print("중복조합")
cnt = 0
D_combination_dfs(0, [])
print(cnt)