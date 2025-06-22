#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  string str1;
  string str2;

  // 1. cin -> cin
  // 다음 cin이 버퍼의 공백 및 개행문자 무시하므로 버퍼 비워줄 필요가 없다
  cin >> str1;
  cin >> str2;
  cout << str1 << " " << str2 << "\n";

  // 2. cin -> getline
  // 다음 getline은 전 버퍼의 공백 및 개행문자를 입력받으므로 버퍼 비워줘야 한다
  cin >> str1;
  cin.ignore();  // 버퍼의 '\n' 비워주기
  getline(cin, str2);
  cout << str1 << " " << str2 << "\n";

  // 3. getline -> getline 또는 cin
  // getline은 애초에 '\n'을 입력으로 안 받으므로 버퍼 비워줄 필요가 없다.
  getline(cin, str1);
  getline(cin, str2);
  cout << str1 << " " << str2 << "\n";
}