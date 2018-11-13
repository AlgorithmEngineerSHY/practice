class Solution:
    def __init__(self):
        self.one_loc_set = None
        self.res = 0
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        one_loc_set = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    one_loc_set.add((row, col))
        self.one_loc_set = one_loc_set
        if self.one_loc_set:
            self.res = 1
        self.helper()
        return self.res ** 2


    def helper(self):
        tmp_one_loc_set = set()
        for one_loc in self.one_loc_set:
            row = one_loc[0]
            col = one_loc[1]
            if (row + 1, col) in self.one_loc_set and \
                    (row + 1, col + 1) in self.one_loc_set and \
                    (row, col + 1) in self.one_loc_set:
                tmp_one_loc_set.add((row, col))
        if tmp_one_loc_set:
            self.one_loc_set = tmp_one_loc_set
            self.res += 1
            self.helper()

obj = Solution()
print(obj.maximalSquare([['1',0,'1',0,0],
                         ['1',0,'1','1','1'],
                         ['1','1','1','1','1'],
                         ['1',0,0,'1',0]]))