from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n_zeros = nums.count(0)
        for i in range(n_zeros):
            nums.remove(0)
        nums = list(map(str, nums))
        func = lambda x, y: int(x + y) - int(y + x)
        nums = sorted(nums, key=cmp_to_key(func), reverse=True)
        res = ''.join(nums)
        res += '0' * n_zeros
        if res[0] == '0':
            return '0'
        else:
            return res
obj = Solution()
print(obj.largestNumber([3,30,34,5,9]))
