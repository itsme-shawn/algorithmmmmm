#include <math.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(long long A) {
  int cnt = 0;

  for (int i = 1; i < sqrt(A); i++) {
    if (A % i == 0) cnt++;
  }

  cnt *= 2;

  if (sqrt(A) == (int)sqrt(A)) {
    cout << "True" << '\n';
    cnt++;
  }

  cout << cnt;

  return cnt;
}

int main() { solution(8); }