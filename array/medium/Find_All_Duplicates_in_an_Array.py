# from collections import Counter
# class Solution:
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         c = Counter(nums)
#         return [x for x in c if c[x] == 2]

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res