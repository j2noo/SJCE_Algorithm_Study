import java.io.*;
import java.util.*;

public class 좋은_구간 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int L = Integer.parseInt(br.readLine());
        List<Integer> S = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < L; i++) {
            S.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(S);

        int n = Integer.parseInt(br.readLine());

        if (S.contains(n)) {
            System.out.println(0);
        } else if (n < S.get(0)) {
            System.out.println((n) * (S.get(0) - n) - 1);
        } else {
            int count = 0;
            for (int i = 0; i < S.size() - 1; i++) {
                if (S.get(i) < n && S.get(i + 1) > n) {
                    count = (n - S.get(i)) * (S.get(i + 1) - n) - 1;
                    break;
                }
            }
            System.out.println(count);
        }
    }
}
