import java.util.*;

public class 이분탐색 {
    public static void main(String[] args) {
        // 설명: 이분 탐색 기본 (정렬된 배열에서 특정 값 찾기)
        // 시간복잡도: 정렬 O(N log N), 탐색 1회 O(log N)
        // 주의사항: 배열이 정렬되어 있어야 하며, mid 계산은 오버플로 방지((l + r) >>> 1)
        // 예상 출력:
        // arr=[1, 3, 4, 7, 9]
        // idx(4)=2
        // idx(6)=-4
        // (Arrays.binarySearch는 없으면 -(삽입위치+1) 반환)

        int[] arr = {7, 1, 9, 4, 3};
        Arrays.sort(arr);
        System.out.println("arr=" + Arrays.toString(arr));

        int idx1 = Arrays.binarySearch(arr, 4);
        int idx2 = Arrays.binarySearch(arr, 6);
        System.out.println("idx(4)=" + idx1);
        System.out.println("idx(6)=" + idx2);

        // 직접 구현 (left/right 포인터)
        int target = 9;
        int l = 0, r = arr.length - 1;
        int found = -1;
        while (l <= r) {
            int mid = (l + r) >>> 1;
            if (arr[mid] == target) {
                found = mid;
                break;
            } else if (arr[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        // 예상 출력: found(9)=4
        System.out.println("found(9)=" + found);
    }
}
