class Solution(object):
    def searchMatrix(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False
        
        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            a = matrix[row][col]
            if target == a:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < a:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > a:
                row += 1
        return False

s = Solution()
s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
