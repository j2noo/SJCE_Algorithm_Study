import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ZOAC {
    static StringBuilder sb = new StringBuilder();
    static String input;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine();
        visited = new boolean[input.length()];

        zoac(0, input.length() - 1);
        System.out.println(sb);
    }

    static void zoac(int left, int right) {
        if (left > right) {
            return;
        }

        int minIndex = left;
        for (int i = left + 1; i <= right; i++) {
            if (input.charAt(minIndex) > input.charAt(i)) {
                minIndex = i;
            }
        }

        visited[minIndex] = true;

        for (int i = 0; i < input.length(); i++) {
            if (visited[i]) {
                sb.append(input.charAt(i));
            }
        }

        sb.append("\n");
        zoac(minIndex + 1, right);
        zoac(left, minIndex - 1);
    }
}
