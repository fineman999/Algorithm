package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Toy {
    private static int n;
    private static int[] visited;
    private static List<List<Part>> graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        init(br);

        PriorityQueue<Part> q = new PriorityQueue<>();
        q.add(new Part(n, 1));

        int[] basic = new int[n + 1];

        while (!q.isEmpty()) {
            Part part = q.poll();
            for (Part nextPart : graph.get(part.subPart)) {
                basic[nextPart.subPart] += nextPart.weight * part.weight;
                visited[nextPart.subPart]--;
                if (visited[nextPart.subPart] == 0) q.add(new Part(nextPart.subPart, basic[nextPart.subPart]));
            }
        }

        for (int i = 1; i < n; i++) {
            if (graph.get(i).isEmpty()) System.out.println(i + " " + basic[i]);
        }


    }

    private static void init(BufferedReader br) throws IOException {

        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        visited = new int[n + 1];
        graph = new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int part = Integer.parseInt(st.nextToken());
            int subPart = Integer.parseInt(st.nextToken());
            int cnt = Integer.parseInt(st.nextToken());
            visited[subPart] += 1;
            graph.get(part).add(new Part(subPart, cnt));
        }
    }
    static class Part implements Comparable<Part>{
        private final int subPart;
        private final int weight;

        public Part(int subPart, int weight) {
            this.subPart = subPart;
            this.weight = weight;
        }

        @Override
        public int compareTo(Part o) {
            return Integer.compare(this.subPart, o.subPart);
        }
    }
}
