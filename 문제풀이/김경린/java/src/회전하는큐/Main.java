package 회전하는큐;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int size = Integer.parseInt(input[0]);
        int outNum = Integer.parseInt(input[1]);
        input = br.readLine().split(" ");
        int[] targets = new int[outNum];
        Deque<Integer> arr = new LinkedList<Integer>();

        for(int i = 0; i<outNum; i++) {
            targets[i] = Integer.parseInt(input[i]);
        }

        for(int i=0; i< size; i++) {
            arr.add(i+1);
        }

        HashMap<Integer, Integer> idxDict = new HashMap<Integer, Integer>();
        for(int i=0; i < outNum; i++) {
            idxDict.put(targets[i], targets[i]-1);
        }

        int cnt = 0;
        for(int i=0; i < outNum; i++) {
            int idx = idxDict.get(targets[i]);
            int move = 0;
            Iterator iter = arr.iterator();
            if (idx <= size/2) {
                while(arr.peekFirst() != targets[i]) {
                    int tmp = arr.pollFirst();
                    arr.addLast(tmp);
                    move += 1;
                }
                arr.poll();
                if (i != outNum-1) {
                    for (int j = i + 1; j < outNum; j++) {
                        idxDict.put(targets[j], (idxDict.get(targets[j]) - (move) + size) % size - 1);
                    }
                }
                size -= 1;
            } else {
                while(arr.peekLast() != targets[i]) {
                    int tmp = arr.pollLast();
                    arr.addFirst(tmp);
                    move += 1;
                }
                arr.pollLast();
                move += 1;
                if (i != outNum-1) {
                    for (int j = i + 1; j < outNum; j++) {
                        idxDict.put(targets[j], (idxDict.get(targets[j]) + move) % size - 1);
                    }
                }
                size -= 1;
            }
            iter = arr.iterator();
//            System.out.print("move!!"+move+" ");
//            while(iter.hasNext()) {
//                System.out.print(iter.next() + " ");
//            }
//            System.out.println("dict"+idxDict.entrySet());
            cnt += move;
        }
        System.out.println(cnt);

    }
}

// 1 2 3 4 5 6 7 8 9 10
// 2: 1, 9: 8, 4: 5
// 백준 1021