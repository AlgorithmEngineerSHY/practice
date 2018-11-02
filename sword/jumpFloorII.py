class Solution:
    def jumpFloorII(self, number):
        res = 1
        for i in range(1, number):
            res *= 2
        return res

