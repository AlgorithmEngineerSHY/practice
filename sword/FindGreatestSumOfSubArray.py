class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = array[0]
        tmp_sum = 0
        for i in array:
            tmp_sum = max(tmp_sum + i, i)
            res = max(res, tmp_sum)
        return res