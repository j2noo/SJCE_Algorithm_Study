import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 진짜_공간 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[] files = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            files[i] = Integer.parseInt(st.nextToken());
        }
        int cluster = Integer.parseInt(br.readLine());

        long clusterSize = 0;
        for (long file : files) {
            if (file == 0) {
                continue;
            }

            if (file < cluster) {
                clusterSize += cluster;
            } else if (file % cluster == 0) {
                clusterSize += (file / cluster) * cluster;
            } else {
                clusterSize += ((file / cluster) + 1) * cluster;
            }
        }

        System.out.println(clusterSize);
    }
}
