'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1
        while high >= low:
            mid = (high + low) // 2
            num = matrix[mid//col][mid%col]
            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return False