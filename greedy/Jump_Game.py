class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_idx = len(nums) - 1
        max_tmp = 1
        for i, num in enumerate(nums):
            if i == last_idx:
                return True
            max_tmp = max(max_tmp - 1, num)
            if max_tmp == 0:
                return False