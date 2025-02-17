import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 치킨_TOP_N {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] chicken = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            chicken[i] = Integer.parseInt(st.nextToken());
        }

        int k = Integer.parseInt(br.readLine());

        int len = N / k;

        for (int i = 0; i < N / len; i++) {
            int from = i * len;
            int to = (i + 1) * len;

            Arrays.sort(chicken, from, to);
        }

        for (int num : chicken) {
            System.out.print(num + " ");
        }
    }
}
