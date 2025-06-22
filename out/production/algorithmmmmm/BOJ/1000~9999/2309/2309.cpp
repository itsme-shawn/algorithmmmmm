#include <bits/stdc++.h>

using namespace std;

pair<int, int> save;

int main() {
  vector<int> heights;
  vector<int> result;
  int num = 0;
  int total = 0;

  for (int i = 0; i < 9; i++) {
    cin >> num;
    heights.push_back(num);
  }

  total = accumulate(heights.begin(), heights.end(), 0);

  int target = total - 100;
  bool flag = false;

  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 9; j++) {
      if (heights[i] + heights[j] == target) {
        flag = true;
        save = {i, j};
        break;
      }
    }
    if (flag == true) break;
  }

  for (int i = 0; i < 9; i++) {
    if (save.first == i || save.second == i) continue;
    result.push_back(heights[i]);
  }

  sort(result.begin(), result.end());

  for (int i = 0; i < 7; i++) {
    cout << result[i] << '\n';
  }

  return 0;
}