import sys
read = sys.stdin.readline

N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]
minn = float('inf')

# 가능한 모든 기준점 (x, y)와 d1, d2를 시도
for x in range(N - 1):
    for y in range(1, N - 1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if not (0<=x<x+d1+d2 and x+d1+d2<N and 0<=y-d1<y and y<y+d2<N):
                    break

                cnt = [0, 0, 0, 0, 0]  # 각 선거구 인구 합계

                # 5번 선거구 인구 합 계산
                # (경계선 안쪽 포함)
                for l in range(d2):
                    for k in range(d1 + 1):
                        cnt[0] += graph[x + k + l][y - k + l]
                    for k in range(d1):
                        cnt[0] += graph[x + 1 + k + l][y - k + l]
                for k in range(d1 + 1):
                    cnt[0] += graph[x + d2 + k][y + d2 - k]

                # 1번/4번 선거구 인구 합
                for k in range(d1 + 1):
                    for i in range(x + k):
                        cnt[1] += graph[i][y - k]  # 1번
                    for i in range(x + d1 + d2 + 1 - k, N):
                        cnt[4] += graph[i][y - d1 + d2 + k]  # 4번

                # 2번/3번 선거구 인구 합
                for l in range(d2 + 1):
                    for j in range(y + 1 + l, N):
                        cnt[2] += graph[x + l][j]  # 2번
                    for j in range(y - d1 + l):
                        cnt[3] += graph[x + d1 + l][j]  # 3번

                # 나머지 영역 채우기
                for i in range(x + d1):
                    for j in range(y - d1):
                        cnt[1] += graph[i][j]  # 1번
                for i in range(x):
                    for j in range(y + 1, N):
                        cnt[2] += graph[i][j]  # 2번
                for i in range(x + d1 + d2 + 1, N):
                    for j in range(y - d1 + d2):
                        cnt[3] += graph[i][j]  # 3번
                for i in range(x + d2 + 1, N):
                    for j in range(y + d2 + 1, N):
                        cnt[4] += graph[i][j]  # 4번

                # 최대 인구수 - 최소 인구수의 차이
                minn = min(minn, max(cnt) - min(cnt))

print(minn)
