package programmers.코딩_기초_트레이닝;

public class flag에_따라_다른_값_반환하기 {
    class Solution {
        public static int solution(int a, int b, boolean flag) {
            return flag ? a + b : a - b;
        }
    }
    public static void main(String[] args) throws Exception {
        int answer = Solution.solution(-4,7,false);

        System.out.println(answer);
    }
}