import java.util.*;

public class FenwickTree {
    // 설명: 펜윅 트리 (구간합)
    // 시간복잡도: 갱신/쿼리 O(log N), 초기화 O(N log N)
    // 주의사항: 인덱스가 1-based이며, 큰 합은 long 사용 고려
    // 예시: arr=[1,2,3,4,5]
    // 예상 출력:
    // sum(1..3)=6
    // sum(1..5)=15

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int n = arr.length;

        int[] bit = new int[n + 1];
        for (int i = 0; i < n; i++) {
            add(bit, i + 1, arr[i]);
        }

        int sum1 = prefix(bit, 3);
        int sum2 = prefix(bit, 5);

        System.out.println("sum(1..3)=" + sum1);
        System.out.println("sum(1..5)=" + sum2);
    }

    private static void add(int[] bit, int idx, int delta) {
        while (idx < bit.length) {
            bit[idx] += delta;
            idx += idx & -idx;
        }
    }

    private static int prefix(int[] bit, int idx) {
        int sum = 0;
        while (idx > 0) {
            sum += bit[idx];
            idx -= idx & -idx;
        }
        return sum;
    }
}
