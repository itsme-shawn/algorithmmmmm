// boj 15649

#include <bits/stdc++.h>

using namespace std;

int result[8];
bool vis[9];
int n, m;

void dfs(int depth) {
  if (depth == m) {
    for (int i = 0; i < m; i++) {
      cout << result[i] << " ";
    }
    cout << '\n';

    return;
  }

  for (int j = 1; j <= n; j++) {
    if (vis[j] == false) {
      vis[j] = true;
      result[depth] = j;
      dfs(depth + 1);
      vis[j] = false;
    }
  }
}

int main() {
  cin >> n >> m;

  dfs(0);

  return 0;
}