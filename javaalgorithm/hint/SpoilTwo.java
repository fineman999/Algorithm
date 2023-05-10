package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class SpoilTwo {
    private static int n;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] spoils = new int[n];
        List<Integer> minus = new ArrayList<>();
        List<Integer> plus = new ArrayList<>();

        // 초기값 설정
        setInit(br, spoils, minus, plus);

        // 정렬
        if (!plus.isEmpty()) plus.sort(Comparator.naturalOrder());
        if (!minus.isEmpty()) minus.sort(Comparator.reverseOrder());

        int minusIdx = 0;
        int plusIdx = 0;
        int minusLen = minus.size();
        int plusLen = plus.size();
        int[] answer = new int[2];
        answer[1] = Integer.MAX_VALUE;
        List<Integer> temp = new ArrayList<>();
        int cnt = 0;

        while (minusIdx < minusLen || plusIdx < plusLen) {
            if (plusIdx >= plusLen || (minusIdx < minusLen && Math.abs(minus.get(minusIdx)) <= plus.get(plusIdx))) {
                temp.add(minus.get(minusIdx));
                minusIdx++;
            } else {
                temp.add(plus.get(plusIdx));
                plusIdx++;
            }
            cnt++;
            if (cnt > 1) {
                if (Math.abs(temp.get(cnt-1) + temp.get(cnt - 2)) < Math.abs(answer[0] + answer[1])) {
                    answer[0] = temp.get(cnt - 1);
                    answer[1] = temp.get(cnt - 2);
                }
            }
        }

        Arrays.sort(answer);
        System.out.println(answer[0] + " " + answer[1]);
    }

    private static void setInit(BufferedReader br, int[] spoils, List<Integer> minus, List<Integer> plus) throws IOException {
        setSpoils(spoils, br);
        setMinus(spoils, minus);
        setPlus(spoils, plus);
    }

    private static void setPlus(int[] spoils, List<Integer> plus) {
        for (int spoil : spoils) {
            if (spoil >= 0) {
                plus.add(spoil);
            }
        }
    }

    private static void setMinus(int[] spoils, List<Integer> minus) {
        for (int spoil : spoils) {
            if (spoil < 0) {
                minus.add(spoil);
            }
        }
    }

    private static void setSpoils(int[] spoils, BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            spoils[i] = Integer.parseInt(st.nextToken());
        }
    }
}
