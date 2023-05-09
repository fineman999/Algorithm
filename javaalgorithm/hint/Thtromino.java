package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Thtromino {
    private static int n;
    private static int m;
    private static int maxNum;

    private static final int[] dx = {0, -1, 0, 1};
    private static final int[] dy = {1, 0, -1, 0};
    private static final int MAXBLOCKCOUNT = 4;
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        setNAndK(br);
        int[][] graph = new int[n][m];
        setGraphAndMaxNum(br, graph);
        boolean[][] visited = new boolean[n][m];


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(!visited[i][j]) {
                    visited[i][j] = true;
                    dfs(j, i, graph, visited, 1, graph[i][j]);
                    visited[i][j] = false;
                }
            }
        }

        System.out.println(answer);
    }


    private static void dfs(int x, int y, int[][] graph, boolean[][] visited, int cnt, int sub_answer) {
        if (sub_answer + (MAXBLOCKCOUNT - cnt) * maxNum < answer) {
            return;
        }

        if (cnt == MAXBLOCKCOUNT){
            answer = Math.max(sub_answer, answer);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(-1 < ny && ny < n && -1 < nx && nx < m && !visited[ny][nx]) {
                if(cnt == 2) {
                    visited[ny][nx] = true;
                    dfs(x, y, graph, visited, cnt + 1, sub_answer + graph[ny][nx]);
                    visited[ny][nx] = false;
                }
                visited[ny][nx] = true;
                dfs(nx, ny, graph, visited, cnt + 1, sub_answer + graph[ny][nx]);
                visited[ny][nx] = false;
            }
        }

    }

    private static void setGraphAndMaxNum(BufferedReader br, int[][] graph) throws IOException {
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                maxNum = Math.max(graph[i][j], maxNum);
            }
        }
    }

    private static void setNAndK(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
    }
}
