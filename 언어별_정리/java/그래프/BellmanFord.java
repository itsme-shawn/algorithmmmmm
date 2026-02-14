import java.util.*;

public class BellmanFord {
    public static void main(String[] args) {
        // 설명: 벨만-포드 (음수 간선 가능, 음수 사이클 탐지)
        // 시간복잡도: O(V * E)
        // 주의사항: 음수 사이클 탐지는 V번째 완화로 확인하며, 오버플로 방지에 주의
        // 그래프: 1->2(4), 1->3(5), 2->3(-3), 3->4(2)
        // 예상 출력:
        // dist[4]=3

        int n = 4;
        List<int[]> edges = new ArrayList<>();
        edges.add(new int[]{1, 2, 4});
        edges.add(new int[]{1, 3, 5});
        edges.add(new int[]{2, 3, -3});
        edges.add(new int[]{3, 4, 2});

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;

        for (int i = 1; i <= n - 1; i++) {
            for (int[] e : edges) {
                int a = e[0], b = e[1], w = e[2];
                if (dist[a] == Integer.MAX_VALUE) continue;
                if (dist[a] + w < dist[b]) {
                    dist[b] = dist[a] + w;
                }
            }
        }

        System.out.println("dist[4]=" + dist[4]);
    }
}
