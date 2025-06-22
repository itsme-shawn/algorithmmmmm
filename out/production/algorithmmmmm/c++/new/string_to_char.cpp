#include <bits/stdc++.h>

using namespace std;

int main() {
  char ch[100];
  string a = "hello world";

  // c_str() 로 string -> char* 변환 후
  // strcpy 로 char 배열에 저장
  strcpy(ch, a.c_str());

  cout << ch << '\n';
}