#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
int board[502][502];
bool vis[502][502];
int n, m;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs(int i, int j) {
  queue<pair<int, int>> Q;
  vis[i][j] = 1;
  Q.push({i, j});

  int area = 0;  // 그림의 넓이

  while (!Q.empty()) {
    area++;
    auto cur = Q.front();
    Q.pop();

    for (int d = 0; d < 4; d++) {
      int nx = cur.X + dx[d];
      int ny = cur.Y + dy[d];

      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (!vis[nx][ny] && board[nx][ny]) {
          vis[nx][ny] = 1;
          Q.push({nx, ny});
        }
      }
    }
  }

  return area;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
    }

  int mx = 0;   // 그림의 최댓값
  int num = 0;  // 그림 개수
  int cur_area = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (board[i][j] == 0 || vis[i][j]) continue;

      // (i,j) 에서 bfs 시작
      num++;
      cur_area = bfs(i, j);
      mx = max(mx, cur_area);
    }
  }

  cout << num << '\n' << mx;

  return 0;
}