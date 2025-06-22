#include <bits/stdc++.h>

using namespace std;

int main() {
  int n = 5;
  int a[5] = {200, 300, 1, 2, 3};
  vector<int> v;

  for (int i = 0; i < n; i++) {
    v.push_back(a[i]);
  }

  sort(v.begin(), v.end());  // 오름차순 정렬

  int cnt = 0;

  do {
    for (int i = 0; i < 2; i++) {
      cout << v[i] << " ";
    }
    cout << endl;
    cnt += 1;

  } while (next_permutation(v.begin(), v.end()));

  cout << cnt << endl;

  return 0;
}