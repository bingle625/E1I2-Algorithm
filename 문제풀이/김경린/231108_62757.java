import java.util.*;

class Solution {
    public int maxVal = 0;
    public int calc(int[] visited, ArrayList<Integer> nums, ArrayList<String> operator, ArrayList<String> operatorSet) {
        for(int i=0; i<visited.length; i++) {
            int idx = visited[i];
            String op = operatorSet.get(idx);
 
            for(int j=0; j<operator.size(); j++) {
                if (operator.get(j).equals(op)) {
                    int num = 0;
                    if(op.equals("+")) {
                        num = nums.get(j) + nums.get(j+1);
                    } else if(op.equals("-")) {
                        num = nums.get(j) - nums.get(j+1);
                    } else if (op.equals("*")) {
                        num = nums.get(j) * nums.get(j+1);
                    }
                    
                
                    nums.remove(j);
                    nums.remove(j);
                    nums.add(j, num);
                    
                
                    operator.remove(j);
                    j -= 1;
                
                }
            }
            
            
        }
        return Math.abs(nums.get(0));
    }
    public void dfs(int[] visited, ArrayList<Integer> nums,  ArrayList<String> operator, ArrayList<String> operatorSet, int cnt) {
        
        if (cnt == visited.length) {
            maxVal = Math.max(maxVal,calc(visited, (ArrayList<Integer>) nums.clone(), (ArrayList<String>) operator.clone(), operatorSet));
        }
    
        for (int i = 0; i < visited.length; i++) {
            if (visited[i] == 0) {
                visited[i] = cnt;
                dfs(visited, nums, operator, operatorSet, cnt+1);
                visited[i] = 0;
            }
        }
    }
    public long solution(String expression) {
        long answer = 0;
        Queue<String> queue = new LinkedList<>();
        ArrayList<String> operatorSet = new ArrayList<String>();
        ArrayList<String> operator = new ArrayList<String>();
        ArrayList<Integer> nums = new ArrayList<Integer>();
        
        String[] expressionChars = expression.split("");
        ArrayList<String> expressionSplited = new ArrayList<String>();
        
        int lastIdx = 0;
        
        for (int i = 0; i < expressionChars.length; i++) {
            if (expressionChars[i].equals("+") || expressionChars[i].equals("-") || expressionChars[i].equals("*")) {
                
                String[] num = Arrays.copyOfRange(expressionChars, lastIdx, i);
                nums.add(Integer.parseInt(String.join("", num)));
                
                if (!operatorSet.contains(expressionChars)) {
                    operatorSet.add(expressionChars[i]);
                }
                operator.add(expressionChars[i]);
                lastIdx = i+1;
                
            } 
        }
        
        String[] num = Arrays.copyOfRange(expressionChars, lastIdx, expressionChars.length);
        nums.add(Integer.parseInt(String.join("", num)));
        
        // 우선순위
        int[] visited = new int[operatorSet.size()];
        
        dfs(visited, nums, operator, operatorSet, 0);
        return maxVal;
    }
}