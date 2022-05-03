class Solution(object):
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)