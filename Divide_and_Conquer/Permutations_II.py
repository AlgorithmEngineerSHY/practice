class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        for num in nums:
            tmp_re = []
            for re in res:

                for i in range(len(re) + 1):
                    tmp_re.append(re[:i] + [num] + re[i:])
                    if i < len(re) and num == re[i]:
                        break
            res = tmp_re
        return res