class Solution:
    def __init__(self):
        self.res = 1
        self.grid = None
        self.n_row = None
        self.n_col = None
        self.mark = True
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        n_row = len(grid)
        n_col = len(grid[0])
        self.n_row = n_row
        self.n_col = n_col

        for row in range(n_row):

            for col in range(n_col):
                self.mark = True
                self.helper(row, col)
        return self.res - 1

    def helper(self, row, col):
        if self.grid[row][col] == '1':
            if self.mark:
                self.res += 1
                self.mark = False
            self.grid[row][col] = str(self.res)
            if row - 1 >= 0:
                self.helper(row - 1, col)
            if row + 1 < self.n_row:
                self.helper(row + 1, col)
            if col - 1 >= 0:
                self.helper(row, col - 1)
            if col + 1 < self.n_col:
                self.helper(row, col + 1)

obj = Solution()
print(obj.numIslands([['1', '0'],
                      ['0', '1']]))