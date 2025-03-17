import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 꿀_아르바이트 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] T = new int[n];
        long profit = 0;
        long maxProfit = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            T[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < m; i++) {
            maxProfit += T[i];
        }

        profit = maxProfit;
        for (int i = m; i < n; i++) {
            profit = profit - T[i - m] + T[i];
            maxProfit = Math.max(maxProfit, profit);
        }

        System.out.println(maxProfit);
    }
}
