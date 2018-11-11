class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        for i in range(len_n - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len_n - 1