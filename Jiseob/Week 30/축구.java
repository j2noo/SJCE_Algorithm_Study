import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 축구 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double A = Double.parseDouble(br.readLine()) / 100;
        double B = Double.parseDouble(br.readLine()) / 100;

        double[][][] dp = new double[19][19][19];

        dp[0][0][0] = 1.0;

        // dp[i][j][k] = i번째 구간에서 A팀이 j골을 넣고 B팀이 k골을 넣을 확률
        for (int i = 1; i < 19; i++) {
            for (int j = 0; j <= i; j++) {
                for (int k = 0; k <= i; k++) {
                    if (j > 0) { // A팀이 골을 넣을 경우
                        dp[i][j][k] += dp[i - 1][j - 1][k] * A * (1 - B);
                    }

                    if (k > 0) { // B팀이 골을 넣을 경우
                        dp[i][j][k] += dp[i - 1][j][k - 1] * (1 - A) * (B);
                    }

                    if (j > 0 && k > 0) { // A팀, B팀 둘 다 골을 넣을 경우
                        dp[i][j][k] += dp[i - 1][j - 1][k - 1] * A * B;
                    }

                    // 둘 다 골을 넣지 않을 경우
                    dp[i][j][k] += dp[i - 1][j][k] * (1 - A) * (1 - B);
                }
            }
        }

        double answer = 0;

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                if (isPrime(i) || isPrime(j)) {
                    answer += dp[18][i][j];
                }
            }
        }

        System.out.printf("%.16f", answer);
    }

    static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }

        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }
}