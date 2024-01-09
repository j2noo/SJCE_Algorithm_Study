#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int nArea = 0;
int nRain[625] = { 0 };
int n, map[25][25];

void DFS(int i, int j) {
	nRain[nArea]++;
	map[i][j] = nArea + 1;				//단지번호 + 1로 숫자 변경
	if (map[i + 1][j] == 1 && i < n - 1) {	//아래에 아직 탐색하지 않은 집이 있다면 탐색
		DFS(i + 1, j);
	}
	if (map[i][j - 1] == 1 && j >= 1) {		//왼쪽
		DFS(i, j - 1);
	}
	if (map[i][j + 1] == 1 && j < n - 1) {	//오른쪽
		DFS(i, j + 1);
	}
	if (map[i - 1][j] == 1 && i >= 1) {		//위쪽
		DFS(i - 1, j);
	}
	
	//더 이상 탐색하지 않은 집이 없다면 return
	return;
}

int main() {
	char in[26] = { '\0' };

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> in;
		for (int j = 0; j < n; j++) {
			map[i][j] = in[j] - '0';
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 1) {
				nArea++;
				DFS(i, j);
			}
		}
	}

	//변경된 맵 확인용 코드
	/*for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout.width(3);
			cout.fill(' ');
			cout << map[i][j] << ' ';
		}
		cout << endl;
	}*/

	cout << nArea << endl;
	sort(nRain, nRain + nArea + 1);
	for (int i = 0; i < nArea; i++) {
		cout << nRain[i + 1] << endl;
	}

	return 0;
} 
