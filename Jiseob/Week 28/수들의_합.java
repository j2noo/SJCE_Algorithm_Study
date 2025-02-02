import java.io.*;

public class 수들의_합 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long S = Long.parseLong(br.readLine());

        long n = 1;
        while ((n * (n + 1) / 2) <= S) {
            n++;
        }

        System.out.println(n - 1);
    }
}
