import java.util.*;

public class HashMapCounting {
    public static void main(String[] args) {
        // 설명: 해시맵으로 개수 세기 (순서 고정 위해 LinkedHashMap 사용)
        // 시간복잡도: 평균 O(N) (삽입/조회 O(1))
        // 주의사항: 순서가 필요하면 LinkedHashMap/TreeMap 사용
        // 예상 출력:
        // {1=1, 2=2, 3=3}

        int[] nums = {1, 2, 2, 3, 3, 3};
        Map<Integer, Integer> count = new LinkedHashMap<>();

        for (int x : nums) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        System.out.println(count);
    }
}
