#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> originMap;
vector<vector<int>> copiedMap;

void DFS(int i, int j, int size, int rain) {
	copiedMap[i][j] = 0;				//탐색한 영역 마스킹

	if (i < size - 1) {
		if (copiedMap[i + 1][j] == 1) {	//아래에 아직 탐색하지 않은 영역이 있다면 탐색
			DFS(i + 1, j, size, rain);
		}
	}

	if (j >= 1) {
		if (copiedMap[i][j - 1] == 1) {		//왼쪽
			DFS(i, j - 1, size, rain);
		}
	}

	if (j < size - 1) {
		if (copiedMap[i][j + 1] == 1) {	//오른쪽
			DFS(i, j + 1, size, rain);
		}
	}

	if (i >= 1) {
		if (copiedMap[i - 1][j] == 1) {		//위쪽
			DFS(i - 1, j, size, rain);
		}
	}

	//더 이상 탐색하지 않은 영역이 없다면 return
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

	//(debug): 강우량 경우의수 잘 출력되나
	//for (int i = 0; i < rain.size(); i++) {
	//	cout << rain[i] << ' ' << endl;
	//}
	//cout << "-----------------" << endl;

	for (int i = 0; i < rain.size(); i++) {
		//DFS를 돌릴 복사본 맵 생성
		copy(originMap.begin(), originMap.end(), copiedMap.begin());
		//강우량보다 높은 지역은 0, 낮은 지역은 -1로 변환
		for (auto& row : copiedMap) {
			replace_if(row.begin(), row.end(), [rain, i](int num) { return num < rain[i]; }, 0);
		}

		for (auto& row : copiedMap) {
			replace_if(row.begin(), row.end(), [](int num) { return num != 0; }, 1);
		}

		//(debug): 구역별 잠기나 안 잠기나 마스킹 잘 되었나
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

	//(debug): nRain값 잘 들어가나
	//for (int i = 0; i < nRain.size(); i++) {
	//	cout << nRain[i] << ' ' << endl;
	//}

	cout << *max_element(nRain.begin(), nRain.end());

	return 0;
}