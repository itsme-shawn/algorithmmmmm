#include <bits/stdc++.h>

using namespace std;

int arr[26];
int main() {
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