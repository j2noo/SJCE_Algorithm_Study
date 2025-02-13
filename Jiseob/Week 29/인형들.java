import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 인형들 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] doll = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            doll[i] = Integer.parseInt(st.nextToken());
        }

        double minValue = Double.MAX_VALUE;
        for (int k = K; k <= N; k++) {
            for (int i = 0; i <= N - k; i++) {
                int[] temp = new int[k];
                for (int j = 0; j < k; j++) {
                    temp[j] = doll[i + j];
                }

                minValue = Math.min(minValue, calculateStandardDeviation(temp));
            }
        }

        System.out.printf("%.11f", minValue);
    }

    static double calculateStandardDeviation(int[] arr) {
        double sum = 0.0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        double m = sum / arr.length;

        double variance = 0;

        for (int i = 0; i < arr.length; i++) {
            variance += Math.pow(arr[i] - m, 2);
        }

        variance /= arr.length;

        return Math.sqrt(variance);
    }
}
