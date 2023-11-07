import java.util.*;

class Solution {
    
    public boolean isSame(int[][] arr, int arrSize) {
        int val = arr[0][0];
       if (arrSize == 1) {
           return true;
       }
        for(int i=0; i<arrSize; i++) {
            for (int j = 0; j<arrSize; j++) {
                if(arr[i][j] != val) {
                    return false;
                }   
            }
        } 
        return true;
    }
    
    public int[][] divideList(int[][] arr, int idx, int arrSize) {
        int[][] newArr = new int[arrSize][arrSize];
        int startX = 0;
        int startY = 0;
        
        if (idx == 1) {
            startX = 0;
            startY = 0;
        } else if (idx == 2) {
            startX = arrSize;
            startY = 0;
        } else if (idx == 3) {
            startX = 0;
            startY = arrSize;
        } else if (idx == 4) {
            startX = arrSize;
            startY = arrSize;
        }
        
        for (int i = startY; i < startY+arrSize; i++) {
            newArr[i-startY] = Arrays.copyOfRange(arr[i], startX, startX+arrSize);
        }
        
        return newArr;
    }
    
    public int[] calc(int[][] arr) {
        int[] cnt = {0, 0};
        if (arr[0][0] == 0) {
            cnt[0] = 1;
        } else {
            cnt[1] = 1;
        }
        
        return cnt;
    }
    
    public int[] dfs(int[][] arr, int arrSize) {
        if (isSame(arr, arrSize)) {
            // answer 계산
            return calc(arr);
            
        }
        arrSize = arrSize / 2;
        int[][] arr1 = divideList(arr, 1, arrSize);
        int[] cnt1 = dfs(arr1, arrSize);
        
        int[][] arr2 = divideList(arr, 2, arrSize);
        int[] cnt2 = dfs(arr2, arrSize);
        
        int[][] arr3 = divideList(arr, 3, arrSize);
        int[] cnt3 = dfs(arr3, arrSize);
        
        int[][] arr4 = divideList(arr, 4, arrSize);
        int[] cnt4 = dfs(arr4, arrSize);
        
        int[] cntSum = {0, 0};
        
        cntSum[0] = cnt1[0] + cnt2[0] + cnt3[0] + cnt4[0];
        cntSum[1] = cnt1[1] + cnt2[1] + cnt3[1] + cnt4[1];
        
        return cntSum;
    }
    public int[] solution(int[][] arr) {
        int[] answer = {};
        int arrSize = arr.length;
        
        answer = dfs(arr, arrSize);
        
        return answer;
    }
}