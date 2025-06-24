
import java.io.*;
import java.util.*;

public class Main {

    public static String solution(String str) {
        char[] ch = str.toCharArray();
        int lt = 0, rt = ch.length - 1;
        System.out.println((int) 'A');
        while (lt <= rt) {
            if (!Character.isLetter(ch[lt])) {
                lt++;
            } else if (!Character.isLetter(ch[rt])) {
                rt--;
            } else {
                char tmp = ch[lt];
                ch[lt] = ch[rt];
                ch[rt] = tmp;
                lt++;
                rt--;
            }
        }

        // return new String(ch);
        return new String(ch);
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("in_1.txt"));
        String str = sc.nextLine();
        sc.close();
        System.out.println(solution(str));
    }

}
