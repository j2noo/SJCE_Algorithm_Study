import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 한_줄로_서기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] answer = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            int count = 0;
            int index = 0;
            while (count != arr[i]) {
                if (answer[index] == 0) {
                    count++;
                }
                index++;
            }

            while (answer[index] != 0) {
                index++;
            }

            answer[index] = i + 1;
        }

        for (int num : answer) {
            System.out.print(num + " ");
        }
    }
}
