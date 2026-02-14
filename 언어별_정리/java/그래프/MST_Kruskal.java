import java.util.*;

public class MST_Kruskal {
    public static void main(String[] args) {
        // 설명: 최소 신장 트리 (크루스칼)
        // 시간복잡도: O(E log E) (간선 정렬 포함)
        // 주의사항: 그래프가 비연결이면 MST가 아닌 최소 신장 숲이 됨
        // 그래프(무방향):
        // 1-2(3), 1-3(1), 2-3(2), 2-4(4), 3-4(5)
        // 예상 출력:
        // mstWeight=7

        int n = 4;
        int[][] edges = {
            {1, 2, 3},
            {1, 3, 1},
            {2, 3, 2},
            {2, 4, 4},
            {3, 4, 5}
        };

        Arrays.sort(edges, Comparator.comparingInt(a -> a[2]));

        int[] parent = new int[n + 1];
        int[] size = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        int total = 0;
        int used = 0;
        for (int[] e : edges) {
            int a = e[0], b = e[1], w = e[2];
            if (union(parent, size, a, b)) {
                total += w;
                used++;
                if (used == n - 1) break;
            }
        }

        System.out.println("mstWeight=" + total);
    }

    private static int find(int[] parent, int x) {
        if (parent[x] == x) return x;
        parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    private static boolean union(int[] parent, int[] size, int a, int b) {
        int ra = find(parent, a);
        int rb = find(parent, b);
        if (ra == rb) return false;
        if (size[ra] < size[rb]) {
            parent[ra] = rb;
            size[rb] += size[ra];
        } else {
            parent[rb] = ra;
            size[ra] += size[rb];
        }
        return true;
    }
}
