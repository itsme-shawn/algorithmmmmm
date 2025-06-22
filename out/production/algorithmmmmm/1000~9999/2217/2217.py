import sys

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))
ropes.sort(reverse=True)

maxx = 0
cnt = 0  # 현재 로프개수
for x in ropes:
    cnt += 1
    temp = x * cnt
    if temp >= maxx:
        maxx = temp
    # else 에서 break 해주면 안 됨! 반례 있음
    # else:
    #     break
print(maxx)
