package hint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PhoneList {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        start(br);

    }

    private static void start(BufferedReader br) throws IOException {
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            String[] phones = new String[n];
            for (int j = 0; j < n; j++) {
                phones[j] = br.readLine();
            }
            String answer = solution(phones);

            System.out.println(answer);
        }
    }

    private static String solution(String[] phones) {
        Arrays.sort(phones);
        Map<String, Integer> phoneMaps = new HashMap<>();

        for (String phone : phones) {
            for (int i = 0; i < phone.length(); i++) {
                if(phoneMaps.containsKey(phone.substring(0,i))) return "NO";
            }
            phoneMaps.put(phone, 1);

        }
        return "YES";
    }
}
