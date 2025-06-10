
import java.io.*;
import java.util.*;

public class Main_1 {

    public static String solution(String str) {
        // ascii 코드 이용
        String ans = "";
        for (char x : str.toCharArray()) {
            if (x >= 'a' && x <= 'z') { // 소문자로 만들기
                ans += (char) (x - ('a' - 'A')); // 'A':65 , 'a':97
            } else {
                ans += (char) (x + ('a' - 'A')); // 대문자로 만들기
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
