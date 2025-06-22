#include <bits/stdc++.h>

using namespace std;

int main() {
  string a = "안녕하세요";

  cout << a << "\n";     // 안녕하세요
  cout << a[0] << "\n";  // �
  cout << a[1] << "\n";  // �
  cout << a[2] << "\n";  // �

  // 한글 문자열은 인덱스 접근 불가

  cout << a[0] << a[1] << a[2] << "\n";  // 안
  // 3바이트 연속으로 출력하면 한글 한 글자 출력

  string b = "hello";

  cout << b << "\n";     // hello
  cout << b[0] << "\n";  // h
  cout << b[1] << "\n";  // e
  cout << b[2] << "\n";  // l

  return 0;
}
