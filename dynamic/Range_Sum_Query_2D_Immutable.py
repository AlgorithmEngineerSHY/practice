class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return None
        self.mat = []
        n_row = len(matrix)
        n_col = len(matrix[0])
        for row in range(n_row + 1):
            self.mat.append([0] * (n_col + 1))
        for row in range(1, n_row + 1):
            for col in range(1, n_col + 1):
                self.mat[row][col] = matrix[row - 1][col - 1] - self.mat[row - 1][col - 1] + \
                    self.mat[row - 1][col] + self.mat[row][col - 1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.mat[row2 + 1][col2 + 1] + self.mat[row1][col1] - self.mat[row1][col2 + 1] - self.mat[row2 + 1][col1]



# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
param_1 = obj.sumRegion(2,1,4,3)
print(param_1)