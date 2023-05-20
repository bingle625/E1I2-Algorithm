import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static public void bfs(int[][] graph, int start, int num) {
        Queue<Integer> queue = new LinkedList<Integer>();
        boolean[] visited = new boolean[num+1];
        queue.add(start);
        visited[start] = true;
        while(!queue.isEmpty()) {
            int node = queue.poll();
            System.out.printf("%d ", node);
            for(int i = 1; i < num+1; i++) {
                if (graph[node][i]==1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }

    }

    static public void dfs(int[][] graph, int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node+" ");

        for(int i = 1; i< visited.length; i++) {
            if (graph[node][i]==1 && !visited[i]) {
                dfs(graph, i, visited);
//                visited[i] = false;
            }
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] inputs = line.split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        int v = Integer.parseInt(inputs[2]);

//        HashMap<Integer, Integer[]> graph = new HashMap<Integer, Integer[]>();
        int[][] graph = new int[n+1][n+1];

        for (int i=0; i<m; i++){
            String input = br.readLine();
            String[] nodes = input.split(" ");
            graph[Integer.parseInt(nodes[0])][Integer.parseInt(nodes[1])] = 1;
            graph[Integer.parseInt(nodes[1])][Integer.parseInt(nodes[0])] = 1;
        }

        dfs(graph, v, new boolean[n+1]);
        System.out.println("");
        bfs(graph, v, n);

    }
}