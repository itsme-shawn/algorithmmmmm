import java.util.*;

public class DequeBasics {
    public static void main(String[] args) {
        // 설명: 덱(Deque) 양쪽 삽입/삭제
        // 시간복잡도: 삽입/삭제 O(1)
        // 주의사항: ArrayDeque는 null 요소를 허용하지 않음
        // 예상 출력:
        // front=0, back=2, remain=[1]

        Deque<Integer> dq = new ArrayDeque<>();

        dq.addLast(1);
        dq.addLast(2);
        dq.addFirst(0);

        int front = dq.pollFirst();
        int back = dq.pollLast();

        System.out.println("front=" + front + ", back=" + back + ", remain=" + dq);
    }
}
