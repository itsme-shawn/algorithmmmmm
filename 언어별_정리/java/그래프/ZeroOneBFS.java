import java.util.*;

public class ZeroOneBFS {
    public static void main(String[] args) {
        // 설명: 0-1 BFS (가중치가 0 또는 1일 때 최단거리)
        // 시간복잡도: O(V + E)
        // 주의사항: 간선 가중치가 0 또는 1일 때만 사용 가능
        // 그래프: 1-2(0), 1-3(1), 2-3(1), 2-4(0), 3-4(1)
        // 예상 출력:
        // dist[4]=0

        int n = 4;
        List<int[]>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();

        addEdge(g, 1, 2, 0);
        addEdge(g, 1, 3, 1);
        addEdge(g, 2, 3, 1);
        addEdge(g, 2, 4, 0);
        addEdge(g, 3, 4, 1);

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        Deque<Integer> dq = new ArrayDeque<>();
        dist[1] = 0;
        dq.add(1);

        while (!dq.isEmpty()) {
            int v = dq.pollFirst();
            for (int[] e : g[v]) {
                int nv = e[0];
                int w = e[1];
                if (dist[v] + w < dist[nv]) {
                    dist[nv] = dist[v] + w;
                    if (w == 0) dq.addFirst(nv);
                    else dq.addLast(nv);
                }
            }
        }

        System.out.println("dist[4]=" + dist[4]);
    }

    private static void addEdge(List<int[]>[] g, int a, int b, int w) {
        g[a].add(new int[]{b, w});
        g[b].add(new int[]{a, w});
    }
}
