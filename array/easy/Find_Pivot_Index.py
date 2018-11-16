class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        right_sum = sum(nums[1:])
        left_sum = 0
        if right_sum == left_sum:
            return 0

        for idx in range(1, len(nums)):
            left_sum += nums[idx - 1]
            right_sum -= nums[idx]
            if left_sum == right_sum:
                return idx
        return -1

obj = Solution()
print(obj.pivotIndex([1,7,3,6,5,6]))