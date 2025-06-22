#include <math.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<long long> yaksu;

int get_yaksu(long long A) {
  int cnt = 0;

  for (int i = 1; i < sqrt(A); i++) {
    if (A % i == 0) {
      cnt++;
      yaksu.push_back(i);
    }
  }

  cnt *= 2;

  if (sqrt(A) == (int)sqrt(A)) {
    cnt++;
  }

  for (int i = yaksu.size() - 1; i >= 0; i--) {
    yaksu.push_back(A / yaksu[i]);
  }

  return cnt;
}

long long solution(long long A) {
  int maxx_num = -1;
  long long cur_yaksu_cnt = 1000000000000;

  cout << get_yaksu(A) << " ";

  // for (int num : yaksu) {
  //   cout << "num : " << num << " ";
  // }

  vector<long long> temp = yaksu;

  for (int num : temp) {
    if (num == 1) continue;

    cout << num << " ";

    int yaksu_cnt = get_yaksu(num);

    if (get_yaksu(num) < yaksu_cnt && num > maxx_num) {
      cur_yaksu_cnt = yaksu_cnt;
      maxx_num = num;
    }
  }

  cout << maxx_num;

  return maxx_num;
}

int main() { solution(21); }