class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        helper_list = [1] * len_nums

        for i in range(len_nums):

            for j in range(i):
                if nums[i] > nums[j]:
                    helper_list[i] = max(helper_list[i], helper_list[j] + 1)
        return max(helper_list)

obj = Solution()
print(obj.lengthOfLIS([10,9,2,5,3,7,101,18]))

