#include <bits/stdc++.h>

using namespace std;

int main() {
  char ch[100] = "hello world";

  // string 생성자를 이용해서 char* -> string 변환
  string new_str(ch);

  cout << new_str;
}