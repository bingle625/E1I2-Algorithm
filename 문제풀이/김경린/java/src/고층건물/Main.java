package 고층건물;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int nums = Integer.parseInt(br.readLine());
        int[] buildings = new int[nums];
        float[][] gradients = new float[nums][nums];
        int[] increases = new int[nums];


        String[] input = br.readLine().split(" ");
        for(int i=0; i<nums; i++) {
            buildings[i] = Integer.parseInt(input[i]);
        }

        for(int i=0; i<nums; i++) {
            for(int j=0; j<nums; j++) {
                if(i!=j) {
                    gradients[i][j] = (float)(buildings[i] - buildings[j])/(i-j);
                    gradients[j][i] = gradients[i][j];
                } else {
                    gradients[i][j] = 0;
                    gradients[j][i] = 0;
                }
            }
        }
        int answer = 0;
        for(int i=0; i<nums; i++) {
            Deque<Float> front = new LinkedList<Float>();
            Deque<Float> back = new LinkedList<Float>();
            for(int j=0; j<nums; j++) {
                if(i>j) {
                    if (!front.isEmpty()) {
                        if(front.peekLast() < gradients[i][j]) {
                            front.add(gradients[i][j]);;
                        } else {
                            while(!front.isEmpty() && front.peekLast() >= gradients[i][j]) {
                                front.pollLast();
                            }
                            front.add(gradients[i][j]);
                        }
                    } else {
                        front.add(gradients[i][j]);
                    }
                } else if (i<j) {
                    if (!back.isEmpty()) {
                        if(back.peekLast() < gradients[i][j]) {
                            back.add(gradients[i][j]);;
                        }
                    } else {
                        back.add(gradients[i][j]);
                    }
                }
            }
//            System.out.println( buildings[i] + " 기울기 ->" + Arrays.toString(gradients[i]));
//            Iterator iter = front.iterator();
//            while(iter.hasNext()) {
//                System.out.print(iter.next() + " ");
//            }
//            iter = back.iterator();
//            while(iter.hasNext()) {
//                System.out.print(iter.next() + " ");
//            }
//            System.out.println("\n============================");

            answer = front.size() + back.size() > answer ? front.size() + back.size(): answer;
        }
        System.out.println(answer);
    }
}

// 고층 빌딩 a에서 다른 고층 빌딩이 보여야함. 가장 많은 고층 빌딩이 보이는 빌딩을
// 기울기 4 1 1/3 6/4
// 나를 기준으로 높은 건물은 기울기가 점점 커야 안보임 증가하는 수가 많은 것
// 증가하는수열이 가장 긴 빌ㄷ이

// 백준 1027