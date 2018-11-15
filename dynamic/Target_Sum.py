class Solution:

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_nums = sum(nums)
        if sum_nums < S or S < -sum_nums:
            return 0
        if (sum_nums + S) % 2 != 0:
            return 0
        target = (sum_nums + S) // 2
        helper_list = [0] * (target + 1)
        helper_list[0] = 1

        for num in nums:
            for idx in range(target, num - 1, -1):
                helper_list[idx] += helper_list[idx - num]
        return helper_list[-1]



# class Solution:
#     def __init__(self):
#         self.res = 0
#         self.nums = None
#         self.target = None
#         self.len_nums = None
#
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         self.nums = nums
#         self.target = S
#         self.len_nums = len(nums)
#         self.helper(-1, 0)
#         return self.res
#
#     def helper(self, idx, tmp_sum):
#         if idx == self.len_nums - 1:
#             if tmp_sum == self.target:
#                 self.res += 1
#             return None
#         self.helper(idx + 1, tmp_sum + self.nums[idx + 1])
#         self.helper(idx + 1, tmp_sum - self.nums[idx + 1])
