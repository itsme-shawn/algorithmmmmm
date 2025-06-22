#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

double a = 1.23456789;
int b = 12;
int c = 2;

int main() {
  printf("%0.3lf\n", a);  // 1.235
  printf("%03d\n", b);    // 012
  printf("%05d\n", c);    // 00002
  printf("%6d\n", c);     //      2 (전체 6자리로 출력)

  return 0;
}