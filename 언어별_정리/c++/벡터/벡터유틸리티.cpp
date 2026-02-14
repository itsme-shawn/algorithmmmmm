#include <bits/stdc++.h>

using namespace std;

void print(vector<int> &v){
	for (int n : v){
		cout << n << " ";
	}
	cout << "\n";
}

int main() {
	vector<int> v;  // 빈 벡터 정의
	print(v);

    // 추가
    // cpp : v.push_back(x)
    // python : v.append(x)
	v.push_back(10);
	v.push_back(20);
	v.push_back(30);
	

	cout << "after append : ";
	print(v);

    // 삽입
    // cpp : v.insert(v.begin() + i, x)
    // python : v.insert(i, x)
	v.insert(v.begin() + 1, 15);  // 1번째에 15 삽입
	cout << "after insert(1,15): ";
	print(v);

    // 맨 뒤 삭제
    // cpp : v.pop_back()
    // python : v.pop()

	v.pop_back();
	cout << "after pop(): ";
	print(v);

    // 특정 인덱스 삭제
    // cpp : v.erase(v.begin() + i)
    // python : v.pop(i), del v[i]
	v.erase(v.begin() + 0);
	cout << "after pop(0): ";
	print(v);

    // 구간 삭제
    // cpp : v.erase(v.begin()+a, v.begin()+b)
    // python : del v[a:b]
	v.push_back(25);
	v.push_back(35);
	v.push_back(45);
	cout << "after push_back 25,35,45 :";
	print(v);
	v.erase(v.begin() + 1, v.begin() + 3); // 인덱스 1~2 삭제
	cout << "after del v[1:3]: ";
    print(v);

    // 길이 확인
    // cpp : v.size()
    // python : len(v)
	cout << "size = " << v.size() << "\n";

	// 인덱스 접근
    // cpp : v[i]
    // python : v[i]
    cout << "v[0] = " << v[0] << "\n";

    // 마지막 원소
    // cpp : v.back()
    // python : v[-1]
    cout << "v.back() = " << v.back() << "\n";

	// 개수세기
	// cpp : count(시작, 끝, 찾는 값)
	// python : count(x)
	v.push_back(10);
	v.push_back(10);
	cout << "after push_back 10,10: ";
	print(v);
	cout << "count(10) = " << count(v.begin(), v.end(), 10) << "\n";

	// 포함 여부 확인
	// cpp : find(시작, 끝, x) != 끝
	// python : x in v
	int x = 25;
	bool exists = (find(v.begin(), v.end(), x) != v.end());
	cout << x << (exists ? " exists" : " not in v") << "\n";

	// 값의 인덱스 찾기
	// cpp : find(v.begin(), v.end(), x) - v.begin()
	// python : v.index(x)
	int target = 10;
	int idx = find(v.begin(), v.end(), target) - v.begin();
	cout << "index of " << target << " = " << idx << "\n";

	// 값의 모든 인덱스 찾기
	// cpp : find문 활용 or 단순 for문으로 탐색
	// python : [i for i, val in enumerate(v) if val == x]
	auto it = v.begin();
	// find 의 결과를 it 에 저장하고 1 증가
	while((it = find(it, v.end(), target)) != v.end()) {
		cout << "found at index " << it - v.begin() << "\n";
		it++;
	}

	// 정렬 (기본 오름차순)
	// cpp : sort(v.begin(), v.end())
	// python : v.sort()
	sort(v.begin(), v.end());
	cout << "after sort: ";
	print(v);

	// 내림차순 정렬
	// cpp : sort(v.begin(), v.end(), greater<int>())
	// python : v.sort(reverse=True)
	sort(v.begin(), v.end(), greater<int>());
	cout << "after sort desc: ";
	print(v);

	// 역순 뒤집기
	// cpp : reverse(v.begin(), v.end())
	// python : v.reverse()
	reverse(v.begin(), v.end());
	cout << "after reverse(): ";
	print(v);

	// 확장
	// cpp : v.insert(v.end(), u.begin(), u.end())
	// python : v.extend(u)
	vector<int> u = {100,200,300};
	v.insert(v.end(), u.begin(), u.end());
	cout << "after extend(u): ";
	print(v);

	// 전체 비우기
	// cpp : v.clear()
	// python : v.clear()
	v.clear();
	cout << "after clear: ";
	print(v);

}