import java.io.*;
import java.util.*;

public class 통계학 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        double sum = 0;
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];
        }
        Arrays.sort(arr);

        int mean = (int)Math.round(sum / N);
        int median = arr[N / 2];
        int mode = 0;
        int range = arr[arr.length - 1] - arr[0];

        HashMap<Integer, Integer> map = new LinkedHashMap<>();
        int max = 0;
        for (int i = 0; i < N; i++) {
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);

            if (max < map.get(arr[i])) {
                max = map.get(arr[i]);
            }
        }
        ArrayList<Integer> count = new ArrayList<>();
        for (Integer key : map.keySet()) {
            if (map.get(key) == max) {
                count.add(key);
            }
        }

        if (count.size() > 1) {
            mode = count.get(1);
        }
        else {
            mode = count.get(0);
        }

        bw.write(mean + "\n");
        bw.write(median + "\n");
        bw.write(mode + "\n");
        bw.write(range + "\n");
        bw.flush();
    }
}