
import java.io.*;
import java.util.*;

// 자바 답안 템플릿
public class Main {

    static int target = 5;
    static boolean[] visited;
    static int[][] graph;
    static List<Integer> path;
    static int cnt = 0; // 최종 경로 개수
    static int N;

    public static void dfs(int v) {
        if (v == target) {
            cnt++;
            System.out.println("path: " + path); // 경로 출력
        } else {
            for (int i = 1; i <= N; i++) {
                if (!visited[i] && graph[v][i] == 1) {
                    path.add(i);
                    visited[i] = true;
                    dfs(i);
                    path.remove(path.size() - 1);
                    visited[i] = false;
                }
            }
        }
    }

    public static int solution(int n, int[][] edges) {
        graph = new int[n + 1][n + 1];
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            graph[from][to] = 1;
        }

        // // 그래프 출력
        // for (int i = 1; i < n + 1; i++) {
        //     for (int j = 1; j < n + 1; j++) {
        //         System.out.print(graph[i][j] + " ");
        //     }
        //     System.out.println();
        // }
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
