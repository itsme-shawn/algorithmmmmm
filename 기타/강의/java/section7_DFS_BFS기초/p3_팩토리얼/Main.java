
import java.io.*;
import java.util.*;

// 자바 답안 템플릿
public class Main {

    public static int DFS(int n) {
        if (n == 1) {
            return 1;
        } else {
            return n * DFS(n - 1);
        }
    }

    public static int solution(int num) {
        return DFS(num);
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(System.in);
        // Scanner sc = new Scanner(new File("1.txt"));
        int num = sc.nextInt();
        sc.close();
        System.out.println(solution(num));
    }

}
