import java.util.*;

public class FloydWarshall {
    public static void main(String[] args) {
        // 설명: 플로이드-워셜 (모든 쌍 최단거리)
        // 시간복잡도: O(N^3), 메모리 O(N^2)
        // 주의사항: INF를 충분히 크게 잡고 덧셈 오버플로에 주의
        // 그래프: 1->2(4), 2->3(1), 1->3(10)
        // 예상 출력:
        // dist[1][3]=5

        int n = 3;
        int INF = 1_000_000_000;
        int[][] dist = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        dist[1][2] = 4;
        dist[2][3] = 1;
        dist[1][3] = 10;

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        System.out.println("dist[1][3]=" + dist[1][3]);
    }
}
