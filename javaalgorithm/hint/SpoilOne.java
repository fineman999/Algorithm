package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class SpoilOne {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = initN(br);
        int[] arr = initIntArr(N, br);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        initPointers(arr, left, right);

        if(!left.isEmpty())left.sort(Comparator.reverseOrder());
        if(!right.isEmpty()) right.sort(Comparator.naturalOrder());


        List<Integer> dp = new ArrayList<>();
        int[] answer = {0, Integer.MAX_VALUE};

        int cnt = 0;
        int right_index = 0;
        int left_index = 0;
        while (left_index < left.size() || right_index < right.size()) {
            if (left_index >= left.size() || right_index < right.size() && right.get(right_index) < Math.abs(left.get(left_index))) {
                dp.add(right.get(right_index));
                right_index += 1;
            }
            else {
                dp.add(left.get(left_index));
                left_index += 1;
            }
            cnt += 1;
            getAnswer(dp, answer, cnt);
        }
        printAnswer(answer);
    }

    private static void initPointers(int[] arr, List<Integer> left, List<Integer> right) {
        for (int item : arr) {
            if (item >= 0) right.add(item);
            else left.add(item);
        }
    }

    private static void printAnswer(int[] answer) {
        System.out.printf("%d %d%n", Math.min(answer[0], answer[1]), Math.max(answer[0], answer[1]));
    }

    private static void getAnswer(List<Integer> dp, int[] answer, int cnt) {
        if (cnt > 1 && Math.abs(dp.get(cnt - 1) + dp.get(cnt - 2)) < Math.abs(answer[0] + answer[1])) {
            answer[0] = dp.get(cnt - 1);
            answer[1] = dp.get(cnt - 2);
        }
    }

    private static int[] initIntArr(int n, BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i< n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        return arr;
    }

    private static int initN(BufferedReader br) throws IOException {
        return Integer.parseInt(br.readLine());
    }


}
