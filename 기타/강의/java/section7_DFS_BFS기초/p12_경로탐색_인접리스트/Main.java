
import java.io.*;
import java.util.*;

// 자바 답안 템플릿
public class Main {

    static int target = 5;
    static boolean[] visited;
    // static int[][] graph; // 인접행렬 대신 아래의 인접리스트로 대체
    static List<List<Integer>> graph;
    static List<Integer> path;
    static int cnt = 0; // 최종 경로 개수
    static int N;

    public static void dfs(int v) {
        if (v == target) {
            cnt++;
            System.out.println("path: " + path); // 경로 출력
        } else {
            for (int nv : graph.get(v)) {
                if (!visited[nv]) {
                    path.add(nv);
                    visited[nv] = true;
                    dfs(nv);
                    path.remove(path.size() - 1);
                    visited[nv] = false;
                }
            }
        }
    }

    public static int solution(int n, int[][] edges) {
        graph = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            graph.get(from).add(to);
        }

        visited = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            visited[i] = false;
        }
        path = new ArrayList<>();
        N = n;

        // dfs 실행
        visited[1] = true;
        path.add(1);
        dfs(1);
        System.out.println("cnt: " + cnt);

        return cnt;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("1.txt"));

        int n = sc.nextInt(); // 정점 개수
        int m = sc.nextInt(); // 간선 개수

        int[][] edges = new int[m][2]; // 간선 정보

        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt(); // 시작 노드
            edges[i][1] = sc.nextInt(); // 도착 노드
        }

        sc.close();
        System.out.println(solution(n, edges));
    }

}
