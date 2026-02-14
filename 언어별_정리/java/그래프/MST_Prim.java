import java.util.*;

public class MST_Prim {
    public static void main(String[] args) {
        // 설명: 최소 신장 트리 (프림)
        // 시간복잡도: O(E log V)
        // 주의사항: 연결 그래프 기준이며, 방문 체크로 중복 간선 추출을 무시
        // 그래프(무방향):
        // 1-2(3), 1-3(1), 2-3(2), 2-4(4), 3-4(5)
        // 예상 출력:
        // mstWeight=7

        int n = 4;
        List<int[]>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        addEdge(g, 1, 2, 3);
        addEdge(g, 1, 3, 1);
        addEdge(g, 2, 3, 2);
        addEdge(g, 2, 4, 4);
        addEdge(g, 3, 4, 5);

        boolean[] used = new boolean[n + 1];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.add(new int[]{1, 0});

        int total = 0;
        int picked = 0;
        while (!pq.isEmpty() && picked < n) {
            int[] cur = pq.poll();
            int v = cur[0];
            int w = cur[1];
            if (used[v]) continue;
            used[v] = true;
            total += w;
            picked++;

            for (int[] e : g[v]) {
                if (!used[e[0]]) pq.add(new int[]{e[0], e[1]});
            }
        }

        System.out.println("mstWeight=" + total);
    }

    private static void addEdge(List<int[]>[] g, int a, int b, int w) {
        g[a].add(new int[]{b, w});
        g[b].add(new int[]{a, w});
    }
}
