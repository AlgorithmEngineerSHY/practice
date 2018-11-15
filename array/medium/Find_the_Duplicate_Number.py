class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        x = nums[slow]
        y = nums[0]
        while x != y:
            x = nums[x]
            y = nums[y]
        return x

obj = Solution()
print(obj.findDuplicate([1,3,4,2,2]))
