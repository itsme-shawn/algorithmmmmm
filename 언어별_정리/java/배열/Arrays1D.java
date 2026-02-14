import java.util.*;

public class Arrays1D {
    public static void main(String[] args) {
        // 설명: 1차원 배열 기본 사용법 (정렬, 이진탐색, 복사, 채우기)
        // 시간복잡도: 정렬 O(N log N), 탐색 O(log N), 복사/채우기 O(N)
        // 주의사항: binarySearch는 정렬된 배열에서만 정확하며, 결과 음수 규칙 주의
        // 예상 출력:
        // sorted=[1, 3, 4, 5, 9]
        // indexOf3=1
        // copy=[1, 3, 4, 5, 9]
        // filled=[7, 7, 7, 7, 7]

        int[] arr = {5, 3, 9, 1, 4};

        Arrays.sort(arr);

        int idx = Arrays.binarySearch(arr, 3); // 정렬된 배열에서 3의 인덱스

        int[] copy = Arrays.copyOf(arr, arr.length);

        int[] filled = new int[5];
        Arrays.fill(filled, 7);

        System.out.println("sorted=" + Arrays.toString(arr));
        System.out.println("indexOf3=" + idx);
        System.out.println("copy=" + Arrays.toString(copy));
        System.out.println("filled=" + Arrays.toString(filled));
    }
}
