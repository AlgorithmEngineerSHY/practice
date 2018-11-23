class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]
        if len_nums == 2 or len_nums == 3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        len_nums = len(nums)
        dp = [0] * len_nums
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len_nums):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]