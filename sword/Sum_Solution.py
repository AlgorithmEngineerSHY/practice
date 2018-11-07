
class Solution:
    def __init__(self):
        self.sum_ = 0

    def Sum_Solution(self, n):
        self.helper(n)
        return self.sum_

    def helper(self, n):
        if n == 0:
            return None
        self.sum_ += n
        n -= 1
        self.helper(n)