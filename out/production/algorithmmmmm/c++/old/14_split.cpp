#include <bits/stdc++.h>

using namespace std;

vector<string> split(const string& input, string dlim) {
  vector<string> result;
  auto start = 0;
  auto end = input.find(dlim);

  while (end != string::npos) {
    result.push_back(input.substr(start, end - start));
    start = end + dlim.size();
    end = input.find(dlim, start);
  }

  result.push_back(input.substr(start));

  return result;
}

int main() {
  string s = "안녕하세요 hello world";
  string d = " ";

  vector<string> a = split(s, d);

  for (string b : a) {
    cout << b << '\n';
  }

  /*
  안녕하세요
  hello
  world
  */
}