// boj 15649

#include <bits/stdc++.h>

using namespace std;

int result[20];
int N, S;
int cnt;

void dfs(int depth, int total) {
  if (depth == N) {
    if (total == S) {
      cnt++;
    }
    return;
  }

  dfs(depth + 1, total);
  dfs(depth + 1, total + result[depth]);
}

int main() {
  cin >> N >> S;

  for (int i = 0; i < N; i++) {
    cin >> result[i];
  }

  dfs(0, 0);

  // 공집합인 경우가 있으니 S 가 0 일 때는 cnt 에서 1 빼줘야함
  if (S == 0) {
    cnt--;
  }

  cout << cnt;

  return 0;
}