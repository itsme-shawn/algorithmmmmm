import java.util.*;

public class SegmentTree {
    // 설명: 세그먼트 트리 (구간합)
    // 시간복잡도: 빌드 O(N), 쿼리 O(log N)
    // 주의사항: 트리 배열 크기(4N) 확보와 큰 합은 long 사용 고려
    // 예시: arr=[1,2,3,4,5]
    // 예상 출력:
    // sum(2..4)=9
    // sum(1..5)=15

    private static int[] tree;
    private static int n;

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        n = arr.length;
        tree = new int[n * 4];

        build(arr, 1, 0, n - 1);

        int sum1 = query(1, 0, n - 1, 1, 3); // 0-based [1..3]
        int sum2 = query(1, 0, n - 1, 0, 4);

        System.out.println("sum(2..4)=" + sum1);
        System.out.println("sum(1..5)=" + sum2);
    }

    private static void build(int[] arr, int node, int l, int r) {
        if (l == r) {
            tree[node] = arr[l];
            return;
        }
        int mid = (l + r) >>> 1;
        build(arr, node * 2, l, mid);
        build(arr, node * 2 + 1, mid + 1, r);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    private static int query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) >>> 1;
        return query(node * 2, l, mid, ql, qr) + query(node * 2 + 1, mid + 1, r, ql, qr);
    }
}
