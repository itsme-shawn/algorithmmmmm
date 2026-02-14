import java.util.*;

public class SortingWithComparator {
    public static void main(String[] args) {
        // 설명: 2차원 정렬 (x 오름차순, y 내림차순)
        // 시간복잡도: O(N log N)
        // 주의사항: Comparator에서 동등(0) 처리와 우선순위를 일관되게 정의
        // 예상 출력:
        // [[1, 5], [1, 2], [2, 3], [2, 1]]

        int[][] pts = {{2, 3}, {1, 5}, {2, 1}, {1, 2}};

        Arrays.sort(pts, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]);
        });

        System.out.println(Arrays.deepToString(pts));
    }
}
