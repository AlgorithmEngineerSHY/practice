class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = sum_nums // 2
        helper_list = [False] * (target + 1)
        helper_list[0] = True
        for num in nums:
            for idx in range(target, num - 1, -1):
                helper_list[idx] = helper_list[idx] or helper_list[idx - num]
            if helper_list[-1] == True:
                return True
        return False



# class Solution:
#     def __init__(self):
#         self.res = False
#         self.nums = None
#         self.len_nums = None
#
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#
#         sum_nums = sum(nums)
#         if sum_nums % 2 != 0:
#             return False
#         nums.sort(reverse=True)
#         self.len_nums = len(nums)
#         self.nums = nums
#         self.helper(0, sum_nums // 2)
#         return self.res
#
#     def helper(self, idx, target):
#         if self.res:
#             return None
#         if target == 0:
#             self.res = True
#             return None
#         if target < 0:
#             return None
#         for i in range(idx + 1, self.len_nums):
#             self.helper(i, target - self.nums[i])
# obj = Solution()
# print(obj.canPartition([1, 5, 11, 5]))
