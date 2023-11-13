import java.util.*;

class Solution {
    public boolean is_one_difference(String word, String target) {
        int count = 0;
        for(int i=0; i<word.length(); i++) {
            if (!(word.charAt(i) == target.charAt(i))) {
                count += 1;
                if (count > 1) {
                    return false;
                }
            }
        }
        if (count == 1) {
            return true;
        }
        return false;
    }
    
    public int bfs(String begin, String target, String[] words) {
        int[] visited = new int[words.length];
        Deque<Integer> nodes = new ArrayDeque<>();
        
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }
        
        for(int i = 0; i< words.length; i++) {
            if (is_one_difference(begin, words[i])) {
                nodes.add(i);
                visited[i] += 1;
            }
        }
        
        while (nodes.size() > 0) {
            int idx = nodes.poll();
            if (words[idx].equals(target)) {
                return visited[idx];
            }
            for (int i=0; i<words.length; i++) {
                if (visited[i] == 0 && is_one_difference(words[idx], words[i])) {
                    nodes.add(i);
                    visited[i] = visited[idx] + 1;
                }
            }
        }
        return 0;
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        answer =  bfs(begin, target, words);
        
        return answer;
    }
}