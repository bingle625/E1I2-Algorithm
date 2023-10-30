package programmers.코딩_기초_트레이닝;

import java.util.Objects;

public class 조건문자열 {
        public static int solution(String ineq, String eq, int n, int m) {
            if (n == m && eq.equals("=")) {
                return 1;
            }
            if (ineq.equals(">") && (n > m) || ineq.equals("<") && (n < m)) {
                return 1;
            }

            return 0;
        }
    public static void main(String[] args) throws Exception {
        int answer = solution(">","!",41,78);

        System.out.println(answer);
    }
}