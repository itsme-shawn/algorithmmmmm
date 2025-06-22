#include <bits/stdc++.h>

using namespace std;

// 내림차순 비교 함수
bool compare(int a, int b) { return a > b; }

int main() {
  vector<int> arr = {5, 2, 9, 1, 5, 6};

  // 내림차순으로 정렬
  sort(arr.begin(), arr.end(), compare);

  // 정렬된 배열 출력
  cout << "Sorted array (descending): ";
  for (int num : arr) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}
