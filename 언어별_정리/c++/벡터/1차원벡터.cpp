#include <bits/stdc++.h>
using namespace std;

int main() {

	// 1. 길이가 n인 int 벡터 만들기
	int n;
	cin >> n;

	vector<int> v(n); // 길이가 n인 벡터. 값은 0으로 초기화
	// vector<int> v(n,0) // 이렇게 하면 0으로 모두 초기화

	// 2. 값 입력
	for (int i=0; i<n; i++){
		cin >> v[i];
	}

	// 3. 인덱스로 접근해서 값 수정
	// 예: 첫 번째 원소에 +10 더하기
	if (n > 0) {
		v[0] += 10;
	}

	// 4. 전체 순회 - 인덱스로
	cout << "index for-loop:\n";
	for (int i=0; i<n; i++){
		cout << "v[" << i << "] = " << v[i] << "\n";
	}

	// 5. 전체 순회 - range-based for (python의 for x in v)
	cout << "range-based for : \n";
	for (int x: v){
		cout << x << " ";
	}
	cout << "\n";

	// 6. 벡터의 길이(size)
	cout << "size : " << v.size() << "\n";

}
