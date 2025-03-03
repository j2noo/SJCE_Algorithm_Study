#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int N, A[50], B[2][50]; //B[0][i]은 원소, B[1][i]은 B[0][i]의 크기 순위
	int S = 0;

	cin >> N;

	for (int i = 0; i < N; i++) {	//init rank of B
		B[1][i] = 1;
	}

	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	for (int i = 0; i < N; i++) {
		cin >> B[0][i];
	}

	for (int i = 0; i < N; i++) {		//순위 찾기
		for (int j = 0; j < i; j++) {	//같은 수일 경우 앞에 나온 숫자의 랭크가 더 높음(1에 가까움)
			if (B[0][i] <= B[0][j]) {
				B[1][i]++;
			}
		}
		for (int j = i; j < N; j++) {
			if (B[0][i] < B[0][j]) {
				B[1][i]++;
			}
		}
	}

	/*for (int i = 0; i < N; i++) {
		cout << B[0][i] << " ";
	}
	cout << endl;
	for (int i = 0; i < N; i++) {
		cout << B[1][i] << " ";
	}*/

	sort(A, A + N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (B[1][j] == i + 1) {
				//cout << "A: " << A[i] << " B: " << B[0][j] << endl;
				S += A[i] * B[0][j];
			}
		}
	}

	cout << S;

	return 0;
}
