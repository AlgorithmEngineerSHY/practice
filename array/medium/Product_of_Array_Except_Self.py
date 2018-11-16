from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_zero = nums.count(0)
        if n_zero == 0:
            product = reduce(lambda x, y: x * y, nums)
            return [product // x for x in nums]
        if n_zero > 1:
            return [0] * len(nums)
        if n_zero == 1:
            idx_zero = nums.index(0)
            res = [0] * len(nums)
            nums.remove(0)
            product = reduce(lambda x, y: x * y, nums)
            res[idx_zero] = product
            return res

obj = Solution()
print(obj.productExceptSelf([1,2,3,4]))