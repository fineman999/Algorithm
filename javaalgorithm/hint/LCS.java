package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class LCS {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] A = init(br);
        char[] B = init(br);

        int[] dp = new int[A.length];

        for (char c : B) {
            int tmp = 0;
            for (int j = 0; j < A.length; j++) {
                if (tmp < dp[j]) tmp = dp[j];
                else if (c == A[j]) dp[j] = Math.max(dp[j], tmp + 1);

            }
        }

        int answer = Arrays.stream(dp).max().orElse(1);
        System.out.println(answer);
    }

    public static char[] init(BufferedReader br) throws IOException {
        String A = br.readLine();
        return A.toCharArray();
    }

}
