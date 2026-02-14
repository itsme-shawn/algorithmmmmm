import java.io.*;
import java.util.*;

public class BFSGrid {
    public static void main(String[] args) throws Exception {
        // 설명: 2차원 격자 BFS 최단거리
        // 시간복잡도: O(N * M)
        // 주의사항: 경계 체크와 방문 체크가 필수이며 시작점/종점 막힘 처리 필요
        // 예시 입력:
        // 3 4
        // 1111
        // 1101
        // 0111
        // 예상 출력:
        // 5

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] grid = new char[n][m];
        for (int i = 0; i < n; i++) {
            grid[i] = br.readLine().toCharArray();
        }

        if (grid[0][0] == '0') {
            System.out.println(-1);
            return;
        }

        int[][] dist = new int[n][m];
        for (int[] row : dist) Arrays.fill(row, -1);

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        Deque<int[]> q = new ArrayDeque<>();
        dist[0][0] = 0;
        q.add(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (grid[nr][nc] == '0') continue;
                if (dist[nr][nc] != -1) continue;
                dist[nr][nc] = dist[r][c] + 1;
                q.add(new int[]{nr, nc});
            }
        }

        System.out.println(dist[n - 1][m - 1]);
    }
}
