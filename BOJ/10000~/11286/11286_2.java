import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

        // 절댓값 기준 + 같으면 실제 값 기준으로 정렬하는 우선순위 큐
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {
            int absA = Math.abs(a);
            int absB = Math.abs(b);

			// return 값 음수 : 정렬순서 a,b 순서
			// return 값 0 : a,b 동등
			// return 값 양수 : 정렬순서 b,a 순서

            if (absA != absB) {
                return absA - absB; // 절댓값이 작은 게 먼저
            } else {
                return a - b;       // 절댓값 같으면 실제 값이 작은 게 먼저 (음수가 먼저)
            }
        });
		
		StringBuilder sb = new StringBuilder();

		for (int i=0; i<n; i++){
			int x = Integer.parseInt(br.readLine());

			if (x != 0) {
				// 값 추가
				pq.offer(x);
			} else {
				if (pq.isEmpty()) {
					sb.append(0).append("\n");
				} else {
					sb.append(pq.poll()).append("\n");
				}
			}
		}

		System.out.println(sb.toString());
	}
	
}
