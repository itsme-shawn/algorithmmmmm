#include <bits/stdc++.h>

using namespace std;

int n, m;
deque<int> nums;
deque<int> result;
vector<bool> used;  // visited
int cnt = 0;

void permutation(int depth) {
  if (depth == m) {
    for (int i = 0; i < m; i++) {
      cout << result[i] << " ";
    }
    cout << '\n';

    cnt++;

    return;
  }

  for (int i = 0; i < n; i++) {
    if (!used[i]) {
      used[i] = true;
      result.push_back(nums[i]);
      permutation(depth + 1);
      used[i] = false;
      result.pop_back();
    }
  }
}

int main() {
  cin >> n >> m;

  for (int i = 1; i < n + 1; i++) {
    nums.push_back(i);
  }

  used.assign(n, false);

  permutation(0);

  cout << cnt << '\n';

  return 0;
}
