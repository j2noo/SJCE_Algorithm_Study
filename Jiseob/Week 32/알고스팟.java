import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 알고스팟 {
    static int N, M;
    static int[][] arr;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        bfs();
    }

    static void bfs() {
        Deque<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 0});
        visited[0][0] = true;

        while(!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int cnt = current[2];

            if (x == N - 1 && y == M - 1) {
                System.out.println(cnt);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M || visited[nx][ny]) {
                    continue;
                }

                if (arr[nx][ny] == 0) {
                    q.addFirst(new int[]{nx, ny, cnt});
                } else {
                    q.addLast(new int[]{nx, ny, cnt + 1});
                }

                visited[nx][ny] = true;
            }
        }
    }
}
