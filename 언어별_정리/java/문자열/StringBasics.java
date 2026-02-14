import java.util.*;

public class StringBasics {
    public static void main(String[] args) {
        // 설명: 문자열 기본 (카운트, 치환, 삭제, 부분문자열 인덱스)
        // 시간복잡도: O(N) ~ O(N * L)
        // 주의사항: 문자열은 불변이라 반복 연결은 StringBuilder 사용 권장
        // 예상 출력:
        // 4
        // XcX
        // bcb
        // [0, 4]

        String s = "abacaba";

        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a') cnt++;
        }

        String replaced = s.replace("aba", "X");
        String removed = s.replace("a", "");

        List<Integer> idx = new ArrayList<>();
        String target = "aba";
        for (int i = 0; i + target.length() <= s.length(); i++) {
            if (s.startsWith(target, i)) idx.add(i);
        }

        System.out.println(cnt);
        System.out.println(replaced);
        System.out.println(removed);
        System.out.println(idx);
    }
}
