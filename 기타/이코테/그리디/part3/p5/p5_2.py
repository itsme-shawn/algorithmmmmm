import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, m = map(int, read().split())
weights = list(map(int, read().split()))
balls = [0] * (m + 1)

# 무게 당 볼링공 개수 저장
for w in weights:
    balls[w] += 1

res = 0
for i in range(1, m + 1):  # balls 리스트 순회
    n -= balls[i]  # 전체 볼링공 개수에서 현재 무게 볼링공 개수 빼기
    res += balls[i] * n  # (현재 무게의 볼링공 개수) * (B가 가능한 경우의 수)

print(res)
