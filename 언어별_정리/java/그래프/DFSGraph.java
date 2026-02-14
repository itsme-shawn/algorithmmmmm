import java.io.*;
import java.util.*;

public class DFSGraph {
    private static List<Integer>[] g;
    private static boolean[] visited;

    private static void dfs(int v) {
        visited[v] = true;
        for (int nv : g[v]) {
            if (!visited[nv]) dfs(nv);
        }
    }

    public static void main(String[] args) throws Exception {
        // 설명: 그래프 DFS로 연결된 정점 수 세기
        // 시간복잡도: O(V + E)
        // 주의사항: 재귀 DFS는 깊은 그래프에서 스택 오버플로가 날 수 있음
        // 예시 입력:
        // 5 4
        // 1 2
        // 1 3
        // 3 4
        // 2 5
        // 예상 출력:
        // 5

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g[a].add(b);
            g[b].add(a);
        }

        visited = new boolean[n + 1];
        dfs(1);

        int count = 0;
        for (int i = 1; i <= n; i++) if (visited[i]) count++;
        System.out.println(count);
    }
}
