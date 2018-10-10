'''
Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
'''


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                tmp_re = 1
                tmp_num = num + 1
                while tmp_num in num_set:
                    tmp_re += 1
                    tmp_num += 1
                re = max(re, tmp_re)
        return re




