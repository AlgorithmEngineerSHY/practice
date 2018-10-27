class Solution:
    def __init__(self):
        self.board = None

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        return self.is_row_valid() and self.is_col_valid() and self.is_square_valid()

    def is_row_valid(self):
        for i in range(9):
            if not self.is_valid(self.board[i]):
                return False
        return True

    def is_col_valid(self):
        for i in zip(*self.board):
            if not self.is_valid(i):
                return False
        return True

    def is_square_valid(self):
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                nums = [self.board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
                if not self.is_valid(nums):
                    return False
        return True

    def is_valid(self, nums):
        nums = [x for x in nums if x != '.']
        return len(nums) == len(set(nums))

