#include <bits/stdc++.h>

using namespace std;

int n, m;
deque<int> nums;
deque<int> result;

void combination(int index, int depth) {
  if (depth == m) {
    for (int i = 0; i < m; ++i) {
      cout << result[i] << " ";
    }
    cout << endl;
    return;
  }

  for (int i = index; i < nums.size(); ++i) {
    result.push_back(nums[i]);
    combination(i + 1, depth + 1);
    result.pop_back();
  }
}

int main() {
  cin >> n >> m;

  for (int i = 0; i < n; ++i) {
    nums.push_back(i + 1);
  }
  combination(0, 0);

  return 0;
}