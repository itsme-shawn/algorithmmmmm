#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  int a[n];  // 런타임시기에 배열 크기 결정

  memset(a, 0, sizeof(a));

  for (int i : a) {  // 범위기반 루프는 컴파일시기에 결정
    cout << i << " ";
  }

  // 일부 컴파일러에서는 오류 발생 주의

  return 0;
}