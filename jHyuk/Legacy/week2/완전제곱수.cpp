#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

#define INF 2147483647

using namespace std;

int main() {
	int M, N, sum = 0, min = INF;

	cin >> M >> N;

	for (int i = M; i <= N; i++) {
		if ((int)sqrt(i) - sqrt(i) == 0) {	//제곱근이 정수이면 반환
			if (min > i) min = i;
			sum += i;
		}
	}

	if (min != INF) cout << sum << endl << min << endl;
	else cout << -1;

	return 0;
}
