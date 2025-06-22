#include <bits/stdc++.h>

using namespace std;

int main() {
  // cin의 공백문자열 이슈
  string s1;
  cout << "input s1 : ";
  cin >> s1;
  cout << "s1 is " << s1 << '\n';

  // cin 입력 버퍼 비우기
  cin.ignore();

  // 또는 아래 방식
  /*
  string bufferflush;
  getline(cin, bufferflush);
  */

  /**
 input s1 : hi hello!
 s1 is hi

 cin 을 공백 문자열을 처리 못 함!
 */

  // getline 은 문자열을 공백 포함해서 처리할 수 있음
  string s2;
  cout << "input s2 : ";
  getline(cin, s2);
  cout << "s2 is " << s2 << '\n';

  /**
  input s2 : hi hello!
  s2 is hi hello!
  */

  string s3;
  cout << "input s3 : ";
  getline(cin, s3, '!');  // 종결문자를 '!'로 받아서 그 전까지만 받음
  cout << "s3 is " << s3 << '\n';

  /*
  input s3 : hi hello!
  s3 is hi hello
  */
}