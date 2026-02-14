
import java.io.*;
import java.util.*;

public class Main {

    public static String solution(String[] str) {
        String[] ans = new String[str.length];
        int i = 0;

        for (String s : str) {
            StringBuilder sb = new StringBuilder(s);
            sb.reverse();
            ans[i++] = sb.toString();
        }

        return Arrays.toString(ans);
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("in_1.txt"));
        int n = Integer.parseInt(sc.nextLine());
        String[] str = new String[n];
        for (int i = 0; i < n; i++) {
            str[i] = sc.nextLine();
        }
        sc.close();
        System.out.println(solution(str));
    }

}
