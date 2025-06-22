
import java.io.*;
import java.util.*;

// 상태 배열에 덮어쓰는 DFS 방식
public class Main_1 {

    // 전역변수들
    static int maxL;
    static int targetNum;
    static int ans = 0;
    static int[] nums;
    static int[] cache;

    public static void dfs(int L) {
        if (L == maxL) {
            int temp = 0;
            for (int a : cache) {
                temp += a;
            }
            if (temp == targetNum) {
                ans++;
            }
            return;
        }

        cache[L] = nums[L];
        dfs(L + 1);

        cache[L] = -nums[L];
        dfs(L + 1);
    }

    public static int solution(int[] numbers, int target) {
        maxL = numbers.length;
        targetNum = target;
        nums = numbers;
        cache = new int[numbers.length];
        ans = 0;

        dfs(0);

        System.out.println("ans: " + ans);

        return ans;
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("1.txt"));
        // Scanner sc = new Scanner(System.in); // 실제 채점 시에는 이 줄 사용

        // 첫 줄: numbers 배열
        int[] numbers = Arrays.stream(sc.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // 둘째 줄: target 값
        int target = Integer.parseInt(sc.nextLine().trim());

        sc.close();

        // solution 함수 호출
        int result = solution(numbers, target);

        // 출력
        System.out.println(result);
    }

}
