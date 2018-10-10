'''
Given a sorted array nums, 
remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = -1
        max_num = -float('inf')
        for num in nums:
            if num > max_num:
                max_num = num
                i += 1
                nums[i] = num

        return i + 1
