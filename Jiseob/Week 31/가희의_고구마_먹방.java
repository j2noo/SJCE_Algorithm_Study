import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 가희의_고구마_먹방 {
    static int R, C, T;
    static char[][] arr;
    static int[] dx = {0, 0, 1, -1, 0};
    static int[] dy = {-1, 1, 0, 0, 0};
    static int ans = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        arr = new char[R][C];

        int x = 0;
        int y = 0;
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                arr[i][j] = line.charAt(j);

                if (arr[i][j] == 'G') {
                    x = i;
                    y = j;
                }
            }
        }

        dfs(x, y, 0, 0);
        System.out.println(ans);
    }

    public static void dfs(int r, int c, int time, int count) {
        if (time == T) {
            ans = Math.max(ans, count);
            return;
        }

        for (int i = 0; i < 5; i++) {
            int x = r + dx[i];
            int y = c + dy[i];

            if (x < 0 || y < 0 || x >= R || y >= C || arr[x][y] == '#') {
                continue;
            }

            if (arr[x][y] == 'S') {
                arr[x][y] = '.';
                dfs(x, y, time + 1, count + 1);
                arr[x][y] = 'S';
            } else {
                dfs(x, y, time + 1, count);
            }
        }
    }
}
