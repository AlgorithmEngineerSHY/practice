class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left_idx = self.helper(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        else:
            return [left_idx, self.helper(nums, target, False) - 1]
    def helper(self, nums, target, left):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target < nums[mid] or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low
