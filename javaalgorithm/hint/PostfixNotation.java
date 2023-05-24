package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class PostfixNotation {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] lines = br.readLine().toCharArray();
        String answer = "";
        Stack<Character> stack = new Stack<>();

        for (char line : lines) {
            if (Character.isLetter(line)) {
                answer += line;
            } else {
                if (line == '(') {
                    stack.add(line);
                } else if (line == ')') {
                    while (!stack.isEmpty()) {
                        Character pop = stack.pop();
                        if (pop == '(') {
                            break;
                        }
                        answer += pop;
                    }
                } else if (line == '*' || line == '/') {
                    while (!stack.isEmpty() && (stack.peek() == '*' || stack.peek() == '/')) {
                        answer += stack.pop();
                    }
                    stack.add(line);
                } else {
                    while (!stack.isEmpty() && stack.peek() != '(') {
                        answer += stack.pop();
                    }
                    stack.add(line);
                }
            }
        }
        while (!stack.isEmpty()) {
            answer += stack.pop();
        }

        System.out.println(answer);

    }

}
