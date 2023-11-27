#include <iostream>

using namespace std;

int main() {
	char board[50][50];
	int M, N, min = 64, cnt = 0;
	char chessBoard[8][8] = { 'W','B','W','B','W','B','W','B',
						  'B','W','B','W','B','W','B','W',
						  'W','B','W','B','W','B','W','B',
						  'B','W','B','W','B','W','B','W',
						  'W','B','W','B','W','B','W','B',
						  'B','W','B','W','B','W','B','W',
						  'W','B','W','B','W','B','W','B',
						  'B','W','B','W','B','W','B','W'};
	cin >> M >> N;

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	for (int i = 0; i < M - 7; i++) {
		for (int j = 0; j < N - 7; j++) {
			for (int k = 0; k < 8; k++) {
				for (int l = 0; l < 8; l++) {
					if (chessBoard[k][l] != board[i + k][j + l]) {
						cnt++;
					}
				}
			}
			if (cnt > 64 - cnt) cnt = 64 - cnt;
			if (min > cnt) min = cnt;
			cnt = 0;
		}
	}

	cout << min;

	return 0;
}