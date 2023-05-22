package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class WaterBath {
    private static int n;
    private static int[] parent;
    private static PriorityQueue<Rice> queue;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        setParent();
        init(br);

        int cnt = 0;
        int answer = 0;
        while (!queue.isEmpty()) {
            Rice rice = queue.poll();
            int parentStart = getParent(rice.getStart());
            int parentEnd = getParent(rice.getEnd());

            if (parentStart != parentEnd) {
                if (parentStart > parentEnd) parent[parentStart] = parentEnd;
                else parent[parentEnd] = parentStart;
                cnt += 1;
                answer += rice.getValue();
                if (cnt == n + 1) {
                    break;
                }
            }
        }
        System.out.println(answer);
    }

    private static int getParent(int node) {
        int start = node;
        while (node != parent[node]) {
            node = parent[node];
        }
        parent[start] = node;
        return node;
    }

    private static void setParent() {
        parent = new int[n + 1];
        for (int i = 0; i < n+1; i++) {
            parent[i] = i;
        }
    }


    private static void init(BufferedReader br) throws IOException {
        int[] well = new int[n];
        for (int i = 0; i < n; i++) {
            well[i] = Integer.parseInt(br.readLine());
        }

        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        queue = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            queue.add(new Rice(well[i], 0, i + 1));
        }
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                queue.add(new Rice(arr[i][j], i + 1, j + 1));
            }
        }
    }

    static class Rice implements Comparable<Rice> {
        private final int value;
        private final int start;
        private final int end;

        public Rice(int value, int start, int end) {
            this.value = value;
            this.start = start;
            this.end = end;
        }

        public int getEnd() {
            return end;
        }

        public int getStart() {
            return start;
        }

        public int getValue() {
            return value;
        }

        @Override
        public int compareTo(Rice o) {
            return Integer.compare(this.value, o.value);
        }
    }
}
