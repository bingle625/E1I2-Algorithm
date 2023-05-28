package 램프;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] rc = br.readLine().split(" ");
        int n = Integer.parseInt(rc[0]);
        int m = Integer.parseInt(rc[1]);
        String[] table = new String[n];
        Map<String, Integer> row = new HashMap<String, Integer>();
        for(int i=0; i<n; i++) {
            table[i] = br.readLine();
            if(row.containsKey(table[i])) {
                row.put(table[i], row.get(table[i])+1);
            } else{
                row.put(table[i], 1);
            }
        }
        List<String> keys = new ArrayList<>(row.keySet());
        Collections.sort(keys, (a,b) -> (row.get(b) - row.get(a)));
        int change = Integer.parseInt(br.readLine());
        boolean isAnswer = false;
        for(String key: keys) {
            long zeroNum = key.chars().filter(k -> k == '0').count();
            if(zeroNum <= change && change%2 == zeroNum%2) {
                System.out.println(row.get(key));
                isAnswer = true;
                break;
            };
        }
        if(!isAnswer) {
            System.out.println(0);
        }

    }
}
// 백준 1034 

