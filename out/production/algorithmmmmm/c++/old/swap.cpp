#include <bits/stdc++.h>

using namespace std;

void swap(int& a, int& b) {
  int tmp = a;
  a = b;
  b = tmp;
}

int main() {
  int a = 3, b = 5;
  swap(a, b);
  cout << a << " " << b << endl;
}