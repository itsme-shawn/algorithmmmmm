package 기타.java.section1_문자열.p2_대소문자변환;
import java.io.*;
import java.util.*;

public class Main {

    public static String solution(String str) {
        StringBuilder sb = new StringBuilder();

        for (char ch : str.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                sb.append(Character.toLowerCase(ch));
            } else {
                sb.append(Character.toUpperCase(ch));
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("in_1.txt"));
        String str = sc.next();
        sc.close();
        System.out.println(solution(str));
    }

}
