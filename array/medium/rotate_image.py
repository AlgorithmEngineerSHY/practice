'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
'''


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])