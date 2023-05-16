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
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String[] size = br.readLine().split(" ");

		int sizeX = Integer.parseInt(size[0]);
		int sizeY = Integer.parseInt(size[1]);
		int defaultForce = Integer.parseInt(size[2]);
		
		String[][] arr = new String[sizeY][sizeX];
		int[][] visited = new int[sizeY][sizeX];
		
		for(int i=0; i< sizeY;i++) {
			arr[i] = br.readLine().split("");
		}
		// System.out.println(Arrays.deepToString(visited)); 2차원 배열 출력
		
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, 1, 0, -1};
		int curX = 0;
		int curY = 0;
		visited[curY][curX] = 1;
		Queue<Pos> queue = new LinkedList<Pos>();
		queue.add(new Pos(curX, curY, defaultForce));
		while(!queue.isEmpty()){
		// 	Iterator iter = queue.iterator();
		
		// 	while(iter.hasNext()){
		// 		System.out.print(iter.next() + " ");
		// 	}
			Pos curPos = queue.poll();
			
			if (curPos.x == sizeX-1 && curPos.y == sizeY-1){
				System.out.println(visited[curPos.y][curPos.x]);
				break;
			}
			for(int i=0; i<4; i++) {
				int nextX = curPos.x + dx[i];
				int nextY = curPos.y + dy[i];
			
				if (nextX >= 0 && nextX < sizeX && nextY >= 0 && nextY < sizeY && visited[nextY][nextX] == 0) {
					if (arr[nextY][nextX].equals("1") && curPos.f >= 10){
						queue.add(new Pos(nextX, nextY, curPos.f - 10));
					} else {
						queue.add(new Pos(nextX, nextY, curPos.f));
					}
					visited[nextY][nextX] = visited[curPos.y][curPos.x] + 1;
				}
			}
		}
		System.out.println("-1");
	}
}

// 구름 마법사의-시험 
// 연속된 나무 조건 안지킴