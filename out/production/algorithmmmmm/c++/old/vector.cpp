#include <bits/stdc++.h>

using namespace std;

int main() {
  const int SIZE = 5;

  // 1. 1차원배열 초기화
  int arr[SIZE];

  fill(arr, arr + SIZE, 1);  // 모든 요소 1으로 초기화

  for (int i = 0; i < SIZE; i++) {
    cout << arr[i] << " ";
  }
  cout << '\n';

  // 2. 1차원벡터 초기화
  vector<int> vec(SIZE);

  fill(vec.begin(), vec.end(), 2);  // 모든 요소 2로 초기화

  for (int i = 0; i < SIZE; i++) {
    cout << vec[i] << " ";
  }
  cout << '\n';

  // 3. 2차원배열 초기화
  const int ROWS = 3;
  const int COLS = 4;
  int arr2[ROWS][COLS];

  for (int i = 0; i < ROWS; i++) {
    fill(arr2[i], arr2[i] + COLS, 3);
  }

  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      cout << arr2[i][j] << " ";
    }
    cout << '\n';
  }

  // 4. 2차원벡터 초기화
  vector<vector<int>> vec2(ROWS, vector<int>(COLS));

  for (int i = 0; i < ROWS; i++) {
    fill(vec2[i].begin(), vec2[i].end(), 4);
  }

  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      cout << vec2[i][j] << " ";
    }
    cout << '\n';
  }

  return 0;
}