class Solution:
    def __init__(self):
        self.set_pacific = set()
        self.set_atlantic = set()
        self.mat = None
        self.n_row = None
        self.n_col = None

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        self.mat = matrix
        self.n_row = len(matrix)
        self.n_col = len(matrix[0])

        for row in range(self.n_row):
            self.dfs(row, 0, self.set_pacific)
        for col in range(self.n_col):
            self.dfs(0, col, self.set_pacific)

        for row in range(self.n_row):
            self.dfs(row, self.n_col - 1, self.set_atlantic)
        for col in range(self.n_col):
            self.dfs(self.n_row - 1, col, self.set_atlantic)

        res_set = self.set_atlantic.intersection(self.set_pacific)
        return [[x[0], x[1]] for x in res_set]

    def dfs(self, row, col, set_):

        set_.add((row, col))
        height = self.mat[row][col]
        if row - 1 >= 0 and (row - 1, col) not in set_ and height <= self.mat[row - 1][col]:
            self.dfs(row - 1, col, set_)
        if row + 1 < self.n_row and (row + 1, col) not in set_ and height <= self.mat[row + 1][col]:
            self.dfs(row + 1, col, set_)
        if col - 1 >= 0 and (row, col - 1) not in set_ and height <= self.mat[row][col - 1]:
            self.dfs(row, col - 1, set_)
        if col + 1 < self.n_col and (row, col + 1) not in set_ and height <= self.mat[row][col + 1]:
            self.dfs(row, col + 1, set_)
