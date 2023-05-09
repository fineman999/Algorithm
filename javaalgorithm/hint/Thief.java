package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Thief {
    private static int n;
    private static int k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        getNAndK(br);
        int[][] boxes = new int[n][2];
        int[] bags = new int[k];
        getBoxes(br, boxes);
        getBags(br, bags);

        Arrays.sort(bags);
        Arrays.sort(boxes, Comparator.comparingInt(o -> o[0]));

        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        long answer = 0L;
        int j = 0;
        for (int bag : bags) {
            while (j < n && boxes[j][0] <= bag) {
                heap.add(boxes[j++][1]);
            }
            if(!heap.isEmpty()) {
                answer += heap.poll();
            }
        }

        System.out.println(answer);
        br.close();

    }

    private static void getBags(BufferedReader br, int[] bags) throws IOException {
        for (int i = 0; i < k; i++) {
            bags[i] = Integer.parseInt(br.readLine());
        }
    }

    private static void getBoxes(BufferedReader br, int[][] boxes) throws IOException {
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            boxes[i][0] = Integer.parseInt(st.nextToken());
            boxes[i][1] = Integer.parseInt(st.nextToken());
        }
    }

    private static void getNAndK(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
         n = Integer.parseInt(st.nextToken());
         k = Integer.parseInt(st.nextToken());
    }
}
