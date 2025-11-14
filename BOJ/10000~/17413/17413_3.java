import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s = br.readLine();
        boolean inTag = false;
        StringBuilder word = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (ch == '<') {
                // 기존 단어 뒤집고 출력
                sb.append(word.reverse());
                word.setLength(0);

                inTag = true;
                sb.append(ch);
            } else if (ch == '>') {
                inTag = false;
                sb.append(ch);
            } else if (inTag) {
                sb.append(ch);
            } else {
                if (ch == ' ') {
                    sb.append(word.reverse());
                    word.setLength(0);
                    sb.append(' ');
                } else {
                    word.append(ch);
                }
            }
        }

        sb.append(word.reverse());
        System.out.println(sb.toString());
    }
}