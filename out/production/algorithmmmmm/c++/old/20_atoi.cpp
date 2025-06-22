#include <bits/stdc++.h>

using namespace std;

int main() {
  int num = 0;
  char cStr[30] = "2019";

  // 문자열 타입으로 출력
  cout << cStr << " " << typeid(cStr).name() << "\n";

  // char* -> int
  num = atoi(cStr);

  // int 타입으로 출력
  cout << num << " " << typeid(num).name() << "\n";

  return 0;
}