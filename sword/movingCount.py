class Solution:
    def __init__(self):
        self.set_ = set()
        self.threshold = None
        self.rows = None
        self.cols = None


    def movingCount(self, threshold, rows, cols):
        if threshold == 0:
            return 1
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        self.helper(0, 0)
        return len(self.set_)

    def helper(self, row, col):
        if (row, col) not in self.set_:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                sum_row = sum(list(map(int, list(str(row)))))
                sum_col = sum(list(map(int, list(str(col)))))
                if sum_col + sum_row <= self.threshold:
                    self.set_.add((row, col))
                    self.helper(row + 1, col)
                    self.helper(row - 1, col)
                    self.helper(row, col + 1)
                    self.helper(row, col - 1)


