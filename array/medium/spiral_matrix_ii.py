'''
Given a positive integer n, 
generate a square matrix filled with elements from 1 to n2 in spiral order.
'''


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0]*n for i in range(n)]
        i, j, di, dj, = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A




