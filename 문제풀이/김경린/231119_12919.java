//import java.io.*;
//import java.util.*;
////import java.util.stream.Stream;
//
//class Node {
//    public int Adiff = 0;
//    public int Bdiff = 0;
//    public String current = "";
//
//    public Node(int Adiff, int Bdiff, String current) {
//        this.Adiff = Adiff;
//        this.Bdiff = Bdiff;
//        this.current = current;
//    }
//}
//public class Main {
//    public static int bfs(String start, String finish, int Adiff, int Bdiff) {
//        Queue<Node> visited = new LinkedList<Node>();
//
//        if (Adiff > 0) {
//            visited.add(new Node(Adiff-1, Bdiff, start.concat("A")));
//        }
//        if (Bdiff > 0) {
//            String newStr = start.concat("B");
//            StringBuffer sb = new StringBuffer(newStr);
//            visited.add(new Node(Adiff, Bdiff-1, sb.reverse().toString()));
//        }
//
//        while (visited.size() > 0) {
//            Node node = visited.poll();
//            String cur = node.current;
//            if (node.Adiff == 0 && node.Bdiff == 0) {
//                if(cur.equals(finish)) {
//                    return 1;
//                }
//            }
//            if (node.Adiff > 0) {
//                visited.add(new Node(node.Adiff-1, node.Bdiff, cur.concat("A")));
//
//            }
//            if (node.Bdiff > 0) {
//                String newStr = cur.concat("B");
//                StringBuffer sb = new StringBuffer(newStr);
//                visited.add(new Node(node.Adiff, node.Bdiff-1, sb.reverse().toString()));
//            }
//        }
//        return 0;
//    }
//
//    public static void main(String[] args) throws IOException {
//        // TODO Auto-generated method stub
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        String start = br.readLine();
//        String finish = br.readLine();
//
//        int Acnt = 0;
//        int Bcnt = 0;
//
//        int AcntAnswer = 0;
//        int BcntAnswer = 0;
//
//        for(int i=0; i<start.length(); i++) {
//            if (start.charAt(i) == 'A') {
//                Acnt += 1;
//            }
//            else if (start.charAt(i) == 'B') {
//                Bcnt += 1;
//            }
//        }
//
//        for(int i=0; i<finish.length(); i++) {
//            if(finish.charAt(i) == 'A') {
//                AcntAnswer += 1;
//            }
//            else if (finish.charAt(i) == 'B') {
//                BcntAnswer += 1;
//            }
//        }
//
//        int Adiff = AcntAnswer - Acnt;
//        int Bdiff = BcntAnswer - Bcnt;
//
//        int answer = bfs(start, finish, Adiff, Bdiff);
//
//        System.out.println(answer);
//
//
//    }
//}


import java.io.*;
import java.util.*;
//import java.util.stream.Stream;

public class Main {
    public static int bfs(String start, String finish) {
        Queue<String> visited = new LinkedList<String>();

        visited.add(finish);

        while (visited.size() > 0) {
            String current = visited.poll();
            if (current.length() == start.length()) {
                if (current.equals(start)) {
                    return 1;
                }
            }
            if (current.length() > 1) {
                if (current.charAt(current.length() - 1) == 'A') {
                    visited.add(current.substring(0, current.length() - 1));
                }
                if (current.charAt(0) == 'B') {
                    StringBuffer sb = new StringBuffer(current);
                    String reversed = sb.reverse().toString();
                    visited.add(reversed.substring(0, reversed.length() - 1));
                }
            }

        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String start = br.readLine();
        String finish = br.readLine();

        int Acnt = 0;
        int Bcnt = 0;

        int AcntAnswer = 0;
        int BcntAnswer = 0;

        for(int i=0; i<start.length(); i++) {
            if (start.charAt(i) == 'A') {
                Acnt += 1;
            }
            else if (start.charAt(i) == 'B') {
                Bcnt += 1;
            }
        }

        for(int i=0; i<finish.length(); i++) {
            if(finish.charAt(i) == 'A') {
                AcntAnswer += 1;
            }
            else if (finish.charAt(i) == 'B') {
                BcntAnswer += 1;
            }
        }

        int Adiff = AcntAnswer - Acnt;
        int Bdiff = BcntAnswer - Bcnt;

        int answer = bfs(start, finish);

        System.out.println(answer);


    }
}