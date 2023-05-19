package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Sushi {
    private static int n;
    private static int d;
    private static int k;
    private static int c;
    private static int[] sushi;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<Integer, Integer> diary = new HashMap<>();
        init(br, diary);


        if (diary.containsKey(c)) diary.put(c, diary.get(c) + 1);
        else diary.put(c, 1);

        int left = 0;
        int answer = 0;
        for (int i = k; i < n + k; i++) {
            answer = Math.max(answer, diary.size());

            diary.put(sushi[left], diary.get(sushi[left]) - 1);
            if (diary.get(sushi[left]) <= 0) diary.remove(sushi[left]);
            if (diary.containsKey(sushi[i])) diary.put(sushi[i], diary.get(sushi[i]) + 1);
            else diary.put(sushi[i], 1);
            left++;
        }

        System.out.println(answer);


    }

    private static void init(BufferedReader br, Map<Integer, Integer> diary) throws IOException {
        String[] belts = br.readLine().split(" ");
        n = Integer.parseInt(belts[0]);
        d = Integer.parseInt(belts[1]);
        k = Integer.parseInt(belts[2]);
        c = Integer.parseInt(belts[3]);
        sushi = new int[n + k];

        for (int i = 0; i < n; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        for (int i = n; i < n+k; i++) {
            sushi[i] = sushi[i-n];
            if (diary.containsKey(sushi[i])) diary.put(sushi[i], diary.get(sushi[i]) + 1);
            else diary.put(sushi[i], 1);
        }

    }
}
