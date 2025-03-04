import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 넷이_놀기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        String[] inputs = br.readLine().split(" ");
        int A = Integer.parseInt(inputs[0]);
        int B = Integer.parseInt(inputs[1]);
        HashSet<String> set = new HashSet<>();
        int[][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            String point = br.readLine();
            set.add(point);
            inputs = point.split(" ");
            arr[i][0] = Integer.parseInt(inputs[0]);
            arr[i][1] = Integer.parseInt(inputs[1]);
        }

        int count = 0;
        for (int i = 0; i < N; i++) {
            String p1 = (arr[i][0] + A) + " " + arr[i][1];
            String p2 = arr[i][0] + " " + (arr[i][1] + B);
            String p3 = (arr[i][0] + A) + " " + (arr[i][1] + B);

            if (set.contains(p1) && set.contains(p2) && set.contains(p3)) {
                count++;
            }
        }

        System.out.println(count);
    }
}