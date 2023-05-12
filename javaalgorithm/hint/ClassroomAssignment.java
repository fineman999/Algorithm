package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class ClassroomAssignment {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] rooms = new int[n][2];
        setRooms(rooms, n, br);

        Arrays.sort(rooms, Comparator.comparing(a -> a[0]));


        PriorityQueue<Integer> q = new PriorityQueue<>();

        for (int[] room : rooms) {
            int start = room[0];
            int end = room[1];
            if(!q.isEmpty() && q.peek() <= start) q.poll();
            q.offer(end);
        }

        System.out.println(q.size());

    }
    private static void setRooms(int[][] rooms, int n, BufferedReader br) throws IOException {
        for (int i = 0; i < n; i++) {
            String[] split = br.readLine().split(" ");
            rooms[i][0] = Integer.parseInt(split[0]);
            rooms[i][1] = Integer.parseInt(split[1]);
        }
    }
}
