class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        for num in nums:
            res_tmp = []
            for re in res:
                for i in range(len(re) + 1):
                    res_tmp.append(re[:i] + [num] + re[i:])
            res = res_tmp
        return res