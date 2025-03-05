import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 사과_빨리_먹기 {
    static int[][] board = new int[5][5];
    static boolean[][] visited = new boolean[5][5];
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int distance = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        visited[r][c] = true;

        dfs(r, c, 0, 0);

        if (distance == Integer.MAX_VALUE) {
            distance = -1;
        }
        System.out.println(distance);
    }

    public static void dfs(int r, int c, int count, int d) {
        if (count == 3) {
            distance = Math.min(distance, d);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int x = r + dx[i];
            int y = c + dy[i];

            if (x < 0 || x >= 5 || y < 0 || y >= 5 || visited[x][y] || board[x][y] == -1) {
                continue;
            }

            visited[x][y] = true;

            if (board[x][y] == 1) {
                dfs(x, y, count + 1, d + 1);
            } else {
                dfs(x, y, count, d + 1);
            }

            visited[x][y] = false;
        }
    }
}