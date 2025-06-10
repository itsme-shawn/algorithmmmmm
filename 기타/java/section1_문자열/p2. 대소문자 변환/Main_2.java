
import java.io.*;
import java.util.*;

public class Main_2 {

    public static String solution(String str) {
        // String 에 더하기 연산으로 붙이기
        String ans = "";
        for (char x : str.toCharArray()) {
            if (Character.isLowerCase(x)) {
                ans += Character.toUpperCase(x);
            } else {
                ans += Character.toLowerCase(x);
            }
        }

        return ans;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("in_1.txt"));
        String str = sc.next();
        sc.close();
        System.out.println(solution(str));
    }

}
