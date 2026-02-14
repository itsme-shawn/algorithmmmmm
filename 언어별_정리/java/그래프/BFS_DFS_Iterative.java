import java.util.*;

public class BFS_DFS_Iterative {
    public static void main(String[] args) {
        // 설명: 그래프 BFS/DFS 반복문 버전
        // 시간복잡도: O(V + E)
        // 주의사항: 방문 체크 순서에 따라 DFS 순회 결과가 달라질 수 있음
        // 그래프: 1-2, 1-3, 2-4, 3-5
        // 예상 출력:
        // bfs=[1, 2, 3, 4, 5]
        // dfs=[1, 3, 5, 2, 4] (스택 LIFO 특성)

        int n = 5;
        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        addEdge(g, 1, 2);
        addEdge(g, 1, 3);
        addEdge(g, 2, 4);
        addEdge(g, 3, 5);

        List<Integer> bfsOrder = bfs(g, n, 1);
        List<Integer> dfsOrder = dfs(g, n, 1);

        System.out.println("bfs=" + bfsOrder);
        System.out.println("dfs=" + dfsOrder);
    }

    private static void addEdge(List<Integer>[] g, int a, int b) {
        g[a].add(b);
        g[b].add(a);
    }

    private static List<Integer> bfs(List<Integer>[] g, int n, int start) {
        boolean[] vis = new boolean[n + 1];
        Deque<Integer> q = new ArrayDeque<>();
        List<Integer> order = new ArrayList<>();

        vis[start] = true;
        q.add(start);
        while (!q.isEmpty()) {
            int v = q.poll();
            order.add(v);
            for (int nv : g[v]) {
                if (!vis[nv]) {
                    vis[nv] = true;
                    q.add(nv);
                }
            }
        }
        return order;
    }

    private static List<Integer> dfs(List<Integer>[] g, int n, int start) {
        boolean[] vis = new boolean[n + 1];
        Deque<Integer> st = new ArrayDeque<>();
        List<Integer> order = new ArrayList<>();

        st.push(start);
        while (!st.isEmpty()) {
            int v = st.pop();
            if (vis[v]) continue;
            vis[v] = true;
            order.add(v);

            // 스택은 역순으로 넣어야 작은 번호부터 처리되는 경우가 많음
            List<Integer> adj = g[v];
            for (int i = adj.size() - 1; i >= 0; i--) {
                int nv = adj.get(i);
                if (!vis[nv]) st.push(nv);
            }
        }
        return order;
    }
}
