package 수묶기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int num = Integer.parseInt(input);
        PriorityQueue<Integer> numsUnderZero = new PriorityQueue<>();
        PriorityQueue<Integer> numsOverZero = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i<num;i++) {
            String n = br.readLine();
            Integer intN = Integer.parseInt(n);
            if(intN <= 0) {
                numsUnderZero.add(intN);
            } else {
                numsOverZero.add(intN);
            }
        }
//        nums.stream().sorted();
//        numsReversed.stream().sorted(Comparator.reverseOrder());

//        Iterator iter = nums.iterator();
//        while(iter.hasNext()) {
//            System.out.print(iter.next() + " ");
//       }
        int sum = 0;
        while(numsUnderZero.size() > 1) {
            int n = numsUnderZero.poll();
            int m = numsUnderZero.poll();
            sum += n*m;
        }
        if(numsUnderZero.size() == 1) {
            sum += numsUnderZero.poll();
        }

        while(numsOverZero.size() > 1) {
            int n = numsOverZero.poll();
            int m = numsOverZero.poll();
            if(n*m < n+m) {
                sum += n+m;
            } else {
                sum += n*m;
            }

        }
        if(numsOverZero.size() == 1) {
            sum += numsOverZero.poll();
        }
        System.out.print(sum);

    }
}
