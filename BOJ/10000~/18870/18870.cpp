#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> nums(n);
	for (int i=0; i<n; i++)
		cin >> nums[i];

	// 중복 제거 후 오름차순 정렬
	// unordered_set 을 쓰면 정렬이 안 되니까 set 을 사용 (Red-black tree 기반 set)
	set<int> s(nums.begin(), nums.end());

	// index 를 위해 다시 vector 로 변환
	vector<int> sorted_nums(s.begin(), s.end());

	// map 으로 만들기
	unordered_map<int,int> mp;
	int idx = 0;
	for (int x : sorted_nums)
		mp[x] = idx++;
	
	// 순회하면서 출력
	for (int x: nums){
		cout << mp[x] << " ";
	}

	return 0;
}