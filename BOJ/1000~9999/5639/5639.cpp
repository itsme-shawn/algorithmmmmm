#include <bits/stdc++.h>
using namespace std;

vector<int> pre_order;

void dfs(int start, int end){
	if (start >= end) return;

	int root = pre_order[start];

	// 왼쪽 서브트리가 끝나는 지점 찾기
	int idx = start + 1;
	while (idx < end && pre_order[idx] < root) {
		idx++;
	}

	// 왼쪽
	dfs(start+1, idx);
	// 오른쪽
	dfs(idx, end);
	// 루트 출력
	cout << root << "\n";	
	
}

int main() {
	// freopen("in.txt", "r", stdin);

	int x;
	while (cin >> x) {
		pre_order.push_back(x);
	}

	dfs(0, pre_order.size());

	return 0;
}

