import java.util.*;

public class TypeCastingCharNumber {
    public static void main(String[] args) {
        // 설명: 숫자 <-> 문자/문자열 변환
        // 시간복잡도: O(1)
        // 주의사항: 문자-숫자 변환 시 유효 범위와 NumberFormatException에 주의
        // 예상 출력:
        // a=123, b=456
        // sum=579
        // c=7, d=65, e=65

        String s1 = "123";
        String s2 = "456";
        int a = Integer.parseInt(s1);
        int b = Integer.parseInt(s2);
        System.out.println("a=" + a + ", b=" + b);
        System.out.println("sum=" + (a + b));

        int num = 7;
        String c = String.valueOf(num); // int -> String

        char ch = 'A';
        int d = ch - '0'; // 문자 '0' 기준 차이
        int e = (int) ch; // 아스키/유니코드 코드값

        System.out.println("c=" + c + ", d=" + d + ", e=" + e);
    }
}
