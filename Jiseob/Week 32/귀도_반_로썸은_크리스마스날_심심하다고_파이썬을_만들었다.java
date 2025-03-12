import java.io.*;

public class 귀도_반_로썸은_크리스마스날_심심하다고_파이썬을_만들었다 {

    static int PC = 0, ACC = 0;
    static int[] Memory = new int[32];
    static final int STA = 0, LDA = 1, BEQ = 2, NOP = 3, DEC = 4, INC = 5, JMP = 6, HLT = 7;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = "";

        while (true) {
            PC = 0;
            ACC = 0;
            for (int i = 0; i < 32; i++) {
                // if ((input = br.readLine()).length() < 2) {
                if ((input = br.readLine()) == null) {
                    System.out.print(sb.toString());
                    return;
                }
                Memory[i] = Integer.parseInt(input, 2);
            }

            boolean run = true;
            while (run) {
                int type = type(Memory[PC]);
                int target = target(Memory[PC]);

                PC = (PC + 1) % 32;

                switch (type) {
                    case STA:
                        Memory[target] = ACC;
                        break;
                    case LDA:
                        ACC = Memory[target];
                        break;
                    case BEQ:
                        if (ACC == 0) PC = target;
                        break;
                    case NOP:
                        break;
                    case DEC:
                        ACC = (ACC + 255) % 256;
                        break;
                    case INC:
                        ACC = (ACC + 1) % 256;
                        break;
                    case JMP:
                        PC = target;
                        break;
                    case HLT:
                        for (int i = 7; i >= 0; i--) {
                            sb.append((ACC >> i) & 1);
                        }
                        sb.append("\n");
                        run = false;
                        break;
                }
            }
        }
    }

    private static int target(int input) {
        return input % 32;
    }

    private static int type(int input) {
        return input / 32;
    }
}