class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_row = len(grid)
        len_col = len(grid[0])

        if len_row == 1 and len_col == 1:
            return grid[0][0]

        my_map = [[0] * len_col for i in range(len_row)]
        my_map[0][0] = grid[0][0]

        for i in range(1, len_col):
            my_map[0][i] = my_map[0][i - 1] + grid[0][i]
        for i in range(1, len_row):
            my_map[i][0] = my_map[i - 1][0] + grid[i][0]

        for i in range(1, len_row):
            for j in range(1, len_col):
                my_map[i][j] = min(my_map[i - 1][j], my_map[i][j - 1]) + grid[i][j]
        return my_map[-1][-1]
obj = Solution()
print(obj.minPathSum([[1,2],[5,6],[1,1]]))