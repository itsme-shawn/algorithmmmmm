import java.io.*;
import java.util.StringTokenizer;

class Main {
	// 입출력 담당 main
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine().trim());
		int[] arr = new int[n + 1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		int m = Integer.parseInt(br.readLine().trim());
		int[][] queries = new int[m][2];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			queries[i][0] = Integer.parseInt(st.nextToken());
			queries[i][1] = Integer.parseInt(st.nextToken());
		}
		String result = solution(n, arr, queries);

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result);
		bw.flush();
	}

	public static String solution(int n, int[] arr, int[][] queries) {
		// dp[s][e] = s~e 구간이 팰린드롬이면 true
		boolean[][] dp = new boolean[n + 1][n + 1];
		// 길이 1은 항상 팰린드롬
		for (int i = 1; i <= n; i++) {
			dp[i][i] = true;
		}
		// 길이 2는 두 값이 같을 때만 팰린드롬
		for (int i = 1; i + 1 <= n; i++) {
			if (arr[i] == arr[i + 1]) {
				dp[i][i + 1] = true;
			}
		}
		// 길이 3 이상은 양 끝이 같고 내부가 팰린드롬이면 성립
		for (int len = 3; len <= n; len++) {
			for (int s = 1; s + len - 1 <= n; s++) {
				int e = s + len - 1;
				if (arr[s] == arr[e] && dp[s + 1][e - 1]) {
					dp[s][e] = true;
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < queries.length; i++) {
			int s = queries[i][0];
			int e = queries[i][1];
			sb.append(dp[s][e] ? 1 : 0).append('\n');
		}
		return sb.toString();
	}
}
