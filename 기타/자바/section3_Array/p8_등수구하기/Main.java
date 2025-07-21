
import java.io.*;
import java.util.*;

// 자바 답안 템플릿
public class Main {

    public static String solution(int n, int[] numbers) {
        // System.out.println(Arrays.toString(numbers));
        int[] ans = new int[n];
        Arrays.fill(ans, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (numbers[i] < numbers[j]) {
                        ans[i]++;
                    }
                }

            }
        }

        return Arrays.toString(ans); 
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("1.txt"));
        int n = Integer.parseInt(sc.nextLine());
        String line = sc.nextLine();
        String[] tokens = line.split(" ");

        int[] numbers = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
            numbers[i] = Integer.parseInt(tokens[i]);
        }

        sc.close();
        System.out.println(solution(n, numbers));
    }

}
