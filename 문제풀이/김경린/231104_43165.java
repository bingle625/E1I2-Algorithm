import java.util.Deque;
import java.util.ArrayDeque;

class Calculator {
    int num;
    int depth;
    
    public Calculator(int num, int depth) {
        this.num = num;
        this.depth = depth;
    }
}

class Solution {
    
    public int bfs(int[] numbers, int target) {
        int answer = 0;
        Deque<Calculator> calc = new ArrayDeque<>();
        
        calc.add(new Calculator(numbers[0], 1));
        calc.add(new Calculator(-numbers[0], 1));
        
        while (calc.size() > 0) {
            Calculator numDepth = calc.pop();
            if (numDepth.depth < numbers.length) {
                calc.add(new Calculator(numDepth.num + numbers[numDepth.depth], numDepth.depth+1));
                calc.add(new Calculator(numDepth.num - numbers[numDepth.depth], numDepth.depth+1));
            } else if ((numDepth.depth == numbers.length) && (numDepth.num == target)) {
                answer += 1;           
            }
        }
        
        return answer;
        
    }
    
    public int solution(int[] numbers, int target) {
        int answer = 0;
        // char[] operators = ['+', '-'];
        
        answer = bfs(numbers, target);      
        return answer;
    }
}