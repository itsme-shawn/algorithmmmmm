#include <bits/stdc++.h>

using namespace std;

int main() {
  string a = "love is";

  a += " pain!";

  a.pop_back();  // ! 제거

  cout << a << " : " << a.size() << "\n";  // love is pain : 12
  cout << *a.begin() << "\n";              // ㅣ
  cout << char(*a.begin()) << "\n";        // ㅣ (위와 동일)

  cout << *a.end() << '\n';        // 제대로 출력 X
  cout << *(a.end() - 1) << '\n';  // n

  a.insert(0, "test ");
  cout << a << " : " << a.size() << "\n";  // test love is pain : 17

  a.insert(4, "ABCD");                     // 4번째 자리에 삽입
  cout << a << " : " << a.size() << "\n";  // testABCD love is pain : 21

  a.erase(0, 4);                           // 인덱스 0~4 까지 삭제
  cout << a << " : " << a.size() << "\n";  // ABCD love is pain : 17

  auto it = a.find("love");  // auto : 변수 타입 자동 추론
  // 여기서 it 는 size_t 로 인덱스 역할
  if (it != string::npos) {
    cout << "포함되어 있다" << '\n';  // 출력
  }

  cout << it << '\n';            // 5
  cout << string::npos << '\n';  // 18446744073709551615

  cout << a.substr(5, 2) << '\n';  // lo

  reverse(a.begin(), a.end());  // niap si evol DCBA
  cout << a << '\n';

  return 0;
}