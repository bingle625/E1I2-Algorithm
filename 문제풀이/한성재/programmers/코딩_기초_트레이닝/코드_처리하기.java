package programmers.코딩_기초_트레이닝;

public class 코드_처리하기 {
    class Solution {
        public static String solution(String code) {
            StringBuilder result = new StringBuilder();
            int mode = 0;
            for (int i = 0; i < code.length(); i++) {
                char c = code.charAt(i);
                if (mode == 0) {
                    if (c != '1') {
                        if (i % 2 == 0) {
                            result.append(c);
                        }
                    } else {
                        mode = (mode + 1) % 2;

                    }
                } else {
                    if (c != '1') {
                        if (i % 2 != 0) {
                            result.append(c);
                        }
                    } else {
                        mode = (mode + 1) % 2;
                    }
                }
            }
            return result.length() == 0 ? "EMPTY" : result.toString();
        }
    }

    public static void main(String[] args) throws Exception {

        String answer = Solution.solution("abc1abc1abc");
        System.out.println(answer);
    }
}