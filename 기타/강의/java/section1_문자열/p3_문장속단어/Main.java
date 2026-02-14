
import java.io.*;
import java.util.*;

public class Main {

    public static String solution(String str) {
        String temp = "";
        int maxx = -1;
        String ans = "";
        for (char c : str.toCharArray()) {
            temp += c;
            if (c == ' ') {
                if (temp.length() - 1 > maxx) {
                    maxx = temp.length() - 1;
                    ans = temp;
                }
                temp = "";
            } else if (c == str.charAt(str.length() - 1)) {
                if (temp.length() > maxx) {
                    maxx = temp.length();
                    ans = temp;
                }
            }
        }

        return ans;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("in_1.txt"));
        String str = sc.nextLine();
        sc.close();
        System.out.println(solution(str));
    }

}
