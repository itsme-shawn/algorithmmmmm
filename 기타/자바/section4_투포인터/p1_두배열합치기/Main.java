
import java.io.*;
import java.util.*;

// 자바 답안 템플릿
public class Main {

    public static String solution(int n, int m, int[] arr1, int[] arr2) {
        System.out.println("n : " + n + " m : " + m + " arr 1 : " + Arrays.toString(arr1) + ", " + Arrays.toString(arr2));

        int i = 0, j = 0, k = 0;
        int[] merge = new int[n + m];
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] <= arr2[j]) {
                merge[k++] = arr1[i++];
            } else {
                merge[k++] = arr2[j++];
            }
        }

        if (i == arr1.length) {
            for (k = i + j; k < n + m; k++) {
                merge[k] = arr2[j++];
            }
        }
        if (j == arr2.length) {
            for (k = i + j; k < n + m; k++) {
                merge[k] = arr1[i++];
            }
        }

        return Arrays.toString(merge);

    }

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new File("1.txt"));

        int n = sc.nextInt();

        int[] arr1 = new int[n];

        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }

        int m = sc.nextInt();

        int[] arr2 = new int[m];

        for (int i = 0; i < m; i++) {
            arr2[i] = sc.nextInt();
        }

        sc.close();
        System.out.println(solution(n, m, arr1, arr2));
    }

}
