import java.io.*;
import java.util.*;

public class ComplexInputPatterns {
    public static void main(String[] args) throws Exception {
        // 설명: 여러 패턴의 입력을 한 코드에서 다루는 예제
        // 시간복잡도: O(총 토큰 수)
        // 주의사항: EOF 처리와 빈 줄 스킵 로직을 명확히 해야 함
        // 예시 입력:
        // 3
        // 1 2
        // 3 4
        // 5 6
        // 7 8 9
        // 10
        // 예상 출력:
        // 55
        // (앞의 3줄: 21, EOF까지 추가 합: 34, 총합: 55)

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sum += a + b;
        }

        String line;
        int tailSum = 0;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;
            st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                tailSum += Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(sum + tailSum);
    }
}
