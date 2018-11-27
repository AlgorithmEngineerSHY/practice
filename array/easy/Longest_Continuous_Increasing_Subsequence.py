class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        len_nums = len(nums)
        tmp_count = 1
        for i in range(1, len_nums):
            if nums[i] > nums[i - 1]:
                tmp_count += 1
            else:
                res = max(res, tmp_count)
                tmp_count = 1
        res = max(res, tmp_count)
        return res

