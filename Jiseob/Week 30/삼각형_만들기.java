import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 삼각형_만들기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        int maxSum = -1;
        for (int i = N - 1; i >= 2; i--) {
            int a = arr[i];
            int b = arr[i - 1];
            int c = arr[i - 2];

            if (a + b > c && a + c > b && b + c > a) {
                maxSum = Math.max(maxSum, a + b + c);
            }
        }

        System.out.println(maxSum);
    }
}
