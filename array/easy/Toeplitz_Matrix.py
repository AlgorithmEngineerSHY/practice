class Solution:
    def __init__(self):
        self.n_row = None
        self.n_col = None
        self.mat = None
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        self.mat = matrix
        self.n_row = len(matrix)
        self.n_col = len(matrix[0])
        for i in range(self.n_col):
            if not self.helper(0, i):
                return False
        for i in range(1, self.n_row):
            if not self.helper(i, 0):
                return False
        return True

    def helper(self, row, col):
        num = self.mat[row][col]
        while row < self.n_row - 1 and col < self.n_col - 1:
            row += 1
            col += 1
            if self.mat[row][col] == num:
                continue
            else:
                return False
        return True