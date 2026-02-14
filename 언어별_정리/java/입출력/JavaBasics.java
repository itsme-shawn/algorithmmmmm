import java.io.*;
import java.util.*;

public class JavaBasics {
    public static void main(String[] args) throws Exception {
        // 설명: 가장 기본적인 입력 처리 흐름 (정수 N + 한 줄에 N개 정수)
        // 시간복잡도: O(N)
        // 주의사항: 입력이 많으면 BufferedReader/StringTokenizer 사용 권장
        // 예시 입력:
        // 5
        // 1 2 3 4 5
        // 예상 출력:
        // 15

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        long sum = 0;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            sum += x;
        }

        System.out.println(sum);
    }
}
