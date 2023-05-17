// import java.io.*;
// import java.util.*;

// class Pos {
// 	int x;
// 	int y;
// 	int f;
// 	public Pos(int x, int y, int f) {
// 		this.x = x;
// 		this.y = y;
// 		this.f = f;
// 	}
// }
// class Main {
// 	public static void main(String[] args) throws Exception {
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		StringTokenizer st = new StringTokenizer(br.readLine());
		
// 		String[] size = br.readLine().split(" ");

// 		int sizeX = Integer.parseInt(size[0]);
// 		int sizeY = Integer.parseInt(size[1]);
// 		int defaultForce = Integer.parseInt(size[2]);
		
// 		String[][] arr = new String[sizeY][sizeX];
// 		int[][] visited = new int[sizeY][sizeX];
		
// 		for(int i=0; i< sizeY;i++) {
// 			arr[i] = br.readLine().split("");
// 		}
// 		// System.out.println(Arrays.deepToString(visited)); 2차원 배열 출력
		
// 		int[] dx = {1, 0, -1, 0};
// 		int[] dy = {0, 1, 0, -1};
// 		int curX = 0;
// 		int curY = 0;
// 		visited[curY][curX] = 1;
// 		Queue<Pos> queue = new LinkedList<Pos>();
// 		queue.add(new Pos(curX, curY, defaultForce));
// 		while(!queue.isEmpty()){
// 		// 	Iterator iter = queue.iterator();
		
// 		// 	while(iter.hasNext()){
// 		// 		System.out.print(iter.next() + " ");
// 		// 	}
// 			Pos curPos = queue.poll();
			
// 			if (curPos.x == sizeX-1 && curPos.y == sizeY-1){
// 				System.out.println(visited[curPos.y][curPos.x]);
// 				break;
// 			}
// 			for(int i=0; i<4; i++) {
// 				int nextX = curPos.x + dx[i];
// 				int nextY = curPos.y + dy[i];
			
// 				if (nextX >= 0 && nextX < sizeX && nextY >= 0 && nextY < sizeY && visited[nextY][nextX] == 0) {
// 					if (arr[nextY][nextX].equals("1") && curPos.f >= 10){
// 						queue.add(new Pos(nextX, nextY, curPos.f - 10));
// 					} else {
// 						queue.add(new Pos(nextX, nextY, curPos.f));
// 					}
// 					visited[nextY][nextX] = visited[curPos.y][curPos.x] + 1;
// 				}
// 			}
// 		}
// 		System.out.println("-1");
// 	}
// }

// // 구름 마법사의-시험 
// // 연속된 나무 조건 안지킴


import java.io.*;
import java.util.*;

class Pos {
	int x;
	int y;
	int f;
	public Pos(int x, int y, int f) {
		this.x = x;
		this.y = y;
		this.f = f;
	}
}
class Status {
	int dist;
	int power;
	public Status(int dist, int power) {
		this.dist = dist;
		this.power = power;
	}
}
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// StringTokenizer st = new StringTokenizer(br.readLine());
		String line = br.readLine();
		
		String[] size = line.split(" ");

		int sizeX = Integer.parseInt(size[0]);
		int sizeY = Integer.parseInt(size[1]);
		int defaultForce = Integer.parseInt(size[2]);
		
		String[][] arr = new String[sizeY][sizeX];
		Status[][] visited = new Status[sizeY][sizeX];
		for(int i=0;i<sizeY;i++){
			for(int j=0;j<sizeX;j++){
				visited[i][j] = new Status(0,0); // 객체 배열은 무조건 초기화,,
			}
		}
		
		for(int i=0; i< sizeY;i++) {
			arr[i] = br.readLine().split("");
		}
		// System.out.println(Arrays.deepToString(visited)); 2차원 배열 출력
		
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, 1, 0, -1};
		int curX = 0;
		int curY = 0;
		boolean escape = false;
		visited[curY][curX].dist = 1;
		visited[curY][curX].power = defaultForce;
		
		Queue<Pos> queue = new LinkedList<Pos>();
		queue.add(new Pos(curX, curY, defaultForce));
		while(!queue.isEmpty()){
		// 	Iterator iter = queue.iterator();
		
		// 	while(iter.hasNext()){
		// 		System.out.print(iter.next() + " ");
		// 	}
			Pos curPos = queue.poll();
			
			// System.out.printf("\n %d %d %d dist:%d", curPos.x, curPos.y, curPos.f, visited[curPos.y][curPos.x].dist);
			
			if (curPos.x == sizeX-1 && curPos.y == sizeY-1){
				System.out.println(visited[curPos.y][curPos.x].dist-1);
				escape = true;
				break;
			}
			for(int i=0; i<4; i++) {
				int nextX = curPos.x + dx[i];
				int nextY = curPos.y + dy[i];
				if (nextX >= 0 && nextX < sizeX && nextY >= 0 && nextY < sizeY && ((visited[nextY][nextX].dist == 0) || (visited[nextY][nextX].power < visited[curPos.y][curPos.x].power))) {
					if (arr[curPos.y][curPos.x].equals("1")) {
						if (!arr[nextY][nextX].equals("1") && curPos.f >= 0){
							queue.add(new Pos(nextX, nextY, curPos.f ));
							visited[nextY][nextX].dist = visited[curPos.y][curPos.x].dist;
							visited[nextY][nextX].power = curPos.f;
						} 
					} else {
						if (arr[nextY][nextX].equals("1")){
							if (curPos.f >= 10) {
								queue.add(new Pos(nextX, nextY, curPos.f - 10));
								visited[nextY][nextX].power = curPos.f - 10;
								visited[nextY][nextX].dist = visited[curPos.y][curPos.x].dist + 1;
							}
						} else {
							queue.add(new Pos(nextX, nextY, curPos.f));
							visited[nextY][nextX].power = curPos.f;
							visited[nextY][nextX].dist = visited[curPos.y][curPos.x].dist + 1;
						}
					}
					
					// System.out.printf("%d %d %d    ",visited[nextY][nextX].dist, visited[nextY][nextX].power, i);
				}
			}
		}
		if (!escape){
			System.out.println("-1");
		}
	}
}
// 시간 초과, 파이썬으로 풀고 자바로 변환해보기