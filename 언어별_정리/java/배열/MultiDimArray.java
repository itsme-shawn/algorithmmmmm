import java.util.*;

public class MultiDimArray {
    public static void main(String[] args) {
        // 설명: 2차원/3차원 배열, 깊은 복사
        // 시간복잡도: 복사 O(N * M)
        // 주의사항: 2차원 배열은 행 단위로 복사해야 깊은 복사됨
        // 예상 출력:
        // [[0, 7, 0], [0, 0, 0]]
        // [[0, 7, 0], [0, 0, 0]]

        int n = 2, m = 3;
        int[][] a = new int[n][m];
        a[0][1] = 7;

        int x = 2, y = 2, z = 2;
        int[][][] b = new int[x][y][z];
        b[1][0][1] = 9;

        int[][] copy = new int[n][m];
        for (int i = 0; i < n; i++) {
            copy[i] = Arrays.copyOf(a[i], m);
        }

        System.out.println(Arrays.deepToString(a));
        System.out.println(Arrays.deepToString(copy));
    }
}
