import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		// 첫 줄: 9 2
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		// 둘째 줄: 3 2 5 5 6 4 4 5 7
		st = new StringTokenizer(br.readLine());

		int[] freq = new int[200001];

		for (int i=0; i<200001; i++){
			freq[i] = 0;
		}

		Deque<Integer> deq = new ArrayDeque<>();
		int num, best = 0;

		for (int i=0; i<N; i++){
			num = Integer.parseInt(st.nextToken());
			deq.addLast(num);
			freq[num] += 1;

			if (freq[num] > K) {
				while (freq[num] > K) {
					int pop = deq.pollFirst();
					freq[pop] -= 1;
				}
			}

			best = Math.max(best, deq.size());

		}

		System.out.println(best);

	}

}
