import java.util.*;
// import java.util.Queue;
// import java.util.LinkedList;


class Solution {
    public int bfs(HashMap<Integer, List<Integer>> distances, int n) {
        int maxVal = 0;
        int cnt = 0;
        List<Integer> neighbor = distances.get(1);
        Queue<Integer> queue = new LinkedList<>();
        int[] visited = new int[n+1];
        visited[1] = -1;
        for(int next: neighbor) {
            queue.add(next);
            visited[next] = 1;
        }
        
        while (queue.size() > 0) {
            int cur = queue.poll();
            // System.out.println(cur+ "  "+ distances.get(cur));
            // System.out.println(Arrays.toString(visited));
            for(int next: distances.get(cur)){
                if (visited[next] == 0) {
                    visited[next] = visited[cur] + 1;
                    queue.add(next);
                    if (visited[next] > maxVal) {
                        maxVal = visited[next];
                        cnt = 1;
                    } else if (visited[next] == maxVal) {
                        cnt += 1;
                    }
                }
            }
        }
        
        return cnt;
        
    }
    public int solution(int n, int[][] edge) {
        int answer = 0;
        HashMap<Integer, List<Integer>> distances = new HashMap();
        int[] visited = new int[n+1];
        
        for(int i=0; i < edge.length; i++) {
            int node1 = edge[i][0];
            int node2 = edge[i][1];
            
            if (distances.get(node1) == null) {
                distances.put(node1, new ArrayList<>());
            } 
            if (distances.get(node2) == null) {
                distances.put(node2, new ArrayList<>());
            }
            
            distances.get(node1).add(node2);
            distances.get(node2).add(node1);
        }
        // System.out.println(distances.get(1));
        answer = bfs(distances, n);
        
        
        return answer;
    }
}