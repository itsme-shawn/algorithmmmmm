import java.io.*;
import java.util.*;

public class DPGridPaths {
    public static void main(String[] args) throws Exception {
        // 설명: 2차원 격자에서 경로 수 DP
        // 시간복잡도: O(N * M)
        // 주의사항: 경로 수가 커질 수 있으니 long/모듈러 처리 고려
        // 예시 입력:
        // 3 3
        // 0 0 0
        // 0 1 0
        // 0 0 0
        // 예상 출력:
        // 2

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] block = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                block[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long[][] dp = new long[n][m];
        if (block[0][0] == 0) dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (block[i][j] == 1) continue;
                if (i > 0) dp[i][j] += dp[i - 1][j];
                if (j > 0) dp[i][j] += dp[i][j - 1];
            }
        }

        System.out.println(dp[n - 1][m - 1]);
    }
}
