import java.util.*;

public class PrefixSum1D {
    public static void main(String[] args) {
        // 설명: 1차원 누적합으로 구간합 빠르게 계산
        // 시간복잡도: 전처리 O(N), 쿼리 O(1)
        // 주의사항: 1-based/0-based 인덱스 혼동과 합 오버플로에 주의
        // 예시 입력(하드코딩):
        // arr = [1, 2, 3, 4, 5], query [2,4]
        // 예상 출력:
        // sum(2..4)=12

        int[] arr = {1, 2, 3, 4, 5};
        int n = arr.length;
        int[] ps = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            ps[i] = ps[i - 1] + arr[i - 1];
        }

        int l = 2, r = 4; // 1-based index
        int sum = ps[r] - ps[l - 1];
        System.out.println("sum(2..4)=" + sum);
    }
}
