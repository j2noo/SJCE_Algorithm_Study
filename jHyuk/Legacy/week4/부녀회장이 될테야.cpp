#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T, k, n;
    cin >> T; // 테스트 케이스의 수

    for(int i=0; i<T; i++){
        cin >> k >> n;
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= n; i++) {
            dp[0][i] = i;
        }

        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }

        cout << dp[k][n] << endl;
    }

    return 0;
}