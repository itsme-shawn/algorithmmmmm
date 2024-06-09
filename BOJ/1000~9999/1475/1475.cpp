#include <bits/stdc++.h>

using namespace std;

int n;
int freq[10];
int ans;
int main() {
  cin >> n;

  // int to string
  string room_num = to_string(n);

  for (char num : room_num) {
    freq[num - '0'] += 1;
  }

  for (int i = 0; i < 10; i++) {
    if (i == 6 || i == 9) continue;
    ans = max(ans, freq[i]);
  }

  ans = max(ans, (freq[6] + freq[9] + 1) / 2);

  cout << ans;
}