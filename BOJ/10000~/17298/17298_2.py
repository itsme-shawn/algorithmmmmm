import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
stack = []  # 현재까지 지나온 seq 의 인덱스를 저장하는 스택 (과거를 저장)
res = [-1] * n  # 오큰수 리스트 : 일단 -1로 전체 깔아놓음
stack.append(0)  # 일단 초기값으로 0을 넣고 시작

for i in range(1, len(seq)):  # 1번인덱스부터 돌면 됨
    while stack and seq[i] > seq[stack[-1]]:  # 오큰수인 경우
        res[stack.pop()] = seq[i]
    stack.append(i)  # 현재 인덱스는 항상 스택에 저장

print(" ".join(map(str, res)))
