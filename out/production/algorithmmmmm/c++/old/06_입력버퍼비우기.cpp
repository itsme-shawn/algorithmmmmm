#include <bits/stdc++.h>

using namespace std;

int T;
string s;

int main() {
  cout << "getline 횟수 : ";
  cin >> T;
  string bufferflush;

  getline(cin, bufferflush);

  for (int i = 0; i < T; i++) {
    getline(cin, s);
    cout << s << '\n';
  }

  return 0;
}