class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        return self.helper(nums)

    def helper(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            num_left = nums[left]
            num_mid = nums[mid]
            num_right = nums[right]
            if num_left <= num_mid:
                if num_mid < num_right:
                    return num_left
                else:
                    left = mid + 1
            else:
                right = mid
        return nums[left]

obj = Solution()
print(obj.findMin([1]))