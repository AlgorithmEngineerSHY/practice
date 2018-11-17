class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix)
        len_col = len(matrix[0])

        row = set()
        col = set()

        for i in range(len_row):
            for j in range(len_col):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(len_row):
            for j in range(len_col):
                if i in row or j in col:
                    matrix[i][j] = 0
        