#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n, 0);  // 벡터 값 초기화

  // 크기가 런타임 도중 결정된다면 vector 를 쓰고 범위기반 for루프를 쓰는 것은
  // 괜찮다고 함
  for (int i : a) {
    cout << i << " ";
  }

  return 0;
}