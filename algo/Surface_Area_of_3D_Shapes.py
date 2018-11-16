class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_len = len(grid)
        area = 0
        for row in range(n_len):
            for col in range(n_len):
                if grid[row][col] > 0:
                    area += 2
                else:
                    continue
                # up
                if row - 1 < 0:
                    area += grid[row][col]
                else:
                    area += max(0, grid[row][col] - grid[row - 1][col])
                # down
                if row + 1 == n_len:
                    area += grid[row][col]
                else:
                    area += max(0, grid[row][col] - grid[row + 1][col])

                # left
                if col - 1 < 0:
                    area += grid[row][col]
                else:
                    area += max(0, grid[row][col] - grid[row][col - 1])

                # right
                if col + 1 == n_len:
                    area += grid[row][col]
                else:
                    area += max(0, grid[row][col] - grid[row][col + 1])
        return area