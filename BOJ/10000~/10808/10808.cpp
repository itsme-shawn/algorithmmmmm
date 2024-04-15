#include <bits/stdc++.h>

using namespace std;

int main() {
  int arr[26] = {
      0,
  };

  string word = "";
  cin >> word;

  for (char w : word) {
    arr[w - 'a']++;
  }

  for (int i = 0; i <= (int)'z' - (int)'a'; i++) {
    cout << arr[i] << " ";
  }

  return 0;
}