#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> originMap;
vector<vector<int>> copiedMap;

void DFS(int i, int j, int size, int rain) {
	copiedMap[i][j] = 0;				//Ž���� ���� ����ŷ

	if (i < size - 1) {
		if (copiedMap[i + 1][j] == 1) {	//�Ʒ��� ���� Ž������ ���� ������ �ִٸ� Ž��
			DFS(i + 1, j, size, rain);
		}
	}

	if (j >= 1) {
		if (copiedMap[i][j - 1] == 1) {		//����
			DFS(i, j - 1, size, rain);
		}
	}

	if (j < size - 1) {
		if (copiedMap[i][j + 1] == 1) {	//������
			DFS(i, j + 1, size, rain);
		}
	}

	if (i >= 1) {
		if (copiedMap[i - 1][j] == 1) {		//����
			DFS(i - 1, j, size, rain);
		}
	}

	//�� �̻� Ž������ ���� ������ ���ٸ� return
	return;
}

int main() {
	int n;
	int min = 101, max = 0;
	cin >> n;

	originMap.resize(n + 1, vector<int>(n + 1));
	copiedMap.resize(n + 1, vector<int>(n + 1));

	vector<int> rain;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> originMap[i][j];
			rain.push_back(originMap[i][j]);
		}
	}

	sort(rain.begin(), rain.end());
	rain.erase(unique(rain.begin(), rain.end()), rain.end());

	vector<int> nRain(rain.size(), 0);

	//(debug): ���췮 ����Ǽ� �� ��µǳ�
	//for (int i = 0; i < rain.size(); i++) {
	//	cout << rain[i] << ' ' << endl;
	//}
	//cout << "-----------------" << endl;

	for (int i = 0; i < rain.size(); i++) {
		//DFS�� ���� ���纻 �� ����
		copy(originMap.begin(), originMap.end(), copiedMap.begin());
		//���췮���� ���� ������ 0, ���� ������ -1�� ��ȯ
		for (auto& row : copiedMap) {
			replace_if(row.begin(), row.end(), [rain, i](int num) { return num < rain[i]; }, 0);
		}

		for (auto& row : copiedMap) {
			replace_if(row.begin(), row.end(), [](int num) { return num != 0; }, 1);
		}

		//(debug): ������ ��⳪ �� ��⳪ ����ŷ �� �Ǿ���
		//for (int row = 0; row < n; row++) {
		//	for (int col = 0; col < n; col++) {
		//		cout << copiedMap[row][col] << ' ';
		//	}
		//	cout << endl;
		//}
		//cout << "-----------------" << endl;

		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				if (copiedMap[j][k] == 1) {
					nRain[i]++;
					DFS(j, k, n, rain[i]);
				}
			}
		}
	}

	//(debug): nRain�� �� ����
	//for (int i = 0; i < nRain.size(); i++) {
	//	cout << nRain[i] << ' ' << endl;
	//}

	cout << *max_element(nRain.begin(), nRain.end());

	return 0;
}