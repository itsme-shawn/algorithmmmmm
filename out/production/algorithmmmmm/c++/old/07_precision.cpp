#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

double a = 31.23456789;

int main() {
  cout << a << "\n";  // 31.2346
  cout.precision(9);  // 정수+소수 9자리 출력 (정수는 그대로)
  cout << a << "\n";  // 31.2345679 (정수부 2자리, 소수부 7자리)

  return 0;
}
