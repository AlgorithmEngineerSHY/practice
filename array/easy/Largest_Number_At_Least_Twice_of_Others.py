class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        first_max = 0
        first_index = 0
        second_max = 0

        for idx, num in enumerate(nums):
            if num > first_max:
                second_max = first_max
                first_max = num
                first_index = idx
            elif num > second_max:
                second_max = num
        if first_max - second_max >= second_max:
            return first_index
        else:
            return -1
obj = Solution()
print(obj.dominantIndex([0,0,0,1]))