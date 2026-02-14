#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// 비교 함수
bool compare(const vector<int>& a, const vector<int>& b) {
  // 첫 번째 값 우선 비교해서 내림차순 정렬
  if (a[0] != b[0]) {
    return a[0] > b[0];
  }
  // 첫 번째 값이 같은 경우에는 두 번째 값이 오름차순 정렬
  else {
    return a[1] < b[1];
  }
}

int main() {
  // 입력
  int n;
  cin >> n;

  vector<vector<int>> lst(n, vector<int>(2));
  for (int i = 0; i < n; ++i) {
    cin >> lst[i][0] >> lst[i][1];
  }

  // 정렬
  sort(lst.begin(), lst.end(), compare);

  // 출력
  int selected_height = -1;
  int selected_weight = -1;
  int cnt = 0;

  for (const auto& v : lst) {
    if (v[1] > selected_weight) {
      selected_weight = v[1];
      cnt++;
    }
  }

  cout << cnt << endl;

  return 0;
}
