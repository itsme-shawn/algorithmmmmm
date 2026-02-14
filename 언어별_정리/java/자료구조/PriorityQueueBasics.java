import java.util.*;

public class PriorityQueueBasics {
    public static void main(String[] args) {
        // 설명: 우선순위큐(힙) 기본 사용법
        // 시간복잡도: 삽입/삭제 O(log N)
        // 주의사항: 기본은 최소힙이며, 최대힙은 Comparator 필요
        // 예상 출력:
        // min=1
        // max=5

        PriorityQueue<Integer> minPQ = new PriorityQueue<>();
        minPQ.add(5);
        minPQ.add(1);
        minPQ.add(3);

        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Collections.reverseOrder());
        maxPQ.add(5);
        maxPQ.add(1);
        maxPQ.add(3);

        System.out.println("min=" + minPQ.poll());
        System.out.println("max=" + maxPQ.poll());
    }
}
