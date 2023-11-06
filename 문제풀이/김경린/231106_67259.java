// class Solution {
//     public void dfs(int x, int y, int[][] board, int boardSize, int beforeDir) {
//         int[] dx = {1, 0, -1, 0};
//         int[] dy = {0, 1, 0, -1};
        
        
//         for(int i = 0; i < 4; i++) {
//             int nextX = x + dx[i];
//             int nextY = y + dy[i];
            
//             if ((nextX == boardSize -1) && (nextY == boardSize-1)) {
//                 int finalValue =  board[y][x] + ((beforeDir % 2 == i % 2) ? 100 : 600);
//                 if (board[nextY][nextX] == 0) {
//                     // 처음 방문
//                     board[nextY][nextX] = finalValue;
//                 } else {
//                     if(finalValue < board[nextY][nextX]) {
//                         board[nextY][nextX] = finalValue;
//                     }
//                 }
//             } else if (0<= nextX && nextX<boardSize && 0<=nextY && nextY<boardSize && board[nextY][nextX] == 0) {
                
//                 board[nextY][nextX] = board[y][x] + ((beforeDir % 2 == i % 2) ? 100 : 600);
//                 dfs(nextX, nextY, board, boardSize, i);
//                 board[nextY][nextX] = 0;
//             }
//         }
        
//     }
    
//     public int solution(int[][] board) {
//         int[] dx = {1, 0, -1, 0};
//         int[] dy = {0, 1, 0, -1};
//         int answer = 0;
//         board[0][0] = 1;
//         int boardSize = board.length;
        
//         for(int i = 0; i<4; i++) {
//             int nextX = 0 + dx[i];
//             int nextY = 0 + dy[i];
            
//             if ((0<= nextX && nextX < boardSize) && (0<=nextY && nextY < boardSize) && (board[nextY][nextX] == 0)) {
//                 board[nextY][nextX] = 100;
//                 dfs(nextX, nextY, board, boardSize, i);
//                 board[nextY][nextX] = 0;
//             }
//         }
//         answer = board[boardSize-1][boardSize-1];
//         return answer;
//     }
// }


import java.util.*;

class Dir {
    int x;
    int y;
    int dir;
    
    public Dir(int x, int y, int dir) {
        this.x = x;
        this.y = y;
        this.dir = dir;
    }
}
class Solution {
    
    public int solution(int[][] board) {
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        int answer = Integer.MAX_VALUE;
        board[0][0] = 1;
        int boardSize = board.length;
        
        Queue<Dir> visited = new LinkedList<>();
        int[][][] point = new int[boardSize][boardSize][4];
        
        for(int i = 0; i<4; i++) {
                int nextX = 0 + dx[i];
                int nextY = 0 + dy[i];

                if (0<= nextX && nextX < boardSize && 0<=nextY && nextY < boardSize && board[nextY][nextX] != 1) {
                    point[nextY][nextX][i] = 100;
                    visited.add(new Dir(nextX, nextY, i));
                }
        }
        
        while (visited.size() > 0) {
            Dir current = visited.poll();
            for(int i = 0; i<4; i++) {
                
                int nextX = current.x + dx[i];
                int nextY = current.y + dy[i];
                
                // 이미 지나쳐서 온 길
                if (Math.abs(current.dir - i) == 2) {
                    continue;
                }
                

                if (0<= nextX && nextX < boardSize && 0<=nextY && nextY < boardSize && board[nextY][nextX] != 1) {
                    int nextValue =  point[current.y][current.x][current.dir] + (( current.dir % 2 == i % 2) ? 100 : 600);
                    // 해당 방향으로 처음 온 길 or 기존 방법보다 더 빠른 경로인 경우
                    if (point[nextY][nextX][i] == 0 || point[nextY][nextX][i] > nextValue) {
                        point[nextY][nextX][i] = nextValue;
                        if (!(nextY == boardSize-1 && nextX == boardSize-1)){
                            visited.add(new Dir(nextX, nextY, i));
                        }
                    }
                    
                }
            }
        }
        
        for (int i = 0; i<4; i++) {
            if (point[boardSize-1][boardSize-1][i] != 0 && point[boardSize-1][boardSize-1][i] < answer) {
                answer = point[boardSize-1][boardSize-1][i];
            }
        }
        return answer;
    }
}