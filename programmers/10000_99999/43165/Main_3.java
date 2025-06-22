
import java.io.*;
import java.util.*;

// BFS
public class Main_3 {

    public static int solution(int[] numbers, int target) {
        int answer = 0;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int level = cur[0];
            int sum = cur[1];
            if (level == numbers.length) {
                if (sum == target) {
                    answer++;
                }
                continue;
            }
            q.offer(new int[]{level + 1, sum + numbers[level]});
            q.offer(new int[]{level + 1, sum - numbers[level]});
        }

        return answer;

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
