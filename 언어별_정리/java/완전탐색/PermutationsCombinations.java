import java.util.*;

public class PermutationsCombinations {
    private static void permute(int[] nums, boolean[] used, List<Integer> cur, List<List<Integer>> out) {
        if (cur.size() == nums.length) {
            out.add(new ArrayList<>(cur));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            cur.add(nums[i]);
            permute(nums, used, cur, out);
            cur.remove(cur.size() - 1);
            used[i] = false;
        }
    }

    private static void combine(int[] nums, int start, int k, List<Integer> cur, List<List<Integer>> out) {
        if (cur.size() == k) {
            out.add(new ArrayList<>(cur));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            cur.add(nums[i]);
            combine(nums, i + 1, k, cur, out);
            cur.remove(cur.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 설명: 순열/조합 직접 구현
        // 시간복잡도: 순열 O(N! * N), 조합 O(C(N,k) * k)
        // 주의사항: 입력 크기가 커지면 경우의 수가 급증하며, 중복 원소는 별도 처리 필요
        // 예상 출력:
        // perms=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        // combs=[[1, 2], [1, 3], [2, 3]]

        int[] nums = {1, 2, 3};

        List<List<Integer>> perms = new ArrayList<>();
        permute(nums, new boolean[nums.length], new ArrayList<>(), perms);

        List<List<Integer>> combs = new ArrayList<>();
        combine(nums, 0, 2, new ArrayList<>(), combs);

        System.out.println("perms=" + perms);
        System.out.println("combs=" + combs);
    }
}
