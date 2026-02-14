import java.util.*;

public class UnionFind {
    public static void main(String[] args) {
        // 설명: 서로소 집합(Union-Find) 기본
        // 시간복잡도: 거의 O(1) (아커만 역함수)
        // 주의사항: 경로 압축 + union by size/rank 사용을 권장
        // 예시 연산:
        // union(1,2), union(3,4), union(2,3)
        // 예상 출력:
        // same(1,4)=true

        int n = 5;
        int[] parent = new int[n + 1];
        int[] size = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        union(parent, size, 1, 2);
        union(parent, size, 3, 4);
        union(parent, size, 2, 3);

        boolean same = find(parent, 1) == find(parent, 4);
        System.out.println("same(1,4)=" + same);
    }

    private static int find(int[] parent, int x) {
        if (parent[x] == x) return x;
        parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    private static void union(int[] parent, int[] size, int a, int b) {
        int ra = find(parent, a);
        int rb = find(parent, b);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            parent[ra] = rb;
            size[rb] += size[ra];
        } else {
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }
}
