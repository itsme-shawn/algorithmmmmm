import java.util.*;

public class DynamicProgrammingIntro {
    public static void main(String[] args) {
        // 설명: DP 기본 예시 (피보나치)
        // 시간복잡도: O(N)
        // 주의사항: 기저값 설정과 오버플로(큰 N은 long) 주의
        // 예상 출력:
        // 55

        int n = 10;
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        System.out.println(dp[n]);
    }
}
