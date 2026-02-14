import java.util.*;

public class ArrayListBasics {
    public static void main(String[] args) {
        // 설명: ArrayList 기본 (추가, 삭제, 정렬)
        // 시간복잡도: 추가 평균 O(1), 삭제 O(N), 정렬 O(N log N)
        // 주의사항: remove(int)와 remove(Object) 오버로드에 주의
        // 예상 출력:
        // [5, 3]

        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(1);
        list.add(5);
        list.add(1);

        list.remove(1); // 인덱스 1 삭제
        list.remove(Integer.valueOf(1)); // 값 1 삭제

        list.sort(Collections.reverseOrder());

        System.out.println(list);
    }
}
