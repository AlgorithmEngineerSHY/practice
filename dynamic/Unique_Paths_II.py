class Solution:
    def __init__(self):
        self.map = None
        self.my_map = None
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        len_row = len(obstacleGrid)
        len_col = len(obstacleGrid[0])
        self.map = obstacleGrid
        self.my_map = [[0] * len_col for i in range(len_row)]
        for i in range(len_col):
            if self.map[0][i] == 0:
                self.my_map[0][i] = 1
            else:
                break
        for i in range(len_row):
            if self.map[i][0] == 0:
                self.my_map[i][0] = 1
            else:
                break
        for i in range(1, len_row):
            for j in range(1, len_col):
                if self.map[i][j] == 1:
                    continue
                else:
                    self.my_map[i][j] += self.my_map[i - 1][j]
                    self.my_map[i][j] += self.my_map[i][j - 1]

        return self.my_map[-1][-1]
obj = Solution()
print(obj.uniquePathsWithObstacles([[0],[0]]))