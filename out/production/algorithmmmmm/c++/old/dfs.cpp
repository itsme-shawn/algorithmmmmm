#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second  // pair 에서 first, second 를 줄여 쓰기 위해 사용

int board[502][502] = {
    {1, 1, 1, 0, 1, 0, 0, 0, 0, 0},
    {1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
    {1, 1, 1, 0, 1, 0, 0, 0, 0, 0},
    {1, 1, 0, 0, 1, 0, 0, 0, 0, 0},
    {0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};  // 1이 파란 칸, 0이 빨간 칸에 대응

bool vis[502][502];         // 방문체크 배열
int n = 7, m = 10;          // n : 행의 수 , m : 열의 수
int dx[4] = {1, 0, -1, 0};  // 행 방향
int dy[4] = {0, 1, 0, -1};  // 열 방향

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  stack<pair<int, int>> S;

  vis[0][0] = 1;  // (0,0) 방문 표시
  S.push({0, 0});

  while (!S.empty()) {
    pair<int, int> cur = S.top();
    S.pop();

    cout << '(' << cur.X << ", " << cur.Y << ") -> ";

    for (int d = 0; d < 4; d++) {
      int nx = cur.X + dx[d];
      int ny = cur.Y + dy[d];

      if (0 <= nx && nx < n && 0 <= ny && ny < m)
        if (vis[nx][ny] == 0 && board[nx][ny] == 1) {
          vis[nx][ny] = 1;
          S.push({nx, ny});
        }
    }
  }

  return 0;
}