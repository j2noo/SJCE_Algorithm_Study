#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
	vector<char> num;
	string in;

	cin >> in;
	copy(in.begin(), in.end(), back_inserter(num));
	
	if (find(num.begin(), num.end(), '0') == num.end()) {
		cout << -1 << "NO ZERO";
		return 0;
	}

	if ((accumulate(num.begin(), num.end(), 0) - '0' * num.size()) % 3 != 0) {
		cout << -1 << "MOD 3 IS" << accumulate(num.begin(), num.end(), 0) - '0' * num.size() % 3;
		return 0;
	}

	sort(num.begin(), num.end(), greater<char>());

	for (int i = 0; i < num.size(); i++) {
		cout << num[i];
	}

	return 0;
}