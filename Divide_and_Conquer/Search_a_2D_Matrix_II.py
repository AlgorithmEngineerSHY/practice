class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:
            return False
        n_row = len(matrix)
        n_col = len(matrix[0])
        min_num = matrix[0][0]
        max_num = matrix[n_row - 1][n_col - 1]

        if target < min_num or target > max_num:
            return False

        row = n_row - 1
        col = 0
        while row >= 0 and col < n_col:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1
        return False