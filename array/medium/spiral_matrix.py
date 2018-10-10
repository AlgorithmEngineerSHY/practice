'''
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.
'''


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        re = []
        i, j, di, dj = 0, 0, 0, 1
        m = len(matrix)
        n = len(matrix[0])
        for k in range(m * n):
            re.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i+di)%m][(j+dj)%n] == None:
                di, dj = dj, -di
            i += di
            j += dj
        return re
