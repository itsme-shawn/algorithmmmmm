#include <bits/stdc++.h>

using namespace std;

int main() {
  // 1. char* -> string 형변환
  // 자동형변환됨
  const char* cStr = "Cstring";
  string cppStr = cStr;
  cout << cppStr << endl;

  // 2. string -> char* 형변환
  // c_str() 써줘야함
  string cppStr2 = "CPPstring";
  const char* cStr2 = cppStr2.c_str();
  cout << cStr2 << endl;
}