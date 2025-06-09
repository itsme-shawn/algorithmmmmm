
import java.io.*;
import java.util.*;

public class p1 {

    public static int solution(String str, char t) {
        // System.out.print(str);
        // System.out.print(t);

        str = str.toUpperCase();
        t = Character.toUpperCase(t);

        int ans = 0;

        for (char x : str.toCharArray()) {
            if (x == t) {
                ans++;
            }
        }

        return ans;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("1.txt"));
        String str = sc.next();
        char c = sc.next().charAt(0);
        sc.close();
        System.out.println(solution(str, c));
    }

}
