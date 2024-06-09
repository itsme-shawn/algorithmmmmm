#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int freq[10];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int a, b, c;

  cin >> a >> b >> c;

  ll result = a * b * c;

  // long long 타입을 string 으로 변환
  string str = to_string(result);

  for (auto s : str) {
    freq[s - '0']++;
  }

  for (int i = 0; i < 10; i++) {
    cout << freq[i] << '\n';
  }
}