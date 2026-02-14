import java.util.*;

public class GraphRepresentation {
    public static void main(String[] args) {
        // 설명: 인접행렬 vs 인접리스트
        // 시간복잡도: 행렬 공간 O(N^2), 리스트 공간 O(N + E)
        // 주의사항: 그래프 밀도에 따라 표현 선택(희소=리스트, 조밀=행렬)
        // 예시 그래프: 1-2, 1-3, 2-4
        // 예상 출력:
        // matrix[1][2]=true, list[1]=[2, 3]

        int n = 4;

        // 인접행렬
        boolean[][] matrix = new boolean[n + 1][n + 1];
        matrix[1][2] = matrix[2][1] = true;
        matrix[1][3] = matrix[3][1] = true;
        matrix[2][4] = matrix[4][2] = true;

        // 인접리스트
        List<Integer>[] list = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) list[i] = new ArrayList<>();
        list[1].add(2); list[2].add(1);
        list[1].add(3); list[3].add(1);
        list[2].add(4); list[4].add(2);

        System.out.println("matrix[1][2]=" + matrix[1][2] + ", list[1]=" + list[1]);
    }
}
