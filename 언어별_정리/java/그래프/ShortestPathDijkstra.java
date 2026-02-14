import java.io.*;
import java.util.*;

public class ShortestPathDijkstra {
    public static void main(String[] args) throws Exception {
        // 설명: 다익스트라 최단거리 (가중치 양수)
        // 시간복잡도: O((V + E) log V)
        // 주의사항: 간선 가중치는 음수가 없어야 하며, 우선순위큐의 오래된 항목은 무시
        // 예시 입력:
        // 5 6
        // 1 2 2
        // 1 3 5
        // 2 3 1
        // 2 4 2
        // 3 5 3
        // 4 5 1
        // 예상 출력:
        // 5

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<int[]>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            g[a].add(new int[]{b, w});
            g[b].add(new int[]{a, w});
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        dist[1] = 0;
        pq.add(new int[]{1, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int v = cur[0];
            int d = cur[1];
            if (d != dist[v]) continue;

            for (int[] e : g[v]) {
                int nv = e[0];
                int w = e[1];
                int nd = d + w;
                if (nd < dist[nv]) {
                    dist[nv] = nd;
                    pq.add(new int[]{nv, nd});
                }
            }
        }

        System.out.println(dist[n]);
    }
}
