package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class CuriousDecimal {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        dfs(n, cnt, "");

    }

    private static void dfs(int n, int cnt, String result) {
        if (cnt == n) {
            System.out.println(result);
            return;
        }
        for (int i = 0; i < 10; i++) {
            if (Objects.equals(result, "") && isDecimal(i)) dfs(n, cnt + 1, result + i);
            else if(isDecimal(Integer.parseInt(result + i))) dfs(n, cnt + 1, result + i);
        }

    }

    private static boolean isDecimal(int k) {
        if (k < 2) {
            return false;
        }
        int sqrt = (int) Math.sqrt(k);
        for (int i = 2; i < sqrt + 1; i++) {
            if (k % i == 0) return false;
        }
        return true;
    }

}
