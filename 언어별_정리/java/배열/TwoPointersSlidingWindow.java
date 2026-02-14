import java.util.*;

public class TwoPointersSlidingWindow {
    public static void main(String[] args) {
        // 설명: 투 포인터/슬라이딩 윈도우로 합이 S 이상인 최소 길이
        // 시간복잡도: O(N)
        // 주의사항: 모든 값이 양수일 때만 슬라이딩 윈도우가 유효
        // 예시 입력(하드코딩):
        // nums = [2, 3, 1, 2, 4, 3], S = 7
        // 예상 출력:
        // minLen=2 (부분합 4+3)

        int[] nums = {2, 3, 1, 2, 4, 3};
        int s = 7;

        int n = nums.length;
        int left = 0;
        int sum = 0;
        int best = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            sum += nums[right];
            while (sum >= s) {
                best = Math.min(best, right - left + 1);
                sum -= nums[left++];
            }
        }

        int ans = (best == Integer.MAX_VALUE) ? 0 : best;
        System.out.println("minLen=" + ans);
    }
}
