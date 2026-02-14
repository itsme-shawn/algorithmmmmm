import java.util.*;

public class CopyAndConstants {
    public static void main(String[] args) {
        // 설명: 상수값, 얕은/깊은 복사
        // 시간복잡도: 복사 O(N)
        // 주의사항: 얕은 복사와 깊은 복사의 차이를 주의
        // 예상 출력:
        // max=2147483647, min=-2147483648
        // a=[9, 2, 3]
        // deep=[1, 2, 3]

        int max = Integer.MAX_VALUE;
        int min = Integer.MIN_VALUE;

        int[] a = {1, 2, 3};
        int[] shallow = a; // 같은 배열 참조
        int[] deep = Arrays.copyOf(a, a.length);

        shallow[0] = 9;

        System.out.println("max=" + max + ", min=" + min);
        System.out.println("a=" + Arrays.toString(a));
        System.out.println("deep=" + Arrays.toString(deep));
    }
}
