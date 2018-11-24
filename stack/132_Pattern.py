class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p_3 = -float('inf')
        stack = []
        for num in nums[::-1]:
            if num < p_3:
                return True
            while stack and stack[-1] < num:
                p_3 = stack.pop()
            stack.append(num)
        return False