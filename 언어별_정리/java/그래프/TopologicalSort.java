import java.util.*;

public class TopologicalSort {
    public static void main(String[] args) {
        // 설명: 위상정렬 (DAG에서 선행 관계 정렬)
        // 시간복잡도: O(V + E)
        // 주의사항: DAG에서만 유효하며, 사이클이 있으면 결과 길이가 V보다 작음
        // 그래프: 1->2, 1->3, 3->4
        // 예상 출력(한 예):
        // order=[1, 2, 3, 4] 또는 [1, 3, 4, 2]

        int n = 4;
        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();

        g[1].add(2);
        g[1].add(3);
        g[3].add(4);

        int[] indeg = new int[n + 1];
        for (int v = 1; v <= n; v++) {
            for (int nv : g[v]) indeg[nv]++;
        }

        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) if (indeg[i] == 0) q.add(i);

        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int v = q.poll();
            order.add(v);
            for (int nv : g[v]) {
                if (--indeg[nv] == 0) q.add(nv);
            }
        }

        System.out.println("order=" + order);
    }
}
