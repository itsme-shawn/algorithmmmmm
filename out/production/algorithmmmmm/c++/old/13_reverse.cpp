#include <bits/stdc++.h>

using namespace std;

int main() {
  string a = "0123456";
  reverse(a.begin(), a.end());
  cout << a << '\n';  // 6543210

  reverse(a.begin(), a.end());
  cout << a << '\n';  // 0123456

  reverse(a.begin() + 3, a.end() - 1);
  cout << a << '\n';  // 0125436

  return 0;
}