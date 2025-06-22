# 실전) 왕실의 나이트
import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, read().split())
x, y, d = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1  # 첫 위치 방문처리
cnt = 1  # 첫 위치 카운트

while True:
    for i in range(4):
        # 반시계
        nx = x + dx[(d - i - 1) % 4]
        ny = y + dy[(d - i - 1) % 4]
        if board[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            x, y = nx, ny  # 위치 갱신
            d = (d - i - 1) % 4  # 방향 갱신
            cnt += 1
            break
    else:  # for 문 4번에서 한 번도 안걸렸을 때 => 네 방향 모두 이미 가본 칸 or 바다
        # 방향 유지한 채 뒤로 후진
        nx = x + dx[(d + 2) % 4]
        ny = y + dy[(d + 2) % 4]
        if board[nx][ny] == 1:  # 뒤쪽이 바다면 종료
            break
        else:  # 뒤쪽이 바다가 아니면
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
            x, y = nx, ny

print(cnt)
