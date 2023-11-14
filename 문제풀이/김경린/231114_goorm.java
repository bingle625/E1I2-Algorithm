
import java.io.*;
import java.util.*;

class Car {
	int idx=0; // 자동차 번호
	int w=0; // 내구도
	
	public Car(int idx, int w) {
		this.idx = idx;
		this.w = w;
	}
}
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num  = Integer.parseInt(br.readLine());
		Car[] vs = new Car[1001];
		for (int i=0; i<1001; i++) {
			vs[i] = new Car(0, 0);
		}
		for (int i=0 ; i< num; i++) {
			String[] info = br.readLine().split(" ");
			int v = Integer.parseInt(info[0]);
			int w = Integer.parseInt(info[1]);
			if (vs[v].w <= w) {
				vs[v].idx = i+1;
				vs[v].w = w;
			}
		}
		int answer = 0;
		for (int i=1; i<1001; i++) {
			answer += vs[i].idx;
		}
		System.out.println(answer);
	}
}