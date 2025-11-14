import sys
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

pre_order = []

while True:
    try:
        pre_order.append(int(read()))
    except:
        break

def dfs(start, end):
    if start >= end:
        return

    root = pre_order[start]

    # 왼쪽 서브트리가 끝나는 지점 찾기
    idx = start + 1
    while idx < end and pre_order[idx] < root:
        idx += 1
    
    # 왼쪽
    dfs(start+1, idx) # [start+1,idx)
    # 오른쪽
    dfs(idx, end)
    # 루트 출력
    print(root)

dfs(0, len(pre_order))
    
# 전위 순회 : 루트 - 왼 - 오
# 후위 순회 : 왼 - 오 - 루트
# 전위순회 결과에서 루트 / 왼 서브트리 / 오 서브트리 구분한다음 재귀