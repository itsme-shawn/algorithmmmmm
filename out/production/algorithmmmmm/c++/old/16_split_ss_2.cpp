#include <bits/stdc++.h>
// #include <sstream>

using namespace std;

vector<string> split(const string& input) {
  vector<string> result;

  stringstream ss;  // stringstream 객체 선언
  string temp;      // 문자열 자를 때 사용하는 임시변수
  ss.str(input);    // ss 를 string input 으로 초기화

  while (ss >> temp) {
    result.push_back(temp);
  }

  return result;
}

int main() {
  string s = "안녕하세요 hello world";

  vector<string> a = split(s);

  for (string b : a) {
    cout << b << '\n';
  }

  /*
  안녕하세요
  hello
  world
  */
}