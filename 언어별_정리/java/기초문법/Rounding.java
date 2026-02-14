public class Rounding {
    public static void main(String[] args) {
        // 설명: 반올림/내림/올림
        // 시간복잡도: O(1)
        // 주의사항: 부동소수점 오차로 경계값 반올림이 기대와 다를 수 있음
        // 예상 출력:
        // 3 2 2.0 3.0

        double x = 2.6;
        double y = 2.4;

        long r1 = Math.round(x);
        long r2 = Math.round(y);
        double f = Math.floor(x);
        double c = Math.ceil(y);

        System.out.println(r1 + " " + r2 + " " + f + " " + c);
    }
}
