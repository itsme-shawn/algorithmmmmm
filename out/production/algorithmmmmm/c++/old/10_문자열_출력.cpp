#include <bits/stdc++.h>

using namespace std;

int a = 1;
char s = 'a';
string str = "문자열";
double b = 1.234567;

int main() {
  printf("%d\n", a);  // 1
  printf("%c\n", s);  // a
  // printf("%s\n", str); // error!
  printf("%s\n", str.c_str());  // c_str() : string 을 문자열포인터로 변환
  cout << str << "\n";  // cout 으로 출력할 때 string 그대로 사용가능
  printf("%lf\n", b);  // 1.234567

  return 0;
}