#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> nums;
vector<int> result;

void dfs(int depth) {
  if (depth == m) {
    for (int i = 0; i < m; i++) {
      cout << result[i] << " ";
    }
    cout << '\n';
    return;
  }

  else {
    for (int i = 0; i < n; i++) {
      result[depth] = nums[i];
      dfs(depth + 1);
    }
  }
}

int main() {
  cin >> n >> m;

  // nums 와 result 벡터 크기 재설정
  nums.resize(n);
  result.resize(m);

  for (int i = 0; i < n; i++) {
    nums[i] = i + 1;
  }

  dfs(0);

  return 0;
}