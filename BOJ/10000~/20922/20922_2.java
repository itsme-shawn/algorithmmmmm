import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Map<Integer, Integer> count = new HashMap<>();
        int best = 0;
        int left = 0;

        for (int right = 0; right < n; right++) {
            int v = nums[right];
            count.put(v, count.getOrDefault(v, 0) + 1);

            while (count.get(v) > k) {
                int lv = nums[left++];
                int c = count.get(lv) - 1;
                if (c == 0) count.remove(lv);
                else count.put(lv, c);
            }

            int len = right - left + 1;
            if (len > best) best = len;
        }

        System.out.println(best);
    }
}
