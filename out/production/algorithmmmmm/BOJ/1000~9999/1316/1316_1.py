import sys
from collections import Counter

n = int(input())
cnt = 0

for _ in range(n):
    string = list(sys.stdin.readline().rstrip())
    # split() 마지막에 하면 안되는 이유? => 노션에 정리

    # 빈도수 딕셔너리 생성 (Counter 이용)
    alpha = dict(Counter(string))

    for i in range(len(string)):
        if alpha[string[i]] >= 2:
            if string[i] != string[i + 1]:
                break
            alpha[string[i]] -= 1
    else:
        cnt += 1

print(cnt)
