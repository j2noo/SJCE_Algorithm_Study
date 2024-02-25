#include <iostream>
#include <vector>

#pragma warning (disable: 4996)

using namespace std;

int Min(int a, int b, int c) {
	if (a < b) {
		if (a < c) return a;
		else if (b < c) return b;
		else return c;
	}
	else {
		if (b < c) return b;
		else return c;
	}
}

int Sol(int n, int m, vector<vector<int>> v) {
	int max = 0;

	for (int i = 0; i < n; i++) {
		if (v[i][0] == 1) max = 1;
	}

	for (int i = 0; i < n; i++) {
		if (v[0][i] == 1) max = 1;
	}

	for (int i = 1; i < n; i++) {
		for (int j = 1; j < m; j++) {
			if (v[i][j] > 0) {
				if (v[i - 1][j - 1] > 0 && v[i][j - 1] > 0 && v[i - 1][j] > 0) {
					v[i][j] += Min(v[i - 1][j - 1], v[i][j - 1], v[i - 1][j]);
					if (v[i][j] > max) max = v[i][j];
				}
				/*cout << "----------------------" << endl;
				for (int k = 0; k < n; k++) {
					for (int l = 0; l < m; l++) {
						cout << v[k][l] << ' ';
					}
					cout << endl;
				}*/
			}
		}
	}

	return max * max;
}

int main() {
	int n, m;
	char in;
	int maxSize = 0;

	cin >> n >> m;
	vector<vector<char>> v(n, vector<char>(m));
	vector<vector<int>> u(n, vector<int>(m));
	

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> v[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			u[i][j] = v[i][j] - '0';
		}
	}

	cout << Sol(n, m, u);

	return 0;
}