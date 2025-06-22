#include <bits/stdc++.h>

using namespace std;

int main() {
  pair<int, int> pi;
  tuple<int, int, int> tl;

  int a, b, c;

  pi = {1, 2};     // 또는 make_pair(1,2)
  tl = {3, 4, 5};  // 또는 make_tuple(3,4,5)

  // 1. pair 에서 tie 로 한 번에 꺼내기
  tie(a, b) = pi;
  cout << a << " " << b << endl;  // 1 2

  // 2. pair 에서 first, second 로 하나씩 꺼내기
  a = pi.first;
  b = pi.second;

  cout << a << " " << b << endl;  // 1 2

  // 3. tuple 에서 tie 로 한 번에 꺼내기
  tie(a, b, c) = tl;
  cout << a << " " << b << " " << c << endl;  // 3 4 5

  // 4. tuple 에서 get 으로 하나씩 꺼내기
  a = get<0>(tl);
  b = get<1>(tl);
  c = get<2>(tl);

  cout << a << " " << b << " " << c << endl;  // 3 4 5
}