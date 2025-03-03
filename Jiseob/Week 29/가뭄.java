import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 가뭄 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int d1 = Integer.parseInt(st.nextToken());
        int d2 = Integer.parseInt(st.nextToken());
        int d3 = Integer.parseInt(st.nextToken());

        double a = (d1 + d2 - d3) / 2.0;
        double b = (d1 + d3 - d2) / 2.0;
        double c = (d2 + d3 - d1) / 2.0;

        if (a < 1 || b < 1 || c < 1) {
            System.out.println(-1);
        } else {
            System.out.println(1);
            System.out.printf("%.1f %.1f %.1f", a, b, c);
        }
    }
}