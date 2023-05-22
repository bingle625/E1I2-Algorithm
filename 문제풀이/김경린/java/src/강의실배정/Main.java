package 강의실배정;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class ClassTime {
    int start;
    int fin;

    public ClassTime(int start, int fin) {
        this.start = start;
        this.fin = fin;
    }

    public int getStart() {
        return this.start;
    }

}

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int classNum = Integer.parseInt(br.readLine());
        ClassTime[] classes = new ClassTime[classNum];
        for(int i=0;i<classNum;i++) {
            String input = br.readLine();
            String[] time = input.split(" ");
            int start = Integer.parseInt(time[0]);
            int fin = Integer.parseInt(time[1]);
            classes[i] = new ClassTime(start, fin);
        }
        Arrays.sort(classes, (a, b) -> a.start - b.start);
        PriorityQueue<ClassTime> result = new PriorityQueue<>((a,b) -> a.fin - b.fin);

        for(int i=0;i<classNum;i++){
//            System.out.println("순서: "+classes[i].start+classes[i].fin);
            if(!result.isEmpty()){
//                System.out.println("result " + result.peek().start+" "+result.peek().fin);
                ClassTime tmp = result.peek();
                if (tmp.fin <= classes[i].start) {
//                    System.out.println("제일 위에 있는 것"+tmp.start+tmp.fin);
                    result.poll();
                    result.add(new ClassTime(tmp.start, classes[i].fin));
                } else {
                 result.add(new ClassTime(classes[i].start, classes[i].fin));             
                }
            } else {
                  result.add(new ClassTime(classes[i].start, classes[i].fin));
            }
        }
//        System.out.println(result.peek().start+" "+result.peek().fin);
        System.out.println(result.size());

    }
}
