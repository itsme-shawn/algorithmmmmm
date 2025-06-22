#include <bits/stdc++.h>

using namespace std;

string a, s;

int main() {
  getline(cin, s);
  cout << s << '\n';

  getline(cin, s, '!');  // 종결문자를 '!'로 받아서 그 전까지만 받음
  cout << s << '\n';

  return 0;
}

/*
입력
테스트 입력

출력
테스트 입력

입력
테스트 입력!

출력
테스트 입력
*/