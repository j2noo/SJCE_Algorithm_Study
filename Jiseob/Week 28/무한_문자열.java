import java.io.*;

public class 무한_문자열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String t = br.readLine();
        StringBuilder fs = new StringBuilder();
        StringBuilder ft = new StringBuilder();

        int len = s.length() * t.length();

        for (int i = 0; i < len / s.length(); i++) {
            fs.append(s);
        }

        for (int i = 0; i < len / t.length(); i++) {
            ft.append(t);
        }

        if (fs.compareTo(ft) == 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
