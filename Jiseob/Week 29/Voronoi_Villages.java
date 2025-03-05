import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Voronoi_Villages {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        double minSize = Integer.MAX_VALUE;
        for (int i = 1; i < N - 1; i++) {
            double leftSize = (double) (arr[i - 1] + arr[i]) / 2.0;
            double rightSize = (double) (arr[i] + arr[i + 1]) / 2.0;

            double size = rightSize - leftSize;

            minSize = Math.min(size, minSize);
        }

        System.out.printf("%.1f%n", minSize);
    }
}
