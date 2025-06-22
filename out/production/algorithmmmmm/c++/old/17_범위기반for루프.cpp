#include <bits/stdc++.h>

using namespace std;

int main() {
  vector<int> a = {1, 2, 3};

  for (int b : a) {
    cout << b << " ";  // 1 2 3
  }

  cout << "\n";

  for (int i = 0; i < a.size(); i++) {
    cout << a[i] << " ";  // 1 2 3
  }

  return 0;
}