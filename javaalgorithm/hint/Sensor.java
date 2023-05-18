package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Sensor {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] sensors = new int[n];
        for (int i = 0; i < n; i++) {
            sensors[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(sensors);
        Integer[] direct = new Integer[n - 1];
        for (int i = 0; i < n-1 ; i++) {
            direct[i] = sensors[i+1] - sensors[i];
        }

        Arrays.sort(direct, Comparator.reverseOrder());

        int answer = 0;
        for (int i = k-1; i < n-1; i++) {
            answer += direct[i];
        }

        System.out.println(answer);
    }
}
