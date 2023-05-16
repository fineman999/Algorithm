package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BinarySearchTree {
    private static final List<Integer> preOrder = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        setPreOrder(br);

        StringBuilder sb = new StringBuilder();
        getPostOrder(sb, 0, preOrder.size());

        System.out.println(sb);
    }

    private static void getPostOrder(StringBuilder sb, int start, int end) {

        if (start >= end) return;

        int root = preOrder.get(start);
        int right = end;

        for (int i = start + 1; i < end; i++) {
            if (root < preOrder.get(i)) {
                right = i;
                break;
            }
        }
        if (start + 1 < right) getPostOrder(sb, start + 1, right);
        if (right < end) getPostOrder(sb, right, end);

        sb.append(root).append("\n");
    }

    private static void setPreOrder(BufferedReader br) throws IOException {
        String input;
        try {
            while ((input = br.readLine()) != null && !input.isEmpty()) {
                preOrder.add(Integer.parseInt(input));
            }
        } catch (Exception ignored) {
//            throw new RuntimeException(ignored);
        }

        br.close();
    }
}
