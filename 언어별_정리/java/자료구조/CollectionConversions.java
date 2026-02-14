import java.util.*;

public class 컬렉션_형변환 {
    public static void main(String[] args) {
        // 설명: 배열 <-> 리스트, 컬렉션 간 변환
        // 시간복잡도: O(N)
        // 주의사항: 기본형 배열은 Arrays.asList로 바로 변환되지 않음(박싱 필요)
        // 예상 출력:
        // list=[1, 2, 3]
        // arr=[1, 2, 3]
        // set=[1, 2, 3]

        int[] arr = {1, 2, 3};

        // 배열 -> 리스트 (Integer 리스트)
        List<Integer> list = new ArrayList<>();
        for (int x : arr) list.add(x);
        System.out.println("list=" + list);

        // 리스트 -> 배열 (int[])
        int[] arr2 = new int[list.size()];
        for (int i = 0; i < list.size(); i++) arr2[i] = list.get(i);
        System.out.println("arr=" + Arrays.toString(arr2));

        // 리스트 -> 집합
        Set<Integer> set = new LinkedHashSet<>(list);
        System.out.println("set=" + set);
    }
}
