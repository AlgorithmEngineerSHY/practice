class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if target < nums[0] or target > nums[-1]:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]
            if target == mid_num:
                return mid
            elif target < mid_num:
                right = mid - 1
            else:
                left = mid + 1
        return -1