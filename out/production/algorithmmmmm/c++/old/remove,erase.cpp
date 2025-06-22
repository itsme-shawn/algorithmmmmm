#include <bits/stdc++.h>

using namespace std;

vector<int> v;

void print() {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
  cout << '\n';

  cout << "size : " << v.size() << "\n";
  cout << "capacity : " << v.capacity() << "\n";
}

int main() {
  v = {1, 1, 2, 3, 3, 4, 5, 8, 20, 10};

  cout << "삭제 전 vector 값들 : ";
  print();

  auto ret = remove(v.begin(), v.end(), 1);  // 처음부터 끝까지 값 중 1 없애기
  cout << "값 1을 remove 한 후 리턴 값 : " << *ret << '\n';

  cout << "값 1 remove 후 vector 값들 : ";
  print();

  // v.erase(시작범위, 끝범위) : [시작범위,끝범위) 의 값 모두 삭제
  v.erase(v.begin(), v.begin() + 1);  // 인덱스 1번 원소 삭제

  cout << "인덱스 1번 erase 후 vector 값들 : ";
  print();

  v.erase(remove(v.begin(), v.end(), 3), v.end());
  cout << "값 3 remove + erase 후 vector 값들 : ";
  print();
}